import openai

# Make sure to set your OpenAI API key as an environment variable
# import os
# os.environ["OPENAI_API_KEY"] = "your-api-key"

def process_user_query(user_query):
    # Define the prompt for splitting questions and identifying entities
    prompt = (
        "You are a helpful assistant. Given the following user query, "
        "please identify and split it into individual questions and extract entities.\n\n"
        f"User Query: \"{user_query}\"\n\n"
        "List the questions separately, each on a new line, and extract entities such as names, places, or organizations in a structured format."
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
        entities = {}
        
        for line in lines:
            if line.startswith("Question"):
                questions.append(line)
            elif ":" in line:
                key, value = line.split(":", 1)
                entities[key.strip()] = value.strip()
        
        return questions, entities
    
    except Exception as e:
        print(f"Error: {e}")
        return [], {}

# Example usage
user_query = "What is the weather today in New York? Can you recommend a good restaurant nearby? How do I get there to the Statue of Liberty?"
questions, entities = process_user_query(user_query)

print("Questions:")
for i, question in enumerate(questions, 1):
    print(f"Question {i}: {question}")

print("\nEntities:")
for key, value in entities.items():
    print(f"{key}: {value}")
