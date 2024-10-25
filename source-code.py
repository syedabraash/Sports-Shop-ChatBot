!pip install pandas
!pip install nltk

import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('/content/sports_shop_chatbot_data.csv')

# View the first few rows of the data
print(df.head())

# Create a dictionary to store questions and answers
qa_dict = {}

# Loop through the DataFrame and populate the dictionary
for index, row in df.iterrows():
    # Combine Question and Alternative Phrasing
    questions = [row['Question']] + row['Alternative Phrasing'].split('|')
    for question in questions:
        qa_dict[question.strip().lower()] = row['Answer']

# Print out the question-answer dictionary
print(qa_dict)

import nltk
from nltk.tokenize import word_tokenize

# Download the 'punkt' resource if it's not already downloaded
nltk.download('punkt')

# Function to find the best match for user input
def get_response(user_input):
    user_input = user_input.lower()
    tokens = word_tokenize(user_input)

    # Match user input with existing questions
    for question in qa_dict.keys():
        if all(token in question for token in tokens):
            return qa_dict[question]
    return "Sorry, I don't understand that. Could you ask another question?"

# Test the chatbot with user input
while True:
    user_input = input("Your Text: ")
    if user_input.lower() == "thanks":
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print(f"Chatbot: {response}")
