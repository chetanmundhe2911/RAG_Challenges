import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Download NLTK stopwords
nltk.download('stopwords')
from nltk.corpus import stopwords

# Function to rank keywords in a user query
def rank_keywords(query, additional_documents=None):
    # Define stop words
    stop_words = set(stopwords.words('english'))

    # Preprocess the query
    query = ' '.join([word for word in query.lower().split() if word not in stop_words])
    
    # If additional documents are provided, include them for context
    if additional_documents is None:
        additional_documents = []

    # Add the user query to the document list
    documents = additional_documents + [query]

    # Create TF-IDF Vectorizer
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    # Get the feature names (keywords)
    feature_names = vectorizer.get_feature_names_out()

    # Get the query vector (last row of the matrix)
    query_vector = tfidf_matrix[-1]

    # Create a dictionary to hold keywords and their scores
    keyword_scores = {}
    for col in range(query_vector.shape[1]):
        keyword_scores[feature_names[col]] = query_vector[0, col]

    # Sort keywords by their scores in descending order
    ranked_keywords = sorted(keyword_scores.items(), key=lambda item: item[1], reverse=True)

    return ranked_keywords

# Example usage
user_query = "How to improve machine learning models"
additional_docs = [
    "Machine learning is a method of data analysis.",
    "Improving models involves tuning parameters."
]

ranked_keywords = rank_keywords(user_query, additional_docs)
print(ranked_keywords)
