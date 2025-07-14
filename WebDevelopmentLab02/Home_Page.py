import streamlit as st

# Title of App

st.title("Web Development Lab 02")

# Assignment Data 
# TODO: Fill out your team number, section, and team members


st.header("CS 1301")
st.subheader("Team  Members: Nathan")

# Introduction
# TODO: Write a quick description for all of your pages in this lab below, in the form:
#       1. **Page Name**: Description
#       2. **Page Name**: Description
#       3. **Page Name**: Description
#       4. **Page Name**: Description


st.write("""
Welcome to our Streamlit Web Development Lab03 app! You can navigate between the pages using the sidebar to the left. The following pages are:

1. Movie Explorer: Browse and filter popular movies by genre, rating, and release year. View trailers, cast, and other metadata directly from TMDB.

2. Review Analyzer: An LLM-powered tool that summarizes and classifies audience reviews by sentiment, themes, and tone, to help understand viewer reactions at a glance.

3. CineBot (Gemini): A conversational chatbot trained on TMDB data that answers detailed movie-related questions and provides intelligent recommendations.
""")

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Film_Reel_icon.svg/1024px-Film_Reel_icon.svg.png", width=150)

st.markdown("Use the sidebar to begin exploring.")
