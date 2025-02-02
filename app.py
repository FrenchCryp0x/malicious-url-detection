import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

token = "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"  # Replace with your token

model = AutoModelForSequenceClassification.from_pretrained(
    "r3ddkahili/final-complete-malicious-url-model", use_auth_token=token
)
tokenizer = AutoTokenizer.from_pretrained(
    "r3ddkahili/final-complete-malicious-url-model", use_auth_token=token
)


# Label mapping
label_mapping = {0: "Benign", 1: "Defacement", 2: "Phishing", 3: "Malware"}

# Function to preprocess and predict URL
def predict_url(url):
    tokens = tokenizer(url, truncation=True, padding=True, max_length=128, return_tensors="pt")
    with torch.no_grad():
        output = model(**tokens)
        probabilities = torch.softmax(output.logits, dim=1).squeeze()
        predicted_label = torch.argmax(probabilities).item()
        predicted_percentage = probabilities[predicted_label].item() * 100
        return label_mapping[predicted_label], predicted_percentage

# Streamlit App
st.title("Malicious URL Detection")

# URL Input
url_input = st.text_input("Enter a URL to analyze:")
if st.button("Analyze URL"):
    if url_input:
        label, percentage = predict_url(url_input)

        # Highlight prediction color based on label
        if label == "Benign":
            color = "green"
        else:
            color = "red"

        # Display result
        st.markdown(
            f"<h3>Prediction: <span style='color:{color}'>{label} ({percentage:.2f}%)</span></h3>",
            unsafe_allow_html=True,
        )
    else:
        st.warning("Please enter a valid URL.")
