# Online Chatbot Based Ticketing System

## Project Overview

Online Chatbot Based Ticketing System is a small web-based project developed using Python and Flask. The main purpose of this project is to provide a simple way for users to ask common support questions and create support tickets when they need help.

The chatbot uses simple keyword matching instead of a complicated AI model. When a user enters a message, the program checks the message for common words such as `ticket`, `payment`, `login`, `refund`, and `support`, and then displays a suitable response.

The ticket section stores user problems in an SQLite database. Each new ticket gets a unique ticket number and starts with an `Open` status.

## Objectives

- To create a simple online support system.
- To provide basic chatbot assistance.
- To allow users to create support tickets.
- To store ticket information in a database.
- To display all submitted tickets.
- To update ticket status.

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- SQLite

## Main Features

### 1. Chatbot
The chatbot responds to common questions using keyword matching.

### 2. Create Ticket
The user can enter:
- Name
- Email
- Phone
- Category
- Problem description

After submission, a ticket ID is generated.

### 3. Ticket Database
SQLite is used to store the ticket details.

### 4. Ticket Status
A ticket can have:
- Open
- In Progress
- Closed

### 5. Simple Web Interface
HTML and CSS are used to create the user interface.

## Project Structure

```text
online-chatbot-ticketing-system/
│
├── app.py
├── chatbot.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── index.html
│   ├── ticket.html
│   ├── success.html
│   └── tickets.html
│
└── static/
    └── style.css
```

`tickets.db` is automatically created when the application is started, so it does not need to be uploaded to GitHub.

## How to Run

### Step 1: Install Python

Install Python 3 on your computer.

### Step 2: Open the project folder

Open Command Prompt or Terminal inside the project folder.

### Step 3: Create a virtual environment (optional)

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

### Step 4: Install Flask

```bash
pip install -r requirements.txt
```

### Step 5: Run the project

```bash
python app.py
```

### Step 6: Open the website

Open:

```text
http://127.0.0.1:5000
```

## Example Chatbot Questions

Try:

```text
Hi
I want to create a ticket
My payment is not working
I forgot my password
I need a refund
I need support
What is my ticket status?
```

## Database

The project uses SQLite because it is simple and does not require a separate database server.

The `tickets` table contains:

| Field | Description |
|---|---|
| id | Unique ticket number |
| name | User name |
| email | User email |
| phone | User phone |
| category | Problem category |
| issue | Problem description |
| status | Current ticket status |
| created_at | Ticket creation time |

## Working of the Project

1. User opens the website.
2. User can communicate with the chatbot.
3. Chatbot checks the entered message.
4. If the question matches a known keyword, the bot gives a response.
5. If the problem needs support, the user opens the Create Ticket page.
6. User fills the ticket form.
7. Data is inserted into SQLite.
8. A unique ticket ID is displayed.
9. Tickets can be viewed from the View Tickets page.
10. The ticket status can be changed to In Progress or Closed.

## Advantages

- Easy to use.
- Simple interface.
- Saves ticket records.
- Does not require an online database.
- Chatbot works without an external API.
- Suitable for a basic college project.

## Limitations

- The chatbot is rule-based and does not understand every sentence.
- There is no real payment gateway.
- There is no email/SMS notification.
- Authentication is not implemented.
- SQLite is mainly suitable for a small project.

## Future Scope

- Add user login and registration.
- Add an admin login.
- Add email notifications.
- Add real-time ticket updates.
- Add an AI/NLP based chatbot.
- Add ticket search and filtering.
- Add file upload for screenshots.
- Deploy the project online.

## Author

Developed as a student academic project.

## License

This project is intended for educational purposes.
