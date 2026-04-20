import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# Load env
load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))

# LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)

# Page config
st.set_page_config(page_title="ELI5 AI", page_icon="🧠", layout="centered")

# 🔥 CUSTOM STYLES
st.markdown("""
<style>
.main {
    max-width: 700px;
    margin: auto;
}

.block-container {
    padding-top: 2rem;
}

h1 {
    text-align: center;
}

.subtext {
    text-align: center;
    color: #9aa0a6;
    margin-bottom: 30px;
}

.stTextInput > div > div > input {
    border-radius: 10px;
    padding: 10px;
}

.stSelectbox > div {
    border-radius: 10px;
}

.stButton>button {
    border-radius: 10px;
    padding: 12px 25px;
    background: linear-gradient(90deg, #4CAF50, #2E7D32);
    color: white;
    font-weight: bold;
    border: none;
}

.result-card {
    background-color: #1e1e1e;
    padding: 20px;
    border-radius: 12px;
    margin-top: 25px;
    border: 1px solid #333;
}

</style>
""", unsafe_allow_html=True)

# 🔥 HEADER
st.markdown("<h1>🧠 Explain Like I'm 5 AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtext'>Turn complex ideas into simple explanations</p>", unsafe_allow_html=True)

# INPUTS
topic = st.text_input("Enter a topic")

level = st.selectbox(
    "Select explanation level",
    ["Kid", "Beginner", "Expert"]
)

# BUTTON
if st.button("✨ Explain Now"):

    if topic.strip() == "":
        st.warning("⚠️ Please enter a topic")
    else:
        template = """
        Explain the following topic in a {level} level.

        Topic: {topic}

        Keep it simple, clear, and engaging.
        """

        prompt = PromptTemplate(
            input_variables=["topic", "level"],
            template=template
        )

        final_prompt = prompt.format(topic=topic, level=level)

        # 🔥 LOADING
        with st.spinner("Thinking... 🤖"):
            response = llm.invoke(final_prompt)

        # 🔥 OUTPUT CARD
        st.markdown(f"""
        <div class="result-card">
            <h4>📖 Explanation</h4>
            <p>{response.content}</p>
        </div>
        """, unsafe_allow_html=True)