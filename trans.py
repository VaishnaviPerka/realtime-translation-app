import speech_recognition as sr
from googletrans import Translator
from datetime import datetime
import pytz
import tkinter as tk
from tkinter import messagebox

# Function to capture audio
def capture_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    return audio

# Function to convert audio to text
def audio_to_text(audio):
    recognizer = sr.Recognizer()
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None

# Function to check the current time
def check_time():
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(ist)
    if current_time.hour >= 18:
        return True
    else:
        return False

# Function to validate text
def validate_text(text):
    words = text.split()
    for word in words:
        if word.startswith('M') or word.startswith('O'):
            return False
    return True

# Function to translate text
def translate_text(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='hi')
    return translated.text

# Main function
def main():
    if not check_time():
        messagebox.showinfo("Info", "Please try after 6 PM IST.")
        return
    
    audio = capture_audio()
    text = audio_to_text(audio)
    
    if text is None:
        messagebox.showinfo("Info", "I didn't catch that. Please repeat.")
        return
    
    if validate_text(text):
        translated_text = translate_text(text)
        messagebox.showinfo("Translated Text", f"Translated text: {translated_text}")
    else:
        messagebox.showinfo("Info", "Text validation failed (either starts with 'M' or 'O').")

# GUI setup
root = tk.Tk()
root.title("English to Hindi Translator")

label = tk.Label(root, text="Press the button to translate your speech from English to Hindi")
label.pack(pady=20)

translate_button = tk.Button(root, text="Translate", command=main)
translate_button.pack(pady=20)

root.mainloop()
