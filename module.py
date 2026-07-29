import pyjokes
joke = pyjokes.get_joke()
print(joke)
 
import pyttsx3
engine = pyttsx3.init()
engine.say("hi my name is ChatGPT, I am a language model developed by OpenAI. I can help you with various tasks and answer your questions.")
engine.runAndWait()

