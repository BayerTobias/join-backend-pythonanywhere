# Join Backend

## Introduction

This project is designed to create and manage users and provide the database for a task management tool, processing and delivering this data through API endpoints.

## Requirements

Make sure you have the following dependencies installed:

- asgiref==3.7.2
- Django==5.0.2
- django-cors-headers==4.3.1
- django-rest-passwordreset==1.4.0
- djangorestframework==3.14.0
- python-dotenv==1.0.1
- pytz==2024.1
- sqlparse==0.4.4
- tzdata==2023.4

Additionally, rename the `.env_example` file to `.env` and provide the necessary information:

EMAIL_HOST = "Enter Email Host example: smtp.gmail.com"  
EMAIL_HOST_USER = "Enter User example: abc@mail.com"  
EMAIL_HOST_PASSWORD = "Enter Password example: emailpassword"

## API Endpoints

- `/admin/`: Django admin panel
- `/login/`: User login endpoint
- `/logout/`: User logout endpoint
- `/check_auth/`: Endpoint to check user authentication status
- `/tasks/`: Endpoint for tasks
- `/tasks/<int:task_id>/`: Endpoint for a single task
- `/categorys/`: Endpoint for categories
- `/users/`: Endpoint for user list
- `/create_user/`: Endpoint to create a user
- `/delete_user/`: Endpoint to delete a user
- `/contacts/`: Endpoint for contacts
- `/contacts/<int:contact_id>/`: Endpoint for a single contact
- `/password_reset/`: Password reset endpoint (include the namespace `password_reset`)
- `/password_reset/confirm/`: Password reset confirmation endpoint (include the namespace `password_reset_confirm`)
