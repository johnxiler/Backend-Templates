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
    git clone https://github.com/your_username/your_backend_project.git
    cd your_backend_project
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
