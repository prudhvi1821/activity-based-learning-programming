positive = ["good", "excellent", "helpful", "amazing", "nice"]
negative = ["bad", "poor", "boring", "worst", "difficult"]
n = int(input("Enter number of feedback sentences: "))
for i in range(n):
    feedback = input("Enter feedback: ").lower()
    pos = sum(word in feedback for word in positive)
    neg = sum(word in feedback for word in negative)
    score = pos - neg
    result = "Positive" if score > 0 else "Negative" if score < 0 else "Neutral"
    print("Positive:", pos, "Negative:", neg, "Score:", score)
    print("Feedback Classification:", result)