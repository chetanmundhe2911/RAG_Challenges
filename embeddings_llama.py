import torch
from transformers import LlamaTokenizer, LlamaModel

def create_embeddings(file_path, model_name='facebook/llama-7b'):
    # Load pre-trained model and tokenizer
    tokenizer = LlamaTokenizer.from_pretrained(model_name)
    model = LlamaModel.from_pretrained(model_name)

    # Read text from the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text_data = file.readlines()

    # Generate embeddings
    embeddings = []
    for text in text_data:
        # Tokenize and encode the text
        inputs = tokenizer(text.strip(), return_tensors='pt', padding=True, truncation=True)
        with torch.no_grad():
            outputs = model(**inputs)

        # Get the embeddings (mean of the last hidden states)
        last_hidden_states = outputs.last_hidden_state
        sentence_embedding = torch.mean(last_hidden_states, dim=1).squeeze()
        embeddings.append(sentence_embedding.numpy())

    return embeddings

# Example usage
embeddings = create_embeddings('text.txt')
print(embeddings)
