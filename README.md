# Sports Shop Customer Support Chatbot

This repository contains a simple Customer Support Chatbot built using basic AI techniques in Python. The chatbot is designed to assist customers of a sports shop with their queries, such as store information, product availability, discounts, delivery details, and more. This project uses a CSV file for storing FAQs and their corresponding responses, which is processed using Python and NLP libraries.

## Table of Contents
- Features
- Requirements
- Installation
- Usage
- Project-structure
- Data Format
- How It Works
- Future Enhancements
- License]

## Features
- Automates customer support for a sports shop with predefined questions and answers.
- Uses a CSV file to store customer queries and responses.
- Handles basic product inquiries, store hours, delivery, return policies, and more.
- Easily extendable with more data and questions.

## Requirements
Before running the project, ensure you have the following installed:

- Python 3.x
- [Google Colab](https://colab.research.google.com/) (or local Jupyter environment)
- Required Python libraries:
  - `pandas`
  - `nltk`

You can install the required libraries using:
```bash
pip install pandas nltk
```

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/sports-shop-chatbot.git
   cd sports-shop-chatbot
   ```

2. **Upload the CSV file**: In Google Colab or your local Jupyter environment, upload the CSV file containing the FAQs (`sports_shop_chatbot_data.csv`).

3. **Install necessary libraries**:
   ```bash
   !pip install pandas nltk
   ```

4. **Run the chatbot script** in your environment.

## Usage
1. **Load the CSV data**: The CSV file (`sports_shop_chatbot_data.csv`) is loaded into the Colab notebook, and it contains the pre-defined questions and answers for the chatbot.
   
2. **Start Chatting**: Once the notebook is run, you can start interacting with the chatbot. The chatbot matches user queries with questions from the CSV file and returns the appropriate answer.

   Example interaction:
   ```
   You: What are your working hours?
   Chatbot: We are open from Monday to Saturday, 9 AM to 7 PM, and on Sundays from 11 AM to 5 PM.
   ```

3. **Exit the Chat**: Type `thanks` to end the conversation.

## Project Structure

```bash
├── sports_shop_chatbot_data.csv  # CSV file with FAQs and responses
├── chatbot.ipynb                 # Jupyter/Colab notebook containing the chatbot code
├── README.md                     # Project documentation
```

### CSV File Format

The CSV file contains the following columns:
- **Category**: The category of the query (e.g., Store Info, Delivery, Products).
- **Question**: The customer query that the chatbot will respond to.
- **Alternative Phrasing**: Variations of the query to ensure the chatbot recognizes different ways of asking the same question.
- **Answer**: The predefined response for the given question.
- **Tags**: Keywords related to the query for better intent recognition.

Example CSV data:
```csv
Category,Question,Alternative Phrasing,Answer,Tags
Store Info,What are your working hours?,When are you open?,We are open from Monday to Saturday, 9 AM to 7 PM, and on Sundays from 11 AM to 5 PM.,hours,working,schedule
Delivery,Do you offer home delivery?,Can you deliver to my home?,Yes, we offer home delivery across the country. Free delivery on orders above $50!,delivery,shipping,home
```

## How It Works
1. **Load Data**: The chatbot reads the CSV file and creates a dictionary of questions and answers.
2. **Text Matching**: The chatbot uses simple text matching techniques with tokenization to find the most relevant answer to the customer’s question.
3. **Response Generation**: Once a match is found, the chatbot responds with the predefined answer. If no match is found, it returns a fallback message.

## Future Enhancements
Some ideas for improving the chatbot:
- **Natural Language Processing**: Implement more advanced NLP techniques to improve question matching and intent recognition.
- **Machine Learning**: Use ML models like BERT or GPT for better understanding and responding to queries.
- **Database Integration**: Instead of CSV, use a database to store questions and answers, making it more scalable.
- **Additional Features**: Implement additional features such as live agent handoff, order tracking integration, and personalized recommendations.

## License
This project is NOT licensed and is Free to use.
