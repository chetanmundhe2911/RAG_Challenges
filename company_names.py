import openai

def extract_company_names(question, api_key):
    # Set up the OpenAI API key
    openai.api_key = api_key

    # Define the prompt for extracting company names
    prompt = f"Extract company names from the following question: {question}"
    
    # Use the OpenAI API to get the completion
    response = openai.Completion.create(
        engine="gpt-4",  # You can choose a different engine if needed
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0
    )

    # Get the text response from the API
    response_text = response.choices[0].text.strip()

    # Return the extracted company names
    return response_text

# Example usage
if __name__ == "__main__":
    api_key = "your-openai-api-key"  # Replace with your OpenAI API key
    question = "What are the latest news from Google and Microsoft?"
    
    company_names = extract_company_names(question, api_key)
    print(f"Extracted Company Names: {company_names}")
