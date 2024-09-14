import pandas as pd
import openai
from fuzzywuzzy import process, fuzz

def extract_company_names(question, api_key):
    openai.api_key = api_key
    prompt = f"Extract company names from the following question: {question}"
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0
    )
    response_text = response.choices[0].text.strip()
    # Assuming response text is a comma-separated list of names
    return [name.strip() for name in response_text.split(',')]

def match_companies_to_stock_data(question, api_key, excel_file_path, threshold=80):
    # Extract company names from the question
    company_names = extract_company_names(question, api_key)

    # Load the Excel data
    df = pd.read_excel(excel_file_path)

    # Ensure the column names match your Excel file
    if 'Stock Name' not in df.columns or 'Stock ID' not in df.columns:
        raise ValueError("Excel file must contain 'Stock ID' and 'Stock Name' columns")

    # Convert stock names to a list for fuzzy matching
    stock_names = df['Stock Name'].tolist()

    # Initialize a list to hold matches
    matches = []

    for name in company_names:
        # Find the best match for each extracted company name
        best_match, best_score = process.extractOne(name, stock_names, scorer=fuzz.token_sort_ratio)
        if best_score >= threshold:
            matched_row = df[df['Stock Name'] == best_match]
            if not matched_row.empty:
                for _, row in matched_row.iterrows():
                    matches.append({
                        'Company Name': name,
                        'Stock ID': row['Stock ID'],
                        'Stock Name': row['Stock Name'],
                        'Match Score': best_score
                    })

    return matches

# Example usage
if __name__ == "__main__":
    api_key = "your-openai-api-key"  # Replace with your OpenAI API key
    question = "What are the stock details for Google and Microsoft?"
    excel_file_path = "stocks.xlsx"  # Path to your Excel file

    matched_stocks = match_companies_to_stock_data(question, api_key, excel_file_path)
    for match in matched_stocks:
        print(f"Company Name: {match['Company Name']}, Stock ID: {match['Stock ID']}, Stock Name: {match['Stock Name']}, Match Score: {match['Match Score']}")
