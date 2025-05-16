import tkinter as tk
from tkinter import messagebox
import string

class SpellChecker:
    def __init__(self, word_list):
        self.dictionary = set(word_list)

    def suggest(self, word):
        suggestions = set()

        for i in range(len(word)):
            for c in string.ascii_lowercase:
                replaced = word[:i] + c + word[i+1:]
                if replaced in self.dictionary and replaced != word:
                    suggestions.add(replaced)

        for i in range(len(word) + 1):
            for c in string.ascii_lowercase:
                inserted = word[:i] + c + word[i:]
                if inserted in self.dictionary:
                    suggestions.add(inserted)

        for i in range(len(word)):
            deleted = word[:i] + word[i+1:]
            if deleted in self.dictionary:
                suggestions.add(deleted)

        return suggestions

def load_dictionary_from_file(filename="words.txt"):
    with open(filename, 'r') as file:
        return [line.strip().lower() for line in file if line.strip()]

def check_word():
    word = entry.get().lower().strip()
    if word in checker.dictionary:
        messagebox.showinfo("Result", f"✅ '{word}' is correct!")
    else:
        suggestions = checker.suggest(word)
        if suggestions:
            messagebox.showinfo("Suggestions", f"❌ '{word}' not found. Suggestions:\n{', '.join(suggestions)}")
        else:
            messagebox.showinfo("Suggestions", f"❌ '{word}' not found. No suggestions available.")

# GUI setup
dictionary = load_dictionary_from_file()
checker = SpellChecker(dictionary)

root = tk.Tk()
root.title("Divya's Spell Checker")

tk.Label(root, text="Enter a word:").pack(pady=10)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

tk.Button(root, text="Check", command=check_word).pack(pady=10)

root.mainloop()
