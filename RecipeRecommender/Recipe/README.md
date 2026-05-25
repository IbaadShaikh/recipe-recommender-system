# Recipe Recommendation System
## Project Overview
* In order to encourage healthier eating among students, I developed a recipe recommendation tool that takes user input into account. I culled more than 5,000 soup recipes from sites like Jamie Oliver and All Recipes.
* Parsed  ingredients and created word embeddings using Word2Vec and TF-IDF.
* Implemented a method for recommending recipes based on their word embeddings by calculating the cosine similarity as a measure of the euclidean distance between them.
* Built a client-facing API using flask, and a user-friendly [app] with Streamlit.

## Code 
**Python Version:** 3.7  
**Packages:** pandas, numpy, sklearn, gensim, matplotlib, seaborn, beautifulsoup, flask, streamlit, json, pickle  
**For Web Framework Requirements:**  ```pip install -r requirements.txt```  
**You can run this model yourself using my API:**

<p align="center">
<img src="./input/flowchart.png" width="513" height="350">
</p>

## Web Scraping
Built a **web scraper** using [Beautiful Soup] to scrape over 5000 food recipes from For each recipe and retrieve the following:

* Recipe name 
* Ingredients
* URL
* Rating

## Data Cleaning
 The **ingredient parser** does the following:
* Lemmatize words to ensure we remove all versions of words, e.g. both pounds and pound
* Removed stopwords 
* Removed cooking measures
* Removed common household items, such as oil
* standard NLP preprocessing: getting rid of punctuation, removing accents, making everything lowercase, getting rid of Unicode, etc.
 
## Model Building
 Word2Vec was used because I wanted the text representations to capture distributional similarities between words. In the context of recipe ingredients, Word2vec allowed me to capture similarities between recipe ingredients that are commonly used together. 

In order to build the recipe recommendation system, **TF-IDF** was used to aggregate embeddings (as opposed to simple averaging) as it gives us better distinguishing power between recipes by favoring unique ingredients.

The recommendation system was built using a **content-based filtering** approach which enables us to recommend recipes to people based on the ingredients the user provides. To measure the similarity between user-given ingredients and recipes **cosine similarity** was used. Spacy and KNN were also trialed but cosine similarity won in terms of performance (it was also the most simple approach). The recommendation model computes the cosine similarity between the inputted ingredient list and all recipes in the corpus. It then outputs the top-N most similar recipes, along with their ingredients and URLs, for the user to choose from.


<p align="center">
<img src="./input/streamlit-app.png" width="800" height="444">
</p>
