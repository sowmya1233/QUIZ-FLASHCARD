import json
import random

def load_flashcards():
    with open('flashcards.json', 'r') as f:
        return json.load(f)

def quiz_user(flashcards):
    for card in random.sample(flashcards, len(flashcards)):
        user_ans = input(f"{card['question']} → ").strip().lower()
        if user_ans == card['answer'].strip().lower():
            print("✅ Correct!\n")
        else:
            print(f"❌ Incorrect. Answer: {card['answer']}\n")

if __name__ == "__main__":
    cards = load_flashcards()
    quiz_user(cards)
