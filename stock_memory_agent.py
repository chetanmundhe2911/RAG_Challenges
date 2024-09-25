from langchain import LLMChain, OpenAI
from langchain.prompts import PromptTemplate

# Initialize the stock memory
stock_memory = StockMemory()

# Set up the LLM
llm = OpenAI(model_name="gpt-3.5-turbo")

# Define a prompt template for stock queries
prompt_template = PromptTemplate(
    input_variables=["last_stock_id", "user_input"],
    template="You are a helpful stock assistant. The last stock ID asked was: {last_stock_id}. "
             "The user has asked: {user_input}. How would you respond?"
)

# Create the stock agent
def ask_stock_agent(user_input):
    # Check if the user input is a stock ID
    stock_id = user_input.strip()  # Assume the user input is the stock ID for simplicity
    stock_memory.update_stock_id(stock_id)
    
    # Prepare the prompt
    last_stock_id = stock_memory.get_last_stock_id()
    prompt = prompt_template.format(last_stock_id=last_stock_id, user_input=user_input)
    
    # Get the response from the LLM
    response = llm(prompt)
    return response

# Example usage
if __name__ == "__main__":
    while True:
        user_question = input("You: ")
        if user_question.lower() in ["exit", "quit"]:
            break
        response = ask_stock_agent(user_question)
        print(f"Stock Agent: {response}")
