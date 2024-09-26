from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Sample list of keywords
keywords = ["python", "data", "machine learning", "artificial intelligence", "programming"]

# Sample text to search for keywords
text = "I love programming in Pyton and learning about machine learning techniques."

# Function to find fuzzy matching keywords
def find_fuzzy_matching_keywords(keywords, text, threshold=80):
    # Split text into individual words for matching
    words = text.split()
    matches = set()
    
    for word in words:
        # Perform fuzzy matching for each word against the keywords
        match, score = process.extractOne(word, keywords, scorer=fuzz.token_set_ratio)
        if score >= threshold:
            matches.add(match)
    
    return list(matches)

# Using the function to find matches with a threshold
matched_keywords = find_fuzzy_matching_keywords(keywords, text, threshold=80)

# Output the result
print("Matched Keywords:", matched_keywords)
