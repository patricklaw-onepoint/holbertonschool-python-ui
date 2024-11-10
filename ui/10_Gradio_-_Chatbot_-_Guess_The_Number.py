#!/usr/bin/python3
"""Build a Gradio Chatbot to play “Guess the number”. 
The game can be played by either the user or the
chatbot guessing the number, and the other 
participant confirming if the guess was correct."""
import random
import gradio as gr

# Constants for supported responses
YES_VARIANTS = ["yes", "y"]
NO_VARIANTS = ["no", "n"]
QUIT_VARIANTS = ["quit", "exit"]
STATE = 0
GUESSER = ""
MAX_NUMBER = 0
BOT_GUESS = 0
MESSAGES = {
    "BYE": "Ok, come back later if you want to play Guess the number with me.",
    "ERROR": "I guess we don't understand each other, bye for now.",
}


def reset():
    """Reset game state"""
    global STATE, MAX_NUMBER, GUESSER
    STATE = 0
    GUESSER = ""
    MAX_NUMBER = 0


def chatbot(message, history):
    """Guess The Number"""
    global STATE, MAX_NUMBER, GUESSER, BOT_GUESS
    print(message)
    print(history)

    # Handle quit command
    if message.lower() in QUIT_VARIANTS:
        reset()
        return MESSAGES["BYE"]

    if STATE == -3 or (STATE == -5 and GUESSER == "PLAYER"):
        try:
            max_number = int(message)
            if max_number < 2:
                raise ValueError
            STATE = STATE * -1
        except ValueError:
            reset()
            return MESSAGES["ERROR"]
    elif STATE < 0:
        if message.lower() not in YES_VARIANTS + NO_VARIANTS:
            # Handle unsupported response after game initiation
            reset()
            return MESSAGES["ERROR"]
        STATE = STATE * -1

    if STATE == 0:
        # Initial greeting
        STATE = 1
        return "Hi, do you want to play Guess the number with me?"
    if STATE == 1:
        # Start game
        if message.lower() in YES_VARIANTS:
            STATE = 2
            return "You or I can guess the number, did you want to be the one guessing?"
        if message.lower() in NO_VARIANTS:
            STATE = 0
            return MESSAGES["BYE"]

        STATE = -1
        return (
            "I'm sorry, I didn't understand that. "
            + "Do you want to play Guess the number with me, yes or no?"
        )

    # Game choice logic
    if STATE == 2:
        if message.lower() in YES_VARIANTS:
            STATE = 3
            GUESSER = "PLAYER"
            return "Ok you guess the number. What is the maximum number we will guess up to?"
        if message.lower() in NO_VARIANTS:
            STATE = 3
            GUESSER = "BOT"
            return "Ok I will guess. What is the maximum number we will guess up to?"

        STATE = -2
        return (
            "I'm sorry, I didn't understand that, "
            + "do you want to be the one guessing, yes or no?"
        )

    # Bot guesses logic
    if STATE == 3:
        try:
            MAX_NUMBER = int(message)
            if MAX_NUMBER < 2:
                raise ValueError
            STATE = 4
        except ValueError:
            STATE = -3
            return (
                "I'm sorry I didn't understand that. "
                + "Please let me know a round number greater than 2 I should guess up to."
            )

    if STATE == 4:
        STATE = 5
        BOT_GUESS = random.randint(1, MAX_NUMBER)
        if GUESSER == "BOT":
            return f"I guess {BOT_GUESS}. Is this correct?"
        return "Ok great, what is your guess?"

    if STATE == 5:
        if GUESSER == "BOT":
            if message.lower() in YES_VARIANTS:
                reset()
                STATE = 0
                return "Great! Come back later if you want to play again."
            if message.lower() in NO_VARIANTS:
                reset()
                STATE = 0
                return (
                    "Ahh, hopefully I will have better luck next time! "
                    + "Come back later if you want to play again."
                )
            STATE = -5
            return "I'm sorry, I didn't understand that, did I guess the correct number, yes or no?"

        try:
            if BOT_GUESS == int(message):
                reset()
                STATE = 0
                return "You guessed correct! Come back later if you want to play again."
            reset()
            STATE = 0
            return (
                f"Incorrect, my number was {BOT_GUESS}. "
                + "Better luck next time. Come back later if you want to play again."
            )
        except ValueError:
            STATE = -5
            return (
                "I'm sorry I didn't understand that. "
                + "Please let me know what round number is your guess."
            )


with gr.Blocks(fill_height=True) as app:

    chat = gr.ChatInterface(chatbot, type="messages")
    gr.Button("Reset").click(
        fn=lambda: [[], [], reset()],
        outputs=[chat.chatbot, chat.chatbot_state],
    )


if __name__ == "__main__":
    app.launch()
