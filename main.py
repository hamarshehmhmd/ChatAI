import random

# Generate a list of random questions
questions = [
    "What is your favorite color?",
    "What is your favorite food?",
    "What is your favorite hobby?",
    "What is your favorite movie?",
    "What is your favorite book?",
]

# Ask the user for their name
name = input("What is your name? ")

# Create an empty list to store the user's responses
responses = []

# Ask the user each question and store their response
for question in questions:
    response = input(f"{question} ")
    responses.append(response)

# Save the user's responses to a file with their name
with open(f"{name}.txt", "w") as f:
    for response in responses:
        f.write(response + "\n")

print("Thank you for answering the questions! Your responses have been saved to a file.")
