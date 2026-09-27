"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(f"User score {score} is {result}")
    if result == "Excellent":
        print("You get a prize!")
    random_score = random.randint(1, 101)
    print(f"Random: {random_score} = {determine_result(random_score)}")


def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()
