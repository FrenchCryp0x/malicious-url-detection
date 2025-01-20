# Malicious URL Detection using Fine-Tuned Model 

This project focuses on detecting malicious URLs using a fine-tuned BERT-based model. The application is designed to predict the nature of a given URL, such as benign, phishing, malware, or defacement, based on its characteristics. The model is enhanced to address overfitting issues and provide precise predictions.

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Model](#model)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction
Malicious URLs pose a significant cybersecurity threat by serving as vectors for phishing, malware distribution, and defacement attacks. This project leverages deep learning to classify URLs into four categories:
- **Benign**
- **Phishing**
- **Malware**
- **Defacement**

By employing a fine-tuned BERT model with techniques like QLoRA for optimization, the project ensures efficient training and precise results.

---

## Dataset
The dataset used for this project is sourced from Kaggle:  
[Malicious URLs Dataset](https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset)

### Dataset Features:
- **URLs**: The primary input, cleaned and tokenized for model training.
- **Labels**: Categorized as `benign`, `phishing`, `malware`, or `defacement`.

The dataset was preprocessed to lower-case URLs and map categorical labels into numerical representations.

---

## Model
- **Base Model**: `bert-base-uncased` from Hugging Face.
- **Optimization**: Fine-tuning performed with QLoRA (Quantized Low-Rank Adapters) to reduce overfitting and memory usage.
- **Evaluation Metrics**:
Loss: 0.0739
The model's average prediction error on the validation dataset.
Accuracy: 98.07%
The proportion of correctly classified URLs.
F1-Score: 98.06%
A harmonic mean of precision and recall, indicating balanced performance.
Precision: 98.07%
The proportion of correctly predicted positive instances out of all positive predictions.
Recall: 98.07%
The proportion of correctly predicted positive instances out of all actual positives.
Runtime: 523.58 seconds
Time taken for evaluation.
Samples per Second: 248.75
Processing speed during evaluation.

The model achieves high accuracy on validation datasets and produces robust predictions.

---

## Features
- Real-time URL classification with percentage probabilities.
- User-friendly web interface powered by **Streamlit**.
- Highlights predictions in color-coded format:
  - **Green** for benign predictions.
  - **Red** for malicious predictions.

---

## Setup Instructions

git clone https://github.com/your-username/malicious-url-detection.git
cd malicious-url-detection

### Step 1: Clone the Repository
```bash
Install Dependencies
Ensure Python 3.8+ is installed. Then, install the required libraries:
pip install -r requirements.txt

### Step 2: Clone the Repository
Run the Application
Launch the Streamlit app:
streamlit run app.py


Usage
Enter a URL in the input box.
Click the Search button.
View the prediction and corresponding probability in a user-friendly format.

Contributing
We welcome contributions to enhance this project. Feel free to:
Fork the repository.
Create a new feature branch: git checkout -b feature-name
Commit your changes: git commit -m "Add feature-name"
Push to the branch: git push origin feature-name
Submit a Pull Request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Dataset: Malicious URLs Dataset
Model: Hugging Face Transformers
Framework: Streamlit

For questions, feel free to contact us!
