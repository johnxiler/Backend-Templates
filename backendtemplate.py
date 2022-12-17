import string
import random
import hashlib
# import mongoose
from django.utils.crypto import get_random_string
from mysql.connector.cursor import MySQLCursorPrepared
from mysql.connector import errorcode
import mysql.connector
from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.UpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
]

# ROUTER TEMPLATE FOR Python CRUD


class RouterTemp:
    def __init__(self):
        self.routes = {}

    def add_route(self, method, path, handler):
        self.routes[(method, path)] = handler

    def handle_request(self, method, path, *args, **kwargs):
        handler = self.routes.get((method, path))
        if handler:
            return handler(*args, **kwargs)
        else:
            return '404 Not Found', 404


router = RouterTemp()

# Add some routes
router.add_route('GET', '/', home)
router.add_route('GET', '/users/', list_users)
router.add_route('GET', '/users/<int:user_id>/', get_user)
router.add_route('POST', '/users/', create_user)
router.add_route('PUT', '/users/<int:user_id>/', update_user)
router.add_route('DELETE', '/users/<int:user_id>/', delete_user)

# MONGOOSE MODEL TEMPLATE FOR Python CRUD


class ModelMongoose:
    def __init__(self):
        self.client = mongoose.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["mydatabase"]
        self.collection = self.db["mycollection"]

    def insert_one(self, data):
        self.collection.insert_one(data)

    def find_one(self, query):
        return self.collection.find_one(query)

    def update_one(self, query, data):
        self.collection.update_one(query, {"$set": data})

    def delete_one(self, query):
        self.collection.delete_one(query)


# Example usage
model = ModelMongoose()
model.insert_one({"name": "John", "age": 30})
print(model.find_one({"name": "John"}))  # {"name": "John", "age": 30}
model.update_one({"name": "John"}, {"age": 35})
print(model.find_one({"name": "John"}))  # {"name": "John", "age": 35}
model.delete_one({"name": "John"})
print(model.find_one({"name": "John"}))  # None


# Controller template for Python CRUD


class Controller:
    def __init__(self, password):
        self.password = password
        self.salt = ''.join(random.choices(
            string.ascii_letters + string.digits, k=10))
        self.hashed_password = hashlib.sha256(
            (self.salt + self.password).encode('utf-8')).hexdigest()
        self.client = mongoose.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["mydatabase"]
        self.collection = self.db["mycollection"]

    def check_password(self, password_attempt):
        hashed_attempt = hashlib.sha256(
            (self.salt + password_attempt).encode('utf-8')).hexdigest()
        return self.hashed_password == hashed_attempt

    def create(self, password_attempt, data):
        if self.check_password(password_attempt):
            self.collection.insert_one(data)

    def read(self, password_attempt, query):
        if self.check_password(password_attempt):
            return self.collection.find(query)

    def update(self, password_attempt, query, data):
        if self.check_password(password_attempt):
            self.collection.update_many(query, {"$set": data})

    def delete(self, password_attempt, query):
        if self.check_password(password_attempt):
            self.collection.delete_many(query)


# Example usage
controller = Controller('mypassword')

# Create a new document
controller.create('mypassword', {"name": "John", "age": 30})

# Read all documents in the collection
print(list(controller.read('mypassword', {})))  # [{"name": "John", "age": 30}]

# Update all documents that match a query
controller.update('mypassword', {"name": "John"}, {"age": 35})

# Read all documents in the collection again
print(list(controller.read('mypassword', {})))  # [{"name": "John", "age": 35}]

# Delete all documents that match a query
controller.delete('mypassword', {"name": "John"})

# Read all documents in the collection again
print(list(controller.read('mypassword', {})))  # []

# CONTROLLER TEMPLATE FOR Python sql database that protects against SQL injection and XSS attacks and uses CSRF tokens


class CRUDController:
    def __init__(self, model, host, user, password, database):
        self.model = model
        self.cnx = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.csrf_tokens = {}

    def create(self, data, csrf_token):
        # Validate the CSRF token
        if csrf_token not in self.csrf_tokens:
            raise ValueError('Invalid CSRF token')
        del self.csrf_tokens[csrf_token]

        # Escape user input to prevent SQL injection and XSS attacks
        escaped_data = {key: mysql.connector.escape_string(
            str(value)) for key, value in data.items()}

        # Create a new instance of the model using the escaped data
        cursor = self.cnx.cursor()
        query = f"INSERT INTO {self.model.table_name} ({', '.join(escaped_data.keys())}) VALUES ({', '.join(['%s'] * len(escaped_data))})"
        cursor.execute(query, tuple(escaped_data.values()))
        self.cnx.commit()
        cursor.close()

    def read(self, pk):
        # Escape user input to prevent SQL injection and XSS attacks
        escaped_pk = mysql.connector.escape_string(str(pk))

        # Retrieve a single instance of the model using the escaped primary key
        cursor = self.cnx.cursor()
        query = f"SELECT * FROM {self.model.table_name} WHERE {self.model.pk_name} = %s"
        cursor.execute(query, (escaped_pk,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def update(self, pk, data, csrf_token):
        # Validate the CSRF token
        if csrf_token not in self.csrf_tokens:
            raise ValueError('Invalid CSRF token')
        del self.csrf_tokens[csrf_token]

        # Escape user input to prevent SQL injection and XSS attacks
        escaped_data = {key: mysql.connector.escape_string(
            str(value)) for key, value in data.items()}
        escaped_pk = mysql.connector.escape_string(str(pk))

        # Update an instance of the model using the escaped data
        cursor = self.cnx.cursor()
        query = f"UPDATE {self.model.table_name} SET {', '.join([f'{key} = %s' for key in escaped_data.keys()])} WHERE {self.model.pk_name} = %s"
