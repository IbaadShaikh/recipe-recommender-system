# Recipe Recommendation System

## Project Overview

This project is a machine learning-powered recipe recommendation system that suggests recipes based on user-provided ingredients.

The application uses Natural Language Processing (NLP) techniques such as TF-IDF vectorization and Word2Vec embeddings to analyze ingredient similarity and recommend recipes from a dataset of over 5,000 recipes scraped from websites such as Jamie Oliver and AllRecipes.

The project includes:
- A Streamlit web application
- NLP preprocessing pipelines
- Content-based recommendation engine
- Web scraping utilities
- Meal planning and user feedback components

---

## Technologies Used

### Programming Language
- Python

### Libraries & Frameworks
- pandas
- numpy
- scikit-learn
- gensim
- BeautifulSoup
- Streamlit
- Flask
- pickle

---

## Installation

Install project dependencies:

```bash
pip install -r requirements.txt
```

---

## Repository Structure

```text
recipe-recommender-system/
│
├── input/          # Recipe datasets and processed data
├── models/         # Trained ML models and encodings
├── src/            # Core application source code
│   └── scraping/   # Web scraping utilities
│
├── README.md
├── requirements.txt
├── streamlit.py
├── setup.sh
├── config.py
└── .gitignore
```

---

## Web Scraping

Built a web scraper using BeautifulSoup to collect over 5,000 recipes from cooking websites.

The scraper extracts:
- Recipe names
- Ingredients
- Recipe URLs
- Ratings

---

## Data Cleaning & NLP Processing

The ingredient parser performs:
- Lemmatization
- Stopword removal
- Cooking measurement normalization
- Household ingredient filtering
- Lowercasing and punctuation cleanup
- Unicode normalization

---

## Model Building

### Word2Vec

Word2Vec embeddings were used to capture semantic relationships between ingredients commonly used together in recipes.

### TF-IDF

TF-IDF weighting was applied to improve distinguishing power between recipes by emphasizing more unique ingredients.

### Recommendation Engine

The recommendation system uses a content-based filtering approach to recommend recipes based on ingredient similarity.

Cosine similarity is used to compare user-input ingredients against recipe embeddings and return the most relevant recipe matches.

The model outputs:
- Top recommended recipes
- Ingredient lists
- Recipe URLs

Spacy and KNN approaches were also explored during experimentation, but cosine similarity provided the best balance of performance and simplicity.

---

## Features

- Recipe recommendations based on ingredients
- NLP-powered ingredient similarity analysis
- TF-IDF and Word2Vec integration
- Streamlit frontend interface
- Web scraping pipeline
- Modular project architecture
- Meal planning functionality
- User feedback system

---

## Future Improvements

- Deploy application publicly using Streamlit Cloud or Render
- Add user authentication
- Add nutritional analysis dashboard
- Improve recommendation accuracy
- Add recipe image support
- Containerize application using Docker

---

## Running the Application

### 1. Clone the Repository
```bash
git clone https://github.com/IbaadShaikh/recipe-recommender-system.git
cd recipe-recommender-system
```

### 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Generate TF-IDF Encodings
```bash
python src/tfidf_encoder.py
```

### 5. Run the Streamlit Application
```bash
streamlit run streamlit.py
```
The application will launch locally in your browser.

---

## Demo Video

https://github.com/user-attachments/assets/d52bb020-210e-4b7c-926d-e6ec8e1d0e13

---

## Author

Ibaad Shaikh
