questions = {
    "What is the capital of India?": "Delhi",
    "What is 5 * 6?": "30",
    "Which is the smallest prime number?": "2",
    "Which language is used for AI?": "Python",
    "Who developed the theory of relativity?": "Einstein"
}

score = 0
for q, ans in questions.items():
    user_ans = input(q + "\nAnswer: ").strip()
    if user_ans.lower() == ans.lower():
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer: {ans}\n")

print(f"Your Score: {score}/{len(questions)}")
