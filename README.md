# Django Grocery Store Web Application

## Overview
This Django web application is a grocery store platform designed to facilitate online shopping for groceries. It provides users with a convenient way to browse, search, and purchase groceries from the comfort of their own homes.

## Features
1. **Product Catalog**: Browse a wide selection of groceries categorized into different sections (e.g., fruits, vegetables, dairy, etc.).
2. **Search Functionality**: Easily search for specific groceries using keywords or filters.
3. **User Authentication**: Register an account or log in to an existing account to access additional features such as saving favorite items or viewing order history.
4. **Shopping Cart**: Add items to a virtual shopping cart and proceed to checkout for payment.
5. **Order Management**: View and manage orders, including order status and delivery tracking.
6. **Admin Panel**: Administrators can manage products, categories, and user accounts through an intuitive admin interface.

## Prerequisites
1. Python 3.12 and Django installed
2. Docker installed
3. Git installed
4. Jenkins installed and configured

## Steps to Run Locally
1. Clone the Repository: https://github.com/TylerBonaparte/GroceryApp.git

2. Navigate to project directory:
   - cd GroceryApp

3. Install Python dependencies:
   - pip install -r requirements.txt

5. Apply migrations:
   - python manage.py migrate 
    
6. Run Django development server
   - python manage.py runserver

## Usage
- Access the application by opening your web browser and navigating to http://localhost:8000.
- Explore the product catalog, add items to your cart, and proceed to checkout to place an order.
- To access the admin panel, go to http://localhost:8000/admin and log in with admin credentials.
- Use the admin panel to manage products, categories, users, and orders.
    
# Jenkins Pipeline Configuration
The Jenkins pipeline automates the build and deployment process of the web application using Docker containers.

# Pipeline Stages:
- Checkout the code from the Git repository.
- Build a Docker image for the web application.
- Optionally, run tests using Django's test framework.
- Push the Docker image to a Docker registry.
- Deploy the application using Docker Compose.

# Contributors
- Tyler Bonaparte
- tbonaparte.tb@gmail.com