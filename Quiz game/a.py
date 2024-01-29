import random

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_welcome_message(self):
        print("Welcome to the Quiz Game!")
        print("Answer multiple-choice or fill-in-the-blank questions to test your knowledge.")

    def display_rules(self):
        print("Rules:")
        print("1. Answer each question to the best of your ability.")
        print("2. For multiple-choice questions, enter the letter corresponding to your answer.")
        print("3. For fill-in-the-blank questions, enter your answer as text.")
        print("4. Each correct answer earns you a point.")
        print("5. Enjoy the quiz!")

    def ask_question(self, question):
        print("\n" + question["text"])

        if question["type"] == "multiple_choice":
            for i, choice in enumerate(question["choices"], start=1):
                print(f"{chr(64 + i)}. {choice}")

            user_answer = input("Your answer: ").upper()
        else:
            user_answer = input("Your answer: ")

        return user_answer

    def evaluate_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("Correct! Well done.")
            self.score += 1
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}")

    def display_final_results(self):
        print("\nQuiz Completed!")
        print(f"Your final score is: {self.score} out of {len(self.questions)}")

    def play_again(self):
        return input("Do you want to play again? (yes/no): ").lower() == "yes"

def main():
    # Sample quiz questions
    quiz_questions = [
        {"text": "What is the capital of France?", "type": "multiple_choice", "choices": ["Paris", "Berlin", "Rome", "Madrid"], "correct_answer": "A"},
        {"text": "Which planet is known as the Red Planet?", "type": "fill_in_the_blank", "correct_answer": "Mars"},
        {"text": "What is the largest mammal on Earth?", "type": "multiple_choice", "choices": ["Elephant", "Blue Whale", "Giraffe", "Penguin"], "correct_answer": "B"}
    ]

    while True:
        game = QuizGame(quiz_questions)
        game.display_welcome_message()
        game.display_rules()

        for question in quiz_questions:
            user_answer = game.ask_question(question)
            correct_answer = question["correct_answer"].upper() if "correct_answer" in question else question["correct_answer"]
            game.evaluate_answer(user_answer, correct_answer)

        game.display_final_results()

        if not game.play_again():
            print("Thank you for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
