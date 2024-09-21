import openai

# Make sure to set your OpenAI API key as an environment variable
# import os
# os.environ["OPENAI_API_KEY"] = "your-api-key"

def process_user_query(user_query):
    # Define the prompt for splitting questions and identifying entities
    prompt = (
        "You are a helpful assistant. Given the following user query, "
        "please identify and split it into individual questions and extract entities such as company names, places, or organizations.\n\n"
        f"User Query: \"{user_query}\"\n\n"
        "List the questions separately, each on a new line, and identify the company names in the user query."
    )
    
    try:
        # Call the OpenAI API with the prompt
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or a different model if necessary
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,  # Adjust token limit as needed
            temperature=0.0,  # Lower temperature for more deterministic output
        )
        
        # Extract the assistant's response
        content = response['choices'][0]['message']['content']
        
        # Split the content into lines for easier processing
        lines = content.strip().split('\n')
        
        # Separate questions and entities from the response
        questions = []
        companies = []
        
        for line in lines:
            if line.startswith("Question"):
                questions.append(line)
            elif "Company Name:" in line:
                companies.append(line.split(":", 1)[1].strip())
        
        return questions, companies
    
    except Exception as e:
        print(f"Error: {e}")
        return [], []

# Example usage
user_query = "What is the latest news about Apple? Can you recommend a good product from Google? How do I contact Microsoft?"
questions, companies = process_user_query(user_query)

print("Questions:")
for i, question in enumerate(questions, 1):
    print(f"Question {i}: {question}")

print("\nCompanies:")
for i, company in enumerate(companies, 1):
    print(f"Company {i}: {company}")
