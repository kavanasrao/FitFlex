# 💪 FitFlex – Backend API for Fitness Class Booking

**FitFlex** is a backend system for a fitness class booking application. It is built with **Python**, **Flask**, and **SQLite**, and uses **JWT authentication** for secure access.

---

## 🛠 Tech Stack

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-JWT-Extended
- SQLite (database)
- Flask-Migrate (for migrations)
- Python-dotenv (for environment variables)

---

## 📁 Project Structure
```bash
FitFlex/
├── app/
│ ├── init.py
│ ├── models/
│ ├── routes/
├── migrations/
├── myenv/ # virtual environment (in .gitignore)
├── .env
├── .gitignore
├──  seed.py
├── config.py
├── requirements.txt
├── run.py
└── README.md
```


---

## 🔐 Features

- User Registration and Login
- Password Hashing using Werkzeug
- JWT Authentication
- View Available Fitness Classes
- Book Classes
- View Bookings by Email
- Environment-based Configuration

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/kavanasrao/FitFlex.git
cd FitFlex
```
### 2. Create and activate virtual environment

### 3. Install dependencies
```bash 
pip install -r requirements.txt
```
### 4. Set environment variables

### 5. Run migrations
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 6. run the app 
```bash
flask run
```
---

## 🧪 Sample API Endpoints

| Method | Endpoint            | Description                |
| ------ | ------------------- | -------------------------- |
| POST   | `/register`         | Register a new user        |
| POST   | `/login`            | Login and get JWT token    |
| GET    | `/classes`          | View all available classes |
| POST   | `/book`             | Book a fitness class       |


## ✅ API Testing with Postman

All API endpoints have been tested successfully using Postman.

🔗 **Postman Collection (Public Link):**  
[FitFlex API - Collection](https://elements.getpostman.com/redirect?entityId=45575642-9535898b-a51f-4150-bcb7-98040da76c15&entityType=collection)


📄 Includes test cases for:
- ✅ Register Users
- ✅ Login and Get JWT Token
- ✅ List Fitness Classes (with time filters)
- ✅ Book Class (with Auth)
- ✅ View Bookings by Email (with Auth)
- ❌ Error Handling (missing fields, wrong IDs, full class, etc.)

🧪 All tests are passed and confirmed working.


## 🚀 Final Notes

This project was inspired by a technical assessment for a Python Developer role.

It showcases:

🔹 Modular Flask application structure

🔹 JWT-based Authentication and Authorization

🔹 SQLite database integration

🔹 Fitness class booking logic with time-based filtering

🔹 Proper error handling and validation

All core functionalities have been tested using Postman and curl, and the test cases (with results) are included in this repository.

## 🙋‍♀️ Author

Kavana

(https://kavanasrao.github.io/)


Thanks for visiting this project! Feel free to connect or leave feedback.

