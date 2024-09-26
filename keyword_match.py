# Sample list of keywords
keywords = ["python", "data", "machine learning", "artificial intelligence", "programming"]

# Sample text to search for keywords
text = "I love programming in Python and learning about machine learning techniques."

# Function to find matching keywords
def find_matching_keywords(keywords, text):
    # Convert text to lower case to make the search case insensitive
    text_lower = text.lower()
    # Find and return matching keywords
    matches = [keyword for keyword in keywords if keyword.lower() in text_lower]
    return matches

# Using the function to find matches
matched_keywords = find_matching_keywords(keywords, text)

# Output the result
print("Matched Keywords:", matched_keywords)
