# 🏋️ FitPlanHub

FitPlanHub is a full-stack fitness web application where trainers create fitness plans and users can explore, follow trainers, and subscribe to plans.Trainers can create workout plans, and users can explore trainers, follow them, and subscribe to plans to access detailed fitness guidance.
This project focuses on clean functionality, role-based access, and a user-friendly interface.

---

## 🔧 Project Setup

### Prerequisites
- Python 3.x
- MySQL
- Git

---

### 1️⃣ Clone the Repository
```
git clone https://github.com/your-username/FitPlanHub.git
cd FitPlanHub
```
2️⃣ Create and Activate Virtual Environment
```
python -m venv venv
```
Windows
```
venv\Scripts\activate
```
Mac/Linux
```
source venv/bin/activate
```
3️⃣ Install Dependencies
```
pip install flask flask-login mysql-connector-python
```
4️⃣ Database Setup (MySQL)
Create the database in SQL:
```
CREATE DATABASE fitplanhub;
```
Update database credentials in app.py:
```
host="localhost"
user="your_mysql_username"
password="your_mysql_password"
database="fitplanhub"
```
5️⃣ Run the Application
```
python app.py
```
Open in browser:
```
http://127.0.0.1:5000/
```
# ✨ Features Implemented

## Database Design
Tables used in the project:
- `users`
- `fitness_plans`
- `subscriptions`
- `follows`

Each table is designed to represent real-world relationships between users, trainers, and fitness plans.

## API / Routes Overview

- `/signup` – Register user or trainer
- `/login` – User login
- `/logout` – Logout
- `/trainer/create` – Create fitness plan
- `/plan/<id>` – View plan details
- `/subscribe/<id>` – Subscribe to plan
- `/follow/<trainer_id>` – Follow trainer
- `/feed` – View followed trainers' plans

## 👤 User
- Signup and login
- Browse fitness plans
- Follow and unfollow trainers
- Subscribe to fitness plans

## 🏋️ Trainer
- Create fitness plans
- Manage plans via dashboard

## 🔒 System
- Role-based authentication
- Restricted access to subscribed content

# 🛠️ Tech Stack
- Frontend: HTML, CSS
- Backend: Flask (Python)
- Database: MySQL
- Authentication: Flask-Login

# 🚀 Future Enhancements
- Payment gateway integration
- Workout progress tracking
- Plan ratings and reviews

