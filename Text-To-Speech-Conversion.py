import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set the speech rate (words per minute)
engine.setProperty('rate', 150)  # You can adjust the speed

# Set the voice (0 for male, 1 for female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Set to female voice

while True:
    # The text you want to convert to speechy
    text = input("Enter what you want to say (type 'exit' to quit): ")
    
    # Exit condition
    if text.lower() == 'exit':
        print("Exiting...")
        break
    
    # Convert text to speech and play it
    engine.say(text)
    engine.runAndWait()
