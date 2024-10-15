from groq import Groq
import pyttsx3
import description

class Jarvis:
    def __init__(self, api_key):
        # Initialize the Groq client with the API key
        self.api_key = api_key
        self.client = Groq(api_key=self.api_key)
        
        # Initialize the text-to-speech engine
        self.engine = pyttsx3.init()
        
        # Initialize an empty list to store conversation messages
        self.messages = []

    def add_message(self, role, content):
        # Add a new message to the conversation history
        self.messages.append({"role": role, "content": content})

    def synthesize_speech(self, text):
        # Convert text to speech using pyttsx3
        self.engine.say(text)
        self.engine.runAndWait()

    def get_response(self):
        try:
            # Send a request to the AI model for a response
            chat_completion = self.client.chat.completions.create(
                messages=self.messages,
                model="Llama-3.1-70b-Versatile",
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            # Handle any errors that occur during the request
            print(f"Error: {str(e)}")
            return None

    def respond_to_user(self, user_input):
        # Add the user's input to the conversation history
        self.add_message("user", user_input.strip())
        
        # Get the AI's response
        response = self.get_response()
        
        if response:
            # Add the AI's response to the conversation history
            self.add_message("assistant", response)
            
            # Print the AI's response
            print("Jarvis:", response)
            
            # Convert the AI's response to speech
            self.synthesize_speech(response)

def main():
    # Initialize the Jarvis instance with the API key
    api_key = "Your API Key"
    jarvis = Jarvis(api_key)

    # Inform the user that the program is listening
    print("I'm listening.")

    while True:
        # Prompt the user for input
        user_input = input("User: ").strip()
        
        # Have Jarvis respond to the user's input
        jarvis.respond_to_user(user_input)

        # Check if the user wants to exit the conversation
        if user_input.lower() == "go to sleep":
            # Add the exit message to the conversation history
            jarvis.add_message("user", user_input)
            
            # Get the AI's response
            response = jarvis.get_response()
            
            if response:
                # Add the AI's response to the conversation history
                jarvis.add_message("assistant", response)
                
                # Print and speak the AI's response
                print("Jarvis:", response)
                jarvis.synthesize_speech(response)
            
            # Exit the loop since the user wants to go to sleep
            break

if __name__ == "__main__":
    main()
1
