# Django Python Backend Template

This template provides a structured starting point for developing a backend API using Django for a CRUD application. It includes examples of URL routing, router setup, Mongoose model for MongoDB, controller templates for different databases, and a CSRF-protected CRUD controller for MySQL.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Django URL Routing](#django-url-routing)
  - [Router Template](#router-template-for-python-crud)
  - [Mongoose Model](#mongoose-model-template-for-python-crud)
  - [Controller](#controller-template-for-python-crud)
  - [CRUD Controller (MySQL)](#controller-template-for-python-sql-database)
- [Examples](#examples)
  - [Django URL Patterns](#django-url-patterns)
  - [Router Usage](#router-usage)
  - [Mongoose Model](#mongoose-model-usage)
  - [Controller Usage](#controller-usage)
  - [CRUD Controller (MySQL)](#crud-controller-mysql-usage)

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Django
- MongoDB (for Mongoose model)
- MySQL (for CRUD Controller MySQL)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/johnxiler/Backend-Templates.git
    cd Backend-Templates
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure your database settings in `settings.py` for Django and `CRUDController` class for MySQL.

## Usage

### Django URL Routing

The Django backend uses URL routing to map URLs to views. Check `urls.py` for defined patterns.

### Router Template for Python CRUD

Use the `RouterTemp` class to create a simple router for handling different HTTP methods and paths.

```python
# Example usage
router = RouterTemp()
router.add_route('GET', '/', home)
router.add_route('POST', '/users/', create_user)

Mongoose Model Template for Python CRUD
The ModelMongoose class is a template for MongoDB using Mongoose. Customize it based on your data model.
# Example usage
model = ModelMongoose()
model.insert_one({"name": "John", "age": 30})

Controller Template for Python CRUD
The Controller class demonstrates basic CRUD operations. Adjust it to match your application's logic.
# Example usage
controller = Controller('mypassword')
controller.create('mypassword', {"name": "John", "age": 30})

CRUD Controller (MySQL)
The CRUDController class is designed for MySQL databases and includes protections against SQL injection and XSS attacks.
# Example usage
crud_controller = CRUDController(model, 'localhost', 'user', 'password', 'mydatabase')
crud_controller.create(data, csrf_token)

Examples
Django URL Patterns
/: Home page
/users/: List of users
/users/<int:user_id>/: Details of a specific user
/users/: Create a new user
/users/<int:user_id>/update/: Update a user
/users/<int:user_id>/delete/: Delete a user
Router Usage
Add routes to the RouterTemp instance and handle requests.
router.add_route('GET', '/', home)
result = router.handle_request('GET', '/')

Mongoose Model Usage
model.insert_one({"name": "John", "age": 30})
user = model.find_one({"name": "John"})
print(user)  # {"name": "John", "age": 30}

Controller Usage
controller = Controller('mypassword')
controller.create('mypassword', {"name": "John", "age": 30})
users = list(controller.read('mypassword', {}))
print(users)  # [{"name": "John", "age": 30}]

CRUD Controller (MySQL) Usage
crud_controller = CRUDController(model, 'localhost', 'user', 'password', 'mydatabase')
crud_controller.create(data, csrf_token)

Feel free to modify and expand on this template to suit the specific requirements of your project.

Make sure to replace placeholders like `your_username`, `your_backend_project`, `localhost`, `user`, `password`, `mydatabase`, etc., with your actual project details and configurations.

