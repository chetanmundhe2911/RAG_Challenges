#This function returns the company name from the user question

def extract_company_names(user_input: str, model_name: str) -> List[str]:
    """
    Use OpenAI to extract company names from the user's input.
    """
    messages = [
        {"role": "system", "content": "You are a helpful assistant. Extract only the company names from the user's query, separated by commas. If no company names are found, return an empty string."},
        {"role": "user", "content": user_input}
    ]
    response = openai.ChatCompletion.create(model=model_name, messages=messages)
    company_names = response.choices[0].message['content'].strip()
    return [name.strip() for name in company_names.split(',')] if company_names else []
