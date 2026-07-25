# ============================================================
# SHL Assessment Recommendation System
# Author: Rushikesh Raghatate
# ============================================================

import time
import requests
import streamlit as st
import datetime

# ============================================================
# CONFIG
# ============================================================

API_URL = "https://shl-assessment-api-ekjl.onrender.com"

st.set_page_config(
    page_title="SHL Assessment Recommendation",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "example_prompt" not in st.session_state:
    st.session_state.example_prompt = None

if "backend_online" not in st.session_state:
    st.session_state.backend_online = False

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def render_recommendation_cards(recommendations):
    """Renders assessment cards in a clean 2-column grid."""
    if not recommendations:
        return

    st.markdown("### 📋 Recommended Assessments")
    cols = st.columns(2)

    for i, rec in enumerate(recommendations):
        with cols[i % 2]:
            with st.container(border=True):
                st.markdown(f"#### 🧠 {rec.get('name', 'Unknown')}")
                st.caption(f"**Type:** {rec.get('test_type', 'Assessment')}")

                if rec.get("description"):
                    with st.expander("Description"):
                        st.write(rec["description"])

                if rec.get("url"):
                    st.link_button(
                        "🔗 View Assessment",
                        rec["url"],
                        use_container_width=True
                    )

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>
#MainMenu { visibility:hidden; }
footer { visibility:hidden; }
header { visibility:hidden; }

html, body, [data-testid="stAppViewContainer"] {
    background: #F5F7FB;
    font-family: Inter, sans-serif;
}
.block-container {
    padding-top: 2rem;
    padding-bottom: 1rem;
    padding-left: 3rem;
    padding-right: 3rem;
}
.hero {
    text-align: center;
    margin-top: 130px;
    margin-bottom: 80px;
}
.hero h1 {
    font-size: 60px;
    font-weight: 700;
    color: #1E3A8A;
    margin-bottom: 10px;
}
.hero p {
    font-size: 20px;
    color: #6B7280;
}

/* Custom CSS to make the sidebar metrics text a bit smaller so they fit side-by-side */
[data-testid="stMetricValue"] {
    font-size: 1.5rem;
}
[data-testid="stMetricLabel"] {
    font-size: 0.85rem;
}

/* Custom CSS to Bold and Color the Chat Input Placeholder */
[data-testid="stChatInput"] textarea::placeholder {
    font-weight: 800 !important;
    color: #1E3A8A !important;
    opacity: 0.8 !important;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.title("🧠 SHL AI")
    st.markdown("---")
    
    st.subheader("Backend Status")
    try:
        response = requests.get(f"{API_URL}/health", timeout=4)
        if response.status_code == 200:
            st.success("🟢 Backend Online")
            st.session_state.backend_online = True
        else:
            st.error("Backend Error")
    except requests.exceptions.RequestException:
        st.error("Backend Offline")

    st.markdown("---")
    
    # --------------------------------------------------------
    # SMALL PARALLEL METRICS
    # --------------------------------------------------------
    st.markdown("<b>📊 Session Metrics</b>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.metric("Messages", len(st.session_state.messages))
    c2.metric("User", len([x for x in st.session_state.messages if x["role"] == "user"]))
    c3.metric("Assistant", len([x for x in st.session_state.messages if x["role"] == "assistant"]))

    st.markdown("---")
    if st.button("🗑 New Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    
    # --------------------------------------------------------
    # CENTERED & BOLDED FOOTER IN SIDEBAR WITH COLOR PATTERN
    # --------------------------------------------------------
    current_year = datetime.datetime.now().year
    st.markdown(f"""
    <div style="text-align: center; margin-top: 25px; line-height: 1.6;">
        <span style="font-size: 1.1em; font-weight: 800; color: #1E3A8A;">🧠 SHL Assessment Recommendation System</span><br>
        <span style="font-size: 0.85em; font-weight: 700; color: #2563EB;">Built using FastAPI • FAISS • Sentence Transformers • Docker • Streamlit</span><br><br>
        <span style="font-size: 0.9em; font-weight: 700; color: #4B5563;">© {current_year} Rushikesh Raghatate</span>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# LANDING PAGE
# ============================================================

if len(st.session_state.messages) == 0:
    st.markdown("""
    <div class="hero">
        <h1>What's the vibe, Recruiter?</h1>
        <p>AI-powered SHL Assessment Recommendation System</p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()
    st.subheader("💡 Try asking")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Recommend assessments for Java Developer", use_container_width=True):
            st.session_state.example_prompt = "Recommend assessments for Java Developer"
        if st.button("Recommend assessments for Data Scientist", use_container_width=True):
            st.session_state.example_prompt = "Recommend assessments for Data Scientist"
        if st.button("Graduate Hiring", use_container_width=True):
            st.session_state.example_prompt = "Graduate Hiring"
    with col2:
        if st.button("Difference between OPQ and GSA", use_container_width=True):
            st.session_state.example_prompt = "Difference between OPQ and GSA"
        if st.button("Sales Hiring", use_container_width=True):
            st.session_state.example_prompt = "Sales Hiring"
        if st.button("Leadership Assessments", use_container_width=True):
            st.session_state.example_prompt = "Leadership Assessments"

# ============================================================
# CHAT ENGINE
# ============================================================

# 1. Display previous conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message["role"] == "assistant" and message.get("recommendations"):
            render_recommendation_cards(message["recommendations"])

# 2. Chat Input
user_prompt = st.chat_input("Ask SHL AI...")

# Handle example prompt click from the Landing Page
if st.session_state.example_prompt:
    user_prompt = st.session_state.example_prompt
    st.session_state.example_prompt = None

# 3. Process new user input
if user_prompt:
    # Append and show user message
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Assistant response
    with st.chat_message("assistant"):
        placeholder = st.empty()
        placeholder.markdown("🤖 Thinking...")

        payload = {"messages": [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]}

        try:
            with st.spinner("Searching SHL catalog..."):
                response = requests.post(f"{API_URL}/chat", json=payload, timeout=90)
                response.raise_for_status()
                data = response.json()

            reply = data.get("reply", "No response received.")
            recommendations = data.get("recommendations", [])
            end_chat = data.get("end_of_conversation", False)

            # Typing animation
            typed = ""
            for word in reply.split():
                typed += word + " "
                placeholder.markdown(typed + "▌")
                time.sleep(0.03)
            placeholder.markdown(reply)

            # Render new recommendations
            if recommendations:
                render_recommendation_cards(recommendations)

            if end_chat:
                st.info("Conversation completed.")

            # Save assistant message
            st.session_state.messages.append({
                "role": "assistant",
                "content": reply,
                "recommendations": recommendations
            })
            
            # Rerun to update the metrics in the sidebar seamlessly
            st.rerun()

        except requests.exceptions.RequestException as e:
            placeholder.error(f"Unable to connect to backend.\n\n{e}")
            st.stop()

# ============================================================
# BOTTOM CONTROLS
# ============================================================

if len(st.session_state.messages) > 0:
    st.divider()
    col1, col2 = st.columns(2)
    
    with col1:
        # Download Chat
        conversation = ""
        for msg in st.session_state.messages:
            conversation += f"{msg['role'].upper()}\n{msg['content']}\n\n"
            
        st.download_button(
            "📄 Download Conversation",
            conversation,
            file_name="conversation.txt",
            use_container_width=True
        )
        
    with col2:
        # Clear Chat
        if st.button("🗑 Clear Conversation", use_container_width=True):
            st.session_state.messages = []
            st.rerun()