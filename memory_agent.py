from langchain import LLMChain, OpenAI
from langchain.prompts import PromptTemplate

# Initialize the memory
memory = Memory()

# Set up the LLM
llm = OpenAI(model_name="gpt-3.5-turbo")

# Define a prompt template
prompt_template = PromptTemplate(
    input_variables=["memory", "user_input"],
    template="You are a helpful assistant. You remember the following questions: {memory}. "
             "The user has asked: {user_input}. How would you respond?"
)

# Create the Langchain agent
def ask_agent(user_input):
    # Add the question to memory
    memory.add_question(user_input)
    
    # Prepare the prompt
    memory_content = ', '.join(memory.get_memory())
    prompt = prompt_template.format(memory=memory_content, user_input=user_input)
    
    # Get the response from the LLM
    response = llm(prompt)
    return response

# Example usage
if __name__ == "__main__":
    while True:
        user_question = input("You: ")
        if user_question.lower() in ["exit", "quit"]:
            break
        response = ask_agent(user_question)
        print(f"Agent: {response}")
