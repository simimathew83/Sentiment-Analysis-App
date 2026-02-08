# Sentiment Analysis App

A simple Python Streamlit application that analyzes the sentiment of user-entered text using TextBlob.

## Description

This app allows a user to enter a sentence and determines whether the sentiment is:
- Positive
- Negative
- Neutral

It also displays the sentiment polarity score.

## Tech Stack

- Python
- Streamlit
- TextBlob

## How to Run (Windows)

1. Create a virtual environment:

```bash
    python -m venv venv

2.Activate the virtual environment:
    .\venv\Scripts\Activate

3. Install dependencies
    pip install -r requirements.txt
    python -m textblob.download_corpora

4. Run the application:
    streamlit run app.py


##Files:
app.py – Streamlit application code
requirements.txt – Project dependencies
README.md – Project documentation


##Output
The app displays:

- Sentiment category (positive / negative / neutral)
- Sentiment polarity score
