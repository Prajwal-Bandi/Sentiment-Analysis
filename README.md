# 📝 Amazon Product Reviews Sentiment Analysis

This project is a **Natural Language Processing (NLP)** based system designed to classify user sentiments into **Positive**, **Negative**, and **Neutral** categories using Amazon product review data. The goal of this project is to extract meaningful insights from user-generated content to improve customer satisfaction and business decisions.

---

## 🚀 Project Overview

The sentiment analysis model was trained on product reviews collected from Amazon. It analyzes review text and classifies it into one of three sentiment categories:
- ✅ **Positive**
- ⚠️ **Neutral**
- ❌ **Negative**

This project demonstrates how machine learning and NLP can be used to automate opinion mining and support better product analysis and recommendation systems.

---

## 🧠 Technologies and Tools Used

- **Python**
- **Pandas, NumPy** – Data manipulation
- **NLTK, SpaCy, TextBlob** – Natural Language Processing
- **Scikit-learn** – Machine learning models
- **TF-IDF Vectorizer** – Feature extraction
- **Matplotlib, Seaborn** – Data visualization
- **Streamlit** – Web app deployment

---

## ⚙️ Workflow

### 1. Data Preprocessing
- **Tokenization** – Breaking text into sentences and words
- **Stopword Removal** – Removing common words with low information
- **Stemming** – Reducing words to their root form
- **Vectorization** – Using **TF-IDF** to convert text into numerical form
- **Sentiment Polarity Analysis** – Using **TextBlob** to compute polarity scores for classification

### 2. Model Building & Evaluation
- Applied multiple ML algorithms:
  - Support Vector Machine (SVM)
  - Logistic Regression
  - Random Forest Classifier
  - Naive Bayes Classifier
  - Decision Tree Classifier
- Implemented **ensemble modeling** to boost accuracy
- Evaluated using:
  - Accuracy
  - Precision
  - Recall
  - F1-score

### 3. Deployment
- Built an interactive **Streamlit web application**
- Allows users to input custom text
- Displays real-time sentiment classification and polarity score

---

## 💻 How to Run the Project

1. Clone the repository or download the `.ipynb` and related files.
2. Install required libraries:
   ```bash
   pip install -r requirements.txt
3.Run the command
```bash
   streamlit run app.py



