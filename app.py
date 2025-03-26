import streamlit as st
from summarizer_utils import summarize_reviews
from mongodb_connection import get_reviews

st.set_page_config(page_title="AI Review Summarizer", layout="wide")

# Page Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>AI-Powered Review Summarizer</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: grey;'>Fetch customer reviews from database and summarize using OpenAI</h4>", unsafe_allow_html=True)
st.write("---")

# Button to summarize
if st.button("Generate AI Summary", use_container_width=True):
    reviews = get_reviews()
    
    if reviews:
        # Display all reviews in a nice format
        st.subheader("Customer Reviews")
        with st.container():
            for i, review in enumerate(reviews, 1):
                st.markdown(f"""
                    <div style="background-color:#f0f2f6; padding: 10px; margin-bottom: 8px; border-left: 5px solid #4CAF50;">
                        <strong>Review {i}:</strong><br>{review}
                    </div>
                """, unsafe_allow_html=True)

        st.write("---")

        # AI Summary
        st.subheader("AI-Generated Summary")
        summary = summarize_reviews(reviews)

        st.markdown(f"""
            <div style="background-color:#e8f5e9; padding: 20px; border-left: 5px solid #4CAF50; font-size: 16px;">
                {summary}
            </div>
        """, unsafe_allow_html=True)

        st.markdown("<p style='color: grey; font-size: 14px;'>This summary is generated using OpenAI's GPT model via LangChain.</p>", unsafe_allow_html=True)

    else:
        st.warning("No reviews found in the database.")

# Add Review Section (Optional)
st.write("---")
st.subheader("Add a New Review")
with st.form("Add Review"):
    new_review = st.text_area("Enter your review here:")
    submitted = st.form_submit_button("Submit Review")
    if submitted and new_review:
        from mongodb_connection import collection
        collection.insert_one({"review": new_review})
        st.success("Thank you! Your review has been added.")