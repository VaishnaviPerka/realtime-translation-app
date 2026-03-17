import csv
import os
from difflib import get_close_matches
import tkinter as tk
from tkinter import messagebox

# List of 100 words
words = [
    "hello", "how", "where", "which", "country", "count", "money", "mountain", "rock", "task",
    "program", "project", "come", "close", "file", "life", "style", "search", "window", "linear",
    "near", "door", "coconut", "table", "book", "date", "series", "world", "vegetable", "fruits",
    "monkey", "key", "helmet", "blood", "hospital", "station", "train", "model", "test",
    "words", "folder", "prepare", "prepone", "post", "aeroplane", "bags", "games", "children",
    "place", "tamarind", "palace", "friends", "fries", "cream", "dream", "charm", "beautiful", "loud",
    "cloud", "mould", "drum", "ugli", "carrot", "berry", "straw", "raw", "match", "empire",
    "empower", "power", "rope", "fine", "define", "determine", "more", "manage", "sun",
    "son", "claim", "offer", "desktop", "user", "correct", "incorrect", "kite", "rite", "right",
    "left", "let"
]

# Define the folder path
folder_path = r"C:\Users\vaish\Desktop\Project\Task2"

# Create the folder if it doesn't exist
os.makedirs(folder_path, exist_ok=True)

# Path to save the CSV file
file_path = os.path.join(folder_path, 'words.csv')

# Function to suggest closest matches
def suggest_word(word, word_list):
    return get_close_matches(word, word_list, n=3)

# Function to check if words are in the list and save to CSV
def save_words_to_csv(words_to_save, all_words, file_path):
    incorrect_words = []
    
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["word"])
        for word in words_to_save:
            if word in all_words:
                writer.writerow([word])
            else:
                incorrect_words.append(word)
                suggestions = suggest_word(word, all_words)
                error_message = f"'{word}' is not available. Suggestions: {', '.join(suggestions)}"
                print(error_message)
                if len(incorrect_words) >= 2:
                    print(f"Incorrect words so far: {', '.join(incorrect_words)}")
    
    if incorrect_words:
        raise ValueError(f"Encountered incorrect words: {', '.join(incorrect_words)}")

# GUI setup
class WordEntryApp:
    def __init__(self, master):
        self.master = master
        master.title("Word Entry App")
        
        self.label = tk.Label(master, text="Enter a word:")
        self.label.pack()
        
        self.entry = tk.Entry(master)
        self.entry.pack()
        
        self.submit_button = tk.Button(master, text="Submit", command=self.submit_word)
        self.submit_button.pack()
        
        self.words_to_save = []
        self.incorrect_words = []
        
    def submit_word(self):
        word = self.entry.get().strip()
        if word:
            if word in words:
                self.words_to_save.append(word)
                messagebox.showinfo("Success", f"'{word}' is available.")
            else:
                self.incorrect_words.append(word)
                suggestions = suggest_word(word, words)
                error_message = f"'{word}' is not available. Suggestions: {', '.join(suggestions)}"
                if len(self.incorrect_words) >= 2:
                    error_message += f"\nIncorrect words so far: {', '.join(self.incorrect_words)}"
                messagebox.showerror("Error", error_message)
            self.entry.delete(0, tk.END)
    
    def save_to_csv(self):
        try:
            save_words_to_csv(self.words_to_save, words, file_path)
            messagebox.showinfo("Success", "Words have been saved to CSV.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

# Main loop
root = tk.Tk()
app = WordEntryApp(root)

# Add save button
save_button = tk.Button(root, text="Save to CSV", command=app.save_to_csv)
save_button.pack()

root.mainloop()
