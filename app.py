import streamlit as st
from summarizer_utils import summarize_reviews
from mongodb_connection import get_reviews, collection

# Page Config
st.set_page_config(page_title="AI Review Summarizer", layout="wide")

# ----------------- CUSTOM CSS -----------------
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
    }
    .title-text {
        text-align: center;
        color: #4CAF50;
        font-size: 38px;
        font-weight: bold;
        margin-top: 10px;
    }
    .subtext {
        text-align: center;
        color: gray;
        font-size: 16px;
        margin-bottom: 30px;
    }
    .review-box {
        background-color: rgba(255, 255, 255, 0.07);
        padding: 15px 20px;
        margin-bottom: 15px;
        border-left: 5px solid #4CAF50;
        border-radius: 8px;
        color: white;
    }
    .summary-box {
        background-color: rgba(0, 255, 100, 0.08);
        padding: 20px;
        margin: 20px 0;
        border-left: 6px solid #4CAF50;
        border-radius: 10px;
        font-size: 18px;
        color: white;
    }
    .ai-note {
        color: #ccc;
        font-size: 14px;
        margin-top: -10px;
    }
    .submit-btn > button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        font-weight: bold;
        padding: 8px 20px;
    }
    .submit-btn > button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------- PAGE TITLE -----------------
st.markdown("<div class='title-text'>AI-Powered Review Summarizer</div>", unsafe_allow_html=True)
st.markdown("<div class='subtext'>Fetch customer reviews from the database and generate summaries using AI</div>", unsafe_allow_html=True)

# ----------------- SUMMARIZE REVIEWS -----------------
if st.button("Generate AI Summary", use_container_width=True):
    reviews = get_reviews()

    if reviews:
        # Display Reviews
        st.markdown("### :green_book: Customer Reviews")
        for i, review in enumerate(reviews, 1):
            st.markdown(f"""
                <div class='review-box'>
                    <strong>Review {i}</strong><br>{review}
                </div>
            """, unsafe_allow_html=True)

        # Generate Summary
        st.markdown("### :robot_face: AI-Generated Summary")
        summary = summarize_reviews(reviews)
        st.markdown(f"<div class='summary-box'>{summary}</div>", unsafe_allow_html=True)
        st.markdown("<div class='ai-note'>This summary is generated using an AI model (OpenAI).</div>", unsafe_allow_html=True)
    else:
        st.warning("No reviews found in the database.")

# ----------------- ADD NEW REVIEW -----------------
st.markdown("---")
st.markdown("### :memo: Add a New Review")

with st.form("add_review_form"):
    new_review = st.text_area("Write your review here:", height=100)
    submitted = st.form_submit_button("Submit Review")
    if submitted and new_review.strip():
        collection.insert_one({"review": new_review})
        st.success("Thank you! Your review has been added.")