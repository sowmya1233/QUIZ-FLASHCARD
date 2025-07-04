import json
import random

def load_flashcards():
    with open('flashcards.json', 'r') as f:
        return json.load(f)

def quiz_user(flashcards):
    import random
    score = 0
    for card in random.sample(flashcards, len(flashcards)):
        user_ans = input(f"{card['question']} → ").strip().lower()
        if user_ans == card['answer'].strip().lower():
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Incorrect. Answer: {card['answer']}\n")
    print(f"🎯 You scored {score}/{len(flashcards)} correct.")


if __name__ == "__main__":
    cards = load_flashcards()
    quiz_user(cards)
