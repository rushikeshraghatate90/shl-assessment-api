from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import pickle

from retriever import retrieve_assessments

# =========================
# LOAD CATALOG
# =========================

with open("catalog_metadata.pkl", "rb") as f:
    catalog_data = pickle.load(f)

# =========================
# FASTAPI APP
# =========================

app = FastAPI(
    title="SHL Assessment Recommendation API",
    description="AI-powered SHL assessment recommendation system",
    version="1.0.0"
)

# =========================
# REQUEST MODELS
# =========================

class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]

# =========================
# RESPONSE MODELS
# =========================

class Recommendation(BaseModel):
    name: str
    url: str
    test_type: str


class ChatResponse(BaseModel):
    reply: str
    recommendations: List[Recommendation]
    end_of_conversation: bool

# =========================
# ROOT ENDPOINT
# =========================

@app.get("/")
def root():

    return {
        "message": "SHL Assessment Recommendation API is running"
    }

# =========================
# HEALTH ENDPOINT
# =========================

@app.get("/health")
def health():

    return {
        "status": "ok"
    }

# =========================
# BUILD FULL CONTEXT
# =========================

def build_context(messages):

    user_messages = []

    for msg in messages:

        if msg.role.lower() == "user":

            user_messages.append(
                msg.content
            )

    return " ".join(user_messages)

# =========================
# OFF TOPIC DETECTION
# =========================

def is_off_topic(query):

    query = query.lower()

    off_topic_words = [
        "bitcoin",
        "crypto",
        "weather",
        "movie",
        "football",
        "recipe",
        "politics",
        "stocks",
        "tax"
    ]

    return any(
        word in query
        for word in off_topic_words
    )

# =========================
# NEEDS CLARIFICATION
# =========================

def needs_clarification(query):

    query = query.lower().strip()

    vague_queries = [
        "assessment",
        "test",
        "developer",
        "engineer",
        "manager"
    ]

    if len(query.split()) <= 2:
        return True

    if query in vague_queries:
        return True

    return False

# =========================
# COMPARISON FUNCTION
# =========================

def compare_assessments(query):

    query_lower = query.lower()

    # =========================
    # DETECT COMPARISON INTENT
    # =========================

    comparison_keywords = [
        "difference",
        "compare",
        "vs",
        "versus"
    ]

    is_comparison = any(
        word in query_lower
        for word in comparison_keywords
    )

    if not is_comparison:
        return None

    # =========================
    # FIND MATCHING ASSESSMENTS
    # =========================

    matched = []

    for item in catalog_data:

        name_lower = item["name"].lower()

        # OPQ
        if "opq" in query_lower and "opq" in name_lower:

            matched.append(item)

        # GSA
        if "gsa" in query_lower and "gsa" in name_lower:

            matched.append(item)

    # =========================
    # REMOVE DUPLICATES
    # =========================

    unique_matches = []

    seen = set()

    for item in matched:

        if item["name"] not in seen:

            seen.add(item["name"])

            unique_matches.append(item)

    matched = unique_matches

    # =========================
    # VALIDATE
    # =========================

    if len(matched) < 2:

        return (
            "I could not find enough SHL "
            "assessments to compare."
        )

    # =========================
    # PICK FIRST TWO
    # =========================

    assessment_a = matched[0]

    assessment_b = matched[1]

    # =========================
    # BUILD RESPONSE
    # =========================

    reply = f"""
Comparison between {assessment_a['name']} and {assessment_b['name']}:

{assessment_a['name']}:
{assessment_a['description'][:300]}

{assessment_b['name']}:
{assessment_b['description'][:300]}
"""

    return reply.strip()

# =========================
# CHAT ENDPOINT
# =========================

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    # =========================
    # VALIDATE REQUEST
    # =========================

    if not request.messages:

        raise HTTPException(
            status_code=400,
            detail="Messages cannot be empty"
        )

    latest_message = (
        request.messages[-1]
        .content
        .strip()
    )

    if not latest_message:

        raise HTTPException(
            status_code=400,
            detail="Empty message"
        )

    # =========================
    # BUILD FULL CONTEXT
    # =========================

    full_context = build_context(
        request.messages
    )

    # =========================
    # OFF TOPIC HANDLING
    # =========================

    if is_off_topic(full_context):

        return ChatResponse(
            reply=(
                "I can only help with SHL "
                "assessment recommendations."
            ),
            recommendations=[],
            end_of_conversation=False
        )

    # =========================
    # COMPARISON HANDLING
    # =========================

    comparison_reply = compare_assessments(
        full_context
    )

    if comparison_reply:

        return ChatResponse(
            reply=comparison_reply,
            recommendations=[],
            end_of_conversation=False
        )

    # =========================
    # CLARIFICATION HANDLING
    # =========================

    if needs_clarification(latest_message):

        return ChatResponse(
            reply=(
                "Could you provide more details "
                "about the role, required skills, "
                "seniority level, or assessment goals?"
            ),
            recommendations=[],
            end_of_conversation=False
        )

    # =========================
    # RETRIEVE ASSESSMENTS
    # =========================

    results = retrieve_assessments(
        full_context,
        top_k=5
    )

    # =========================
    # FORMAT RECOMMENDATIONS
    # =========================

    recommendations = []

    for item in results:

        recommendations.append(
            Recommendation(
                name=item["name"],
                url=item["url"],
                test_type=item["test_type"]
            )
        )

    # =========================
    # RETURN RESPONSE
    # =========================

    return ChatResponse(
        reply=(
            "Here are some recommended SHL "
            "assessments based on your hiring needs."
        ),
        recommendations=recommendations,
        end_of_conversation=False
    )

