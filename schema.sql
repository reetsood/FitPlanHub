CREATE DATABASE fitplanhub;
USE fitplanhub;

-- USERS TABLE
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(120) UNIQUE,
    password VARCHAR(200),
    role VARCHAR(20)
);

-- FITNESS PLANS
CREATE TABLE fitness_plans (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(150),
    description TEXT,
    price INT,
    duration VARCHAR(50),
    trainer_id INT,
    FOREIGN KEY (trainer_id) REFERENCES users(id)
);

-- SUBSCRIPTIONS
CREATE TABLE subscriptions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    plan_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (plan_id) REFERENCES fitness_plans(id)
);

-- FOLLOW TRAINERS
CREATE TABLE follows (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    trainer_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (trainer_id) REFERENCES users(id)
);
