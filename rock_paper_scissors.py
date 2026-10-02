import tkinter as tk
import random

user_score = 0
computer_score = 0
round_number = 1

choices = ["Rock", "Paper", "Scissors"]

window = tk.Tk()

window.title("Rock Paper Scissors")
window.geometry("600x650")
window.resizable(False, False)

window.configure(bg="#1e1e2f")


def play_game(user_choice):

    global user_score
    global computer_score
    global round_number

    computer_choice = random.randint(0, 2)

    user_name = choices[user_choice]
    computer_name = choices[computer_choice]

    user_choice_label.config(
        text=f"You chose: {user_name}"
    )

    computer_choice_label.config(
        text=f"Computer chose: {computer_name}"
    )

    if user_choice == computer_choice:

        result_label.config(
            text="🤝 DRAW!",
            fg="#FFD166"
        )

    elif (
        (user_choice == 0 and computer_choice == 2) or
        (user_choice == 1 and computer_choice == 0) or
        (user_choice == 2 and computer_choice == 1)
    ):

        user_score += 1

        result_label.config(
            text="🎉 YOU WIN!",
            fg="#06D6A0"
        )

    else:

        computer_score += 1

        result_label.config(
            text="💻 COMPUTER WINS!",
            fg="#EF476F"
        )

    score_label.config(
        text=f"You: {user_score}     Computer: {computer_score}"
    )

    if round_number < 3:

        round_number += 1

        round_label.config(
            text=f"Round {round_number} / 3"
        )

    else:

        show_final_result()


def show_final_result():

    rock_button.config(state="disabled")
    paper_button.config(state="disabled")
    scissors_button.config(state="disabled")

    if user_score > computer_score:

        final_result = "🏆 YOU WON THE GAME!"

    elif computer_score > user_score:

        final_result = "💻 COMPUTER WON THE GAME!"

    else:

        final_result = "🤝 THE GAME IS A DRAW!"

    result_label.config(
        text=final_result,
        fg="#FFFFFF"
    )

    round_label.config(
        text="GAME OVER"
    )


def restart_game():

    global user_score
    global computer_score
    global round_number

    # Reset variables
    user_score = 0
    computer_score = 0
    round_number = 1

    # Reset labels
    round_label.config(
        text="Round 1 / 3"
    )

    score_label.config(
        text="You: 0     Computer: 0"
    )

    user_choice_label.config(
        text="Your choice will appear here"
    )

    computer_choice_label.config(
        text="Computer's choice will appear here"
    )

    result_label.config(
        text="Choose Rock, Paper or Scissors",
        fg="#FFFFFF"
    )

    # Enable buttons
    rock_button.config(state="normal")
    paper_button.config(state="normal")
    scissors_button.config(state="normal")

title_label = tk.Label(
    window,
    text="ROCK PAPER SCISSORS",
    font=("Arial", 28, "bold"),
    bg="#1e1e2f",
    fg="#FFFFFF"
)

title_label.pack(pady=30)

round_label = tk.Label(
    window,
    text="Round 1 / 3",
    font=("Arial", 18, "bold"),
    bg="#1e1e2f",
    fg="#FFD166"
)

round_label.pack(pady=10)

score_label = tk.Label(
    window,
    text="You: 0     Computer: 0",
    font=("Arial", 18, "bold"),
    bg="#1e1e2f",
    fg="#FFFFFF"
)

score_label.pack(pady=15)

instruction_label = tk.Label(
    window,
    text="Choose your option",
    font=("Arial", 16),
    bg="#1e1e2f",
    fg="#CCCCCC"
)

instruction_label.pack(pady=10)

button_frame = tk.Frame(
    window,
    bg="#1e1e2f"
)

button_frame.pack(pady=20)

rock_button = tk.Button(
    button_frame,
    text="🪨\nROCK",
    font=("Arial", 14, "bold"),
    width=10,
    height=3,
    command=lambda: play_game(0)
)

rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(
    button_frame,
    text="📄\nPAPER",
    font=("Arial", 14, "bold"),
    width=10,
    height=3,
    command=lambda: play_game(1)
)

paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(
    button_frame,
    text="✂️\nSCISSORS",
    font=("Arial", 14, "bold"),
    width=10,
    height=3,
    command=lambda: play_game(2)
)

scissors_button.grid(row=0, column=2, padx=10)

user_choice_label = tk.Label(
    window,
    text="Your choice will appear here",
    font=("Arial", 14),
    bg="#1e1e2f",
    fg="#FFFFFF"
)

user_choice_label.pack(pady=10)

computer_choice_label = tk.Label(
    window,
    text="Computer's choice will appear here",
    font=("Arial", 14),
    bg="#1e1e2f",
    fg="#FFFFFF"
)

computer_choice_label.pack(pady=5)

result_label = tk.Label(
    window,
    text="Choose Rock, Paper or Scissors",
    font=("Arial", 20, "bold"),
    bg="#1e1e2f",
    fg="#FFFFFF"
)

result_label.pack(pady=20)

restart_button = tk.Button(
    window,
    text="PLAY AGAIN",
    font=("Arial", 14, "bold"),
    width=15,
    height=2,
    command=restart_game
)

restart_button.pack(pady=15)

window.mainloop()
