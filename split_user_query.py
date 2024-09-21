import openai

# Make sure to set your OpenAI API key as an environment variable
# import os
# os.environ["OPENAI_API_KEY"] = "your-api-key"

def split_questions(user_query):
    # Define the prompt to instruct the model
    prompt = (
        "You are a helpful assistant. Given the following user query, "
        "please identify and split it into individual questions:\n\n"
        f"User Query: \"{user_query}\"\n\n"
        "List the questions separately, each on a new line."
    )
    
    try:
        # Call the OpenAI API with the prompt
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-3.5-turbo-1106" for a mini model
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100,  # Adjust token limit as needed
            temperature=0.0,  # Lower temperature for more deterministic output
        )
        
        # Extract the assistant's response
        questions = response['choices'][0]['message']['content']
        return questions.strip().split('\n')
    
    except Exception as e:
        print(f"Error: {e}")
        return []

# Example usage
user_query = "What is the weather today? Can you recommend a good restaurant nearby? How do I get there?"
questions = split_questions(user_query)
for i, question in enumerate(questions, 1):
    print(f"Question {i}: {question}")
