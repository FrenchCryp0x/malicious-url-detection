# app.py

import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from huggingface_hub import login
import os

# Load Hugging Face token from Streamlit secrets
hf_token = st.secrets["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"]
login(hf_token)

# Load model and tokenizer using token
model_name = "r3ddkahili/final-complete-malicious-url-model"
model = AutoModelForSequenceClassification.from_pretrained(model_name, use_auth_token=hf_token)
tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=hf_token)

label_mapping = {0: "Benign", 1: "Defacement", 2: "Phishing", 3: "Malware"}

def predict_url(url):
    tokens = tokenizer(url, truncation=True, padding=True, max_length=128, return_tensors="pt")
    with torch.no_grad():
        output = model(**tokens)
        probabilities = torch.softmax(output.logits, dim=1).squeeze()
        predicted_label = torch.argmax(probabilities).item()
        predicted_percentage = probabilities[predicted_label].item() * 100
        return label_mapping[predicted_label], predicted_percentage

# Streamlit App UI
st.title("Malicious URL Detection")
url_input = st.text_input("Enter a URL to analyze:")

if st.button("Analyze URL"):
    if url_input:
        label, percentage = predict_url(url_input)
        color = "green" if label == "Benign" else "red"
        st.markdown(
            f"<h3>Prediction: <span style='color:{color}'>{label} ({percentage:.2f}%)</span></h3>",
            unsafe_allow_html=True,
        )
    else:
        st.warning("Please enter a valid URL.")
