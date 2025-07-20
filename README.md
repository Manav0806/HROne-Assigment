# HROne Backend Assignment - FastAPI and MongoDB

This repository contains a backend application developed using FastAPI and MongoDB for the HROne Backend Intern Hiring Task. The application simulates a basic e-commerce platform with features for managing products and orders. It is built with modularity, clarity, and ease of extension in mind.

---

## Features

- Developed with FastAPI, a high-performance Python web framework.
- MongoDB database integration using `pymongo`.
- CRUD operations for managing products with support for multiple sizes and quantities.
- Order placement functionality including size-based quantity tracking.
- RESTful API with auto-generated interactive Swagger UI documentation.
- Structured modular codebase with clear separation of concerns.
- Environment variable configuration using `.env` and `python-dotenv`.

---

## Folder Structure

HROne-Assigment/
│
├── app/
│ ├── main.py # FastAPI app entry point
│ ├── database.py # MongoDB client setup
│ ├── models.py # Pydantic models for request and response validation
│ ├── products.py # Routes and logic for product endpoints
│ ├── orders.py # Routes and logic for order endpoints
│ └── utils.py # Helper functions for operations like quantity validation
│
├── .env # Environment variables (not included in version control)
├── .gitignore # Git ignore rules
├── requirements.txt # List of Python dependencies
└── README.md # Project documentation


---

## Installation and Setup

### 1. Clone the repository

git clone https://github.com/Manav0806/HROne-Assigment.git
cd HROne-Assigment



### 2. Create and activate a virtual environment (Windows)

python -m venv venv
venv\Scripts\activate


### 3. Install required Python packages

pip install -r requirements.txt

css
Copy
Edit


### 4. Create a `.env` file

Add your MongoDB connection URI to a file named `.env` in the root directory.

Example `.env` content:

MONGO_URI=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/?retryWrites=true&w=majority


Replace `<username>`, `<password>`, and `<cluster>` with your actual MongoDB Atlas credentials.

### 5. Run the FastAPI application

uvicorn app.main:app --reload


The application will be available at `http://127.0.0.1:8000`.

---

## API Documentation

FastAPI provides automatic interactive documentation using Swagger UI. You can access it at:

http://127.0.0.1:8000/docs


---

## API Overview

### Product Endpoints

#### POST /products

Create a new product with multiple sizes and stock.

Request body example:


{
  "name": "HROne T-Shirt",
  "price": 399.99,
  "sizes": [
  { "size": "M", "quantity": 10 },
    { "size": "L", "quantity": 5 }
  ]
}
GET /products
Retrieve all products. You can optionally filter by name or size.

Order Endpoints
POST /orders
Place an order. The API will validate quantity and update the product stock.

Request body example:

{
  "userId": "user123",
  "items": [
    {
      "productId": "64cfd70c3a402d939d1001cc",
      "size": "M",
      "quantity": 2
    }
  ]
}

GET /orders/{userId}
Retrieve all orders placed by a specific user.

MongoDB Structure
Database Name: hrone

Collections:

products: Stores product documents with multiple sizes.

orders: Stores order documents with references to products and size/quantity.

You can verify this using MongoDB Compass or CLI:
use hrone
show collections

Requirements
Dependencies used in the project are listed in requirements.txt. To install them:

pip install -r requirements.txt

Notes
The application uses environment variables for secure configuration. Do not hard-code secrets in the source code.

Data is stored in MongoDB Atlas and can be accessed using MongoDB Compass or CLI.

The API ensures that product stock is checked before placing orders.

Author
Manav Gupta
GitHub: https://github.com/Manav0806
Email: trensorflow08@gmail.com

License
This project is developed as part of the HROne Backend Intern Hiring Task and is not intended for commercial use. It may be reused or extended for educational and demonstration purposes.


---

Let me know if you also want:

- A `.env.example` file  
- Setup for deployment (Render, Heroku, etc.)  
- Postman collection for testing APIs

