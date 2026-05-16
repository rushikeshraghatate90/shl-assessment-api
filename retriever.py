import faiss
import pickle
import numpy as np
import re

from sentence_transformers import SentenceTransformer

# =========================
# LOAD MODEL
# =========================

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# =========================
# LOAD INDEX
# =========================

index = faiss.read_index(
    "shl_index.faiss"
)

# =========================
# LOAD METADATA
# =========================

with open(
    "catalog_metadata.pkl",
    "rb"
) as f:

    catalog = pickle.load(f)

print("Retriever loaded successfully!")

# =========================
# CLEAN TEXT
# =========================

def clean_text(text):

    text = text.lower()

    text = re.sub(
        r"[^a-z0-9\s]",
        " ",
        text
    )

    return text

# =========================
# TECHNICAL TERMS
# =========================

TECH_TERMS = [
    "java",
    "python",
    "developer",
    "software",
    "backend",
    "frontend",
    "coding",
    "programming",
    "engineer",
    "framework",
    "api"
]

# =========================
# COMMUNICATION TERMS
# =========================

COMM_TERMS = [
    "communication",
    "leadership",
    "stakeholder",
    "collaboration",
    "teamwork",
    "manager"
]

# =========================
# SCORING FUNCTION
# =========================

def calculate_score(query, item, rank):

    query_clean = clean_text(query)

    item_name = clean_text(item["name"])

    item_text = clean_text(item["search_text"])

    # =========================
    # BASE SEMANTIC SCORE
    # =========================

    score = 100 - rank

    # =========================
    # TECHNICAL BOOSTS
    # =========================

    for term in TECH_TERMS:

        if term in query_clean:

            if term in item_name:
                score += 50

            if term in item_text:
                score += 25

    # =========================
    # COMMUNICATION BOOSTS
    # =========================

    for term in COMM_TERMS:

        if term in query_clean:

            if term in item_text:
                score += 10

    return score

# =========================
# MAIN RETRIEVAL
# =========================

def retrieve_assessments(query, top_k=5):

    # =========================
    # QUERY EMBEDDING
    # =========================

    query_embedding = model.encode([query])

    # =========================
    # VECTOR SEARCH
    # =========================

    distances, indices = index.search(
        np.array(
            query_embedding,
            dtype=np.float32
        ),
        40
    )

    scored_results = []

    # =========================
    # SCORE RESULTS
    # =========================

    for rank, idx in enumerate(indices[0]):

        item = catalog[idx]

        score = calculate_score(
            query,
            item,
            rank
        )

        scored_results.append(
            (score, item)
        )

    # =========================
    # SORT RESULTS
    # =========================

    scored_results.sort(
        key=lambda x: x[0],
        reverse=True
    )

    # =========================
    # REMOVE DUPLICATES
    # =========================

    seen = set()

    final_results = []

    for score, item in scored_results:

        if item["name"] in seen:
            continue

        seen.add(item["name"])

        test_type = "Unknown"

        if item.get("test_types"):

            if isinstance(item["test_types"], list):

                if len(item["test_types"]) > 0:

                    test_type = item["test_types"][0]

        final_results.append({
            "name": item["name"],
            "url": item["url"],
            "description": item["description"],
            "duration": item["duration"],
            "test_type": test_type
        })

        if len(final_results) >= top_k:
            break

    return final_results

