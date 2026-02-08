import streamlit as st
from textblob import TextBlob

st.title("Sentiment Analysis App")

st.divider()

st.write("Enter a sentence to analyze its sentiment.")

#get the user input
user_input=st.text_input("Enter your sentence:")

# if the user has entered a sentence
if(user_input):
    blob = TextBlob(user_input)
    sentiment= blob.sentiment.polarity

    if(sentiment>0):
        st.write("Sentiment is positive :)")
    
    elif(sentiment<0):
        st.write("Sentiment is negative :(")

    else:
        st.write("Sentiment is neutral :I")

    st.write(f"Sentiment score: {sentiment}")

else:
    st.write("Please enter a sentence!")
        
