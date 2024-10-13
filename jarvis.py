from groq import Groq
import pyttsx3
import time
import description

# Bringing up the API key from GROQ
api_key = "Fill in your API Key"
client = Groq(api_key=api_key)

engine = pyttsx3.init()

# Printing to let the user know that the code is running
print("I'm listening.")

# Initialize conversation messages with system behavior

messages = [
    {
        "role": "system",
        "content": description.model, # A file where I tell the AI how to behave
    }
]


# If I want to make the AI speak I can use this function
def synthesize_speech(text):
    engine.say(text)
    engine.runAndWait()


# Start the conversation loop
while True:
    # Asking for user to say something
    user_input = input("User: ").strip()

    # Exit condition: if the user says "go to sleep"
    if user_input.lower() == "go to sleep":
        messages.append({
            "role": "user",
            "content": user_input,
        })
        
        # Try to get the AI's response
        try:
            # Make a request to the AI model for a response
            chat_completion = client.chat.completions.create(
                messages=messages,
                model="llama3.1-70b-8192",  # Assuming llama3 model with 70B parameters
            )

            # Extract the AI's response
            response = chat_completion.choices[0].message.content

            # Add AI response to the conversation history
            messages.append({
                "role": "assistant",
                "content": response,
            })

            # Print the AI's response and synthesize speech
            print("Jarvis:", response)
            synthesize_speech(response)

            # Stopping the conversation because the user said go to sleep
            break

        except Exception as e:
            # Handle any errors and print them out
            print(f"Error: {str(e)}")
                
                

            
        
        except Exception as e:
            print(f"Error: {str(e)}")
    
    messages.append({
        "role": "user",
        "content": user_input,
    })

    try:
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="llama3-70b-8192",
        )
        response = chat_completion.choices[0].message.content

        messages.append({
            "role": "assistant",
            "content": response,
        })

        print("Jarvis:", response)
        synthesize_speech(response)
        
        

    except Exception as e:
        print(f"Error: {str(e)}")
