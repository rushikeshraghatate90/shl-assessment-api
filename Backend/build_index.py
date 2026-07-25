import json
import pickle
import numpy as np
import faiss

from sentence_transformers import SentenceTransformer

# =========================
# LOAD CLEAN CATALOG
# =========================

with open("clean_catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

print("Catalog loaded:", len(catalog))

# =========================
# LOAD EMBEDDING MODEL
# =========================

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

print("Embedding model loaded!")

# =========================
# PREPARE SEARCH TEXTS
# =========================

texts = [
    item["search_text"]
    for item in catalog
]

print("Generating embeddings...")

# =========================
# GENERATE EMBEDDINGS
# =========================

embeddings = model.encode(
    texts,
    show_progress_bar=True,
    convert_to_numpy=True
)

print("Embedding shape:", embeddings.shape)

# =========================
# CREATE FAISS INDEX
# =========================

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

# Convert to float32
embeddings = np.array(
    embeddings,
    dtype=np.float32
)

# Add embeddings to index
index.add(embeddings)

print("FAISS index created!")

# =========================
# SAVE FAISS INDEX
# =========================

faiss.write_index(
    index,
    "shl_index.faiss"
)

print("FAISS index saved!")

# =========================
# SAVE METADATA
# =========================

with open(
    "catalog_metadata.pkl",
    "wb"
) as f:

    pickle.dump(catalog, f)

print("Metadata saved!")

# =========================
# DONE
# =========================

print("\nBuild completed successfully!")

