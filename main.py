import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Ask user for input
text = input("Enter something for me to say: ")

# Speak the input
engine.say(text)
engine.runAndWait()
