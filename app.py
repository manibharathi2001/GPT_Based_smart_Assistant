import openai
from apikey import api_data
import speech_recognition as sr  # Converts my voice commands to text
import pyttsx3  # Read out text output to voice.
import webbrowser

# Set the API key
openai.api_key = api_data

def Reply(question):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {'role': "system", "content": "You are a helpful assistant."},
            {'role': 'user', 'content': question}
        ],
        max_tokens=200
    )
    answer = completion.choices[0].message.content.strip()
    return answer

# Text to speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hello, Mani Bharathi!")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1  # Wait for 1 sec before considering the end of a phrase
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")
    except Exception as e:
        print("Say that again, please...")
        return "None"
    return query

if __name__ == '__main__':
    while True:
        query = takeCommand().lower()
        if query == 'none':
            continue

        # Specific Browser Related Tasks
        if "open youtube" in query:
            webbrowser.open('www.youtube.com')
            speak("Opening YouTube.")
            continue
        elif "open instagram" in query:
            webbrowser.open('www.instagram.com')
            speak("Opening Instagram.")
            continue
        elif "open google" in query:
            webbrowser.open('www.google.com')
            speak("Opening Google.")
            continue
        elif "bye" in query or "exit" in query:
            speak("Goodbye!")
            break

        # Get response from OpenAI
        ans = Reply(query)
        print(ans)
        speak(ans)
