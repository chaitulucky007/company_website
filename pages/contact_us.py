import streamlit as st
import pandas as pd
from send_mail import send_mail
df = pd.read_csv("topics.csv")

with st.form(key="Contact_us_forum"):
    email = st.text_input("Your Email Address")
    topics = st.selectbox(label="What topic do you want to discuss?",
                          options=df)

    raw_message = st.text_area("Text")
    message1 = f'''\
Subject: New message from chaitu

{raw_message}
'''

    button = st.form_submit_button("Submit")
    print(button)
    if button:
        send_mail(receiver = email, message = message1)





