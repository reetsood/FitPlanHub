🏋️# FitPlanHub

FitPlanHub is a full-stack fitness web application where trainers can create fitness plans and users can explore, follow trainers, and subscribe to plans to access detailed workout information.

This project was developed as part of a placement assessment to demonstrate backend development, database integration, authentication, and frontend UI design.

🔧# Project Setup
Prerequisites

Make sure you have the following installed:

Python 3.x

MySQL

Git

1️⃣ Clone the Repository
'''bash
git clone https://github.com/reetsood/FitPlanHub.git
cd FitPlanHub

2️⃣ Create and Activate Virtual Environment
python -m venv venv


Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

3️⃣ Install Dependencies
pip install flask flask-login mysql-connector-python

4️⃣ Database Setup (MySQL)

Create a MySQL database:

CREATE DATABASE fitplanhub;


Update database credentials in the Flask app:

host="localhost"
user="your_mysql_username"
password="your_mysql_password"
database="fitplanhub"


Run the SQL tables provided in the project (users, plans, subscriptions, followers).

5️⃣ Run the Application
python app.py


Open your browser and visit:

http://127.0.0.1:5000/

✨ Features Implemented
User Features

User registration and login

Browse fitness plans

Follow and unfollow trainers

Subscribe to fitness plans

View subscribed plans in personal feed

Trainer Features

Trainer registration and login

Create fitness plans

Manage plans through trainer dashboard

System Features

Role-based authentication (User / Trainer)

Restricted access to premium content

Secure login and logout using Flask-Login

🛠️ Technologies Used

Frontend: HTML, CSS

Backend: Python (Flask)

Database: MySQL

Authentication: Flask-Login

Templating: Jinja2

📌 Notes

No frontend frameworks were used.

UI was custom styled using CSS.

Project follows a simple and readable structure.

🚀 Future Enhancements

Payment gateway integration

Workout progress tracking

Plan ratings and reviews

Mobile-responsive design improvements
