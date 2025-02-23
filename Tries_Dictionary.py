
class DictionaryApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Dictionary with Autocomplete")
        
        self.trie = Trie()
        
        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        """Create the GUI components."""
        # Entry for word input
        self.word_var = StringVar()
        self.entry = tk.Entry(self.root, textvariable=self.word_var)
        self.entry.pack(pady=10)
        self.entry.bind("<KeyRelease>", self.on_key_release)  # Corrected line

        # Listbox to display suggestions
        self.suggestion_listbox = Listbox(self.root)
        self.suggestion_listbox.pack(pady=10)

        # Buttons for dictionary operations
        self.add_button = tk.Button(self.root, text="Add Word", command=self.add_word)
        self.add_button.pack(pady=5)

        self.check_button = tk.Button(self.root, text="Check Word", command=self.check_word)
        self.check_button.pack(pady=5)

        self.remove_button = tk.Button(self.root, text="Remove Word", command=self.remove_word)
        self.remove_button.pack(pady=5)
=======
# GUI buttons implementation
def on_key_release(self, event):
        """Handle key release event to update suggestions."""
        prefix = self.word_var.get()
        suggestions = self.trie.suggest(prefix)
        
        # Clear the current suggestions
        self.suggestion_listbox.delete(0, tk.END)
        
        # Insert new suggestions
        for suggestion in suggestions:
            self.suggestion_listbox.insert(tk.END, suggestion)

    def add_word(self):
        """Add a word to the Trie."""
        word = self.word_var.get().strip()
        if word:
            self.trie.insert(word)
            messagebox.showinfo("Success", f"'{word}' has been added to the dictionary.")
        else:
            messagebox.showwarning("Input Error", "Please enter a word to add.")

    def check_word(self):
        """Check if a word exists in the Trie."""
        word = self.word_var.get().strip()
        if word:
            exists = self.trie.search(word)
            if exists:
                messagebox.showinfo("Check Word", f"'{word}' exists in the dictionary.")
            else:
                messagebox.showinfo("Check Word", f"'{word}' does not exist in the dictionary.")
        else:
            messagebox.showwarning("Input Error", "Please enter a word to check.")

    def remove_word(self):
        """Remove a word from the Trie."""
        word = self.word_var.get().strip()
        if word:
            self.trie.remove(word)
            messagebox.showinfo("Success", f"'{word}' has been removed from the dictionary.")
        else:
            messagebox.showwarning("Input Error", "Please enter a word to remove.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DictionaryApp(root)
    root.mainloop()
