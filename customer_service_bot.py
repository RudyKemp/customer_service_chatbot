from transformers import pipeline, set_seed

def create_chatbot():
    # Initialize a text generation pipeline with a pre-trained model
    chatbot = pipeline('text-generation', model='gpt2')
    set_seed(42)
    return chatbot

def get_response(chatbot, prompt):
    # Generate a response from the chatbot
    responses = chatbot(prompt, max_length=50, num_return_sequences=1)
    return responses[0]['generated_text']

if __name__ == "__main__":
    chatbot = create_chatbot()
    print("Customer Service Bot Initialized. How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Thank you for visiting. Goodbye!")
            break
        response = get_response(chatbot, user_input)
        print("Chatbot:", response)
