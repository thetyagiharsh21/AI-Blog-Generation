import streamlit as st
import google.generativeai as genai
from apikey import google_gemini_api_key

# Configure the GenerativeAI API
genai.configure(api_key=google_gemini_api_key)

# Define generation configuration and safety settings
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

# Create the GenerativeModel object
model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    generation_config=generation_config,
    safety_settings=safety_settings,
)

# Set Streamlit page layout
st.set_page_config(layout="wide")
st.title("Blogcraft: Your AI Writing Companion")
st.subheader("Craft perfect blogs with the help of AI - Blogcraft is your new AI blog companion")

# Sidebar for user inputs
with st.sidebar:
    st.title("Input your Blog")
    st.subheader("Enter Details of the blog you want to generate")

    # Blog title
    blog_title = st.text_input("Blog Title")

    # Keywords input
    keywords = st.text_area("Keywords (Comma separated)")

    # Number of words
    num_words = st.slider("Number of Words", min_value=100, max_value=2000, step=100)

    # Number of images
    num_images = st.number_input("Number of Images", min_value=0, max_value=10, step=1)

    prompt_parts = [
        f"Generate a comprehensive engaging blog post relevant to the given title \"{blog_title}\" and Keywords \"{keywords}\". Make sure to incorporate these keywords in the blog post. The Blog should be approximately {num_words} words in length, suitable for an online audience. Ensure the content is original, informative and maintains a consistent tone throughout"
    ]

# Submit Button
submit_button = st.button("Generate Blog")

if submit_button:
    response = model.generate_content(prompt_parts)
    st.write(response.text)


