import tkinter as tk
import random
from tkinter import messagebox

class NumberGuessingGameGUI:
    def __init__(self, root, max_number=100):
        self.root = root
        self.root.title("Number Guessing Game")
        self.max_number = max_number
        self.secret_number = random.randint(1, self.max_number)
        self.attempts = 0

        # Heading Label
        self.label = tk.Label(root, text=f"Guess a number between 1 and {self.max_number}",
                              font=("Arial", 14))
        self.label.pack(pady=10)

        # Entry Box
        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=5)

        # Submit Button
        self.button = tk.Button(root, text="Submit Guess", command=self.check_guess,
                                font=("Arial", 12), bg="lightblue")
        self.button.pack(pady=5)

        # Feedback Label
        self.feedback = tk.Label(root, text="", font=("Arial", 12))
        self.feedback.pack(pady=10)

        # Restart Button
        self.restart_button = tk.Button(root, text="Restart Game", command=self.restart_game,
                                        font=("Arial", 12), bg="lightgreen")
        self.restart_button.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            if 1 <= guess <= self.max_number:
                self.attempts += 1
                if guess < self.secret_number:
                    self.feedback.config(text="Too low! Try again.", fg="red")
                elif guess > self.secret_number:
                    self.feedback.config(text="Too high! Try again.", fg="red")
                else:
                    messagebox.showinfo("Congratulations!",
                                        f"You guessed the number {self.secret_number} in {self.attempts} attempts!")
                    self.restart_game()
            else:
                self.feedback.config(text=f"Enter number between 1 and {self.max_number}", fg="orange")
        except ValueError:
            self.feedback.config(text="Invalid input! Please enter a number.", fg="orange")

    def restart_game(self):
        self.secret_number = random.randint(1, self.max_number)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.feedback.config(text="New game started! Guess again.", fg="blue")


if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGameGUI(root)
    root.mainloop()
