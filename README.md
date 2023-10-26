# Flashcard App

The Flashcard App is a simple web application built with Flask and SQLAlchemy that allows you to create, manage, and study flashcards. It provides basic functionality for adding, reading, updating, and deleting flashcards, making it a handy tool for learning and reviewing information.

## Features

- Add new flashcards with questions and answers.
- View a list of all your flashcards.
- Update existing flashcards to modify questions and answers.
- Delete flashcards you no longer need.

## Prerequisites

Before you can run the Flashcard App, make sure you have the following dependencies installed:

- Python 3
- Flask
- Flask-SQLAlchemy

You can install Flask and Flask-SQLAlchemy using pip:

```
pip install Flask Flask-SQLAlchemy
```


## Getting Started
1. Clone this repository to your local machine.
```
git clone https://github.com/yourusername/flashcard-app.git
cd flashcard-app
```

2. Create a virtual environment
```
python -m venv venv
source venv/bin/activate
# On Windows, use `venv\Scripts\activate`
```

3. Install the required dependencies.
```
pip install -r requirements.txt
```

4. Initialize the SQLite database.
```
python create_db.py
```

5. Start the Flask application.
```
python app.py
```
The application will be running at http://localhost:5000. You can access it through your web browser or use a tool like Postman to send HTTP requests to the API endpoints.


## API Endpoints

### Add a New Flashcard
- **URL**: /ques
- **Method**: POST
- **Request Body**:
```
{
  "ques": "Your question here",
  "ans": "Your answer here"
}
```

### Read All Flashcards
- **URL**: /ques
- **Method**: GET
- **Response Body**: An array of flashcards, each containing an ID, a question (ques), and an answer (ans).

### Update a Flashcard
- **URL**: /ques/{id}
- **Method**: PUT
- **Request Body**: Include the fields you want to update (e.g., "ques" or "ans").

### Delete a Flashcard
- **URL**: /ques/{id}
- **Method**: DELETE
