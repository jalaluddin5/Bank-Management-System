# Bank Management Website (Flask)

This is a simple bank management web application built with Flask. It supports user registration, login, account management (view balance, deposit, withdraw), and transaction history. The UI uses Bootstrap and data is stored in SQLite.

## Features
- User registration and login (Flask-Login)
- Account overview with balance
- Deposit and withdraw money
- Transaction history
- Bootstrap-based UI

## Getting Started

1. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
2. **Run the app:**
   ```sh
   python app.py
   ```
3. **Open in browser:**
   Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Project Structure
- `app.py` - Main Flask app
- `models.py` - Database models
- `extensions.py` - DB and login manager
- `routes/` - Blueprints for authentication and account
- `templates/` - HTML templates
- `static/` - Static files (CSS, JS, images)

## Notes
- This is a development/demo project. Do not use in production as-is.
- You can further customize features and UI as needed.
