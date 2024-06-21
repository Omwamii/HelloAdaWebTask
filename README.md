# Task Management Web Application

This is a simple web application for managing tasks, built with Django. Users can create an account, log in, and manage their tasks (create, read, update, delete). As part of the Hello Ada interview process.

## Features

- User Authentication:
  - Register with an email and password.
  - Log in and log out.
- Task Management:
  - Create a new task with a title and description.
  - View a list of all tasks.
  - Update the title and description of tasks.
  - Delete a task.
- Database:
  - Uses SQLite to store user and task information.
  - Each user has their own set of tasks.

## Requirements

- Python 3.x
- Django 4.x or higher

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Omwamii/HelloAdaWebTask.git
    cd taskmanagement
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the development server:
    ```bash
    python manage.py runserver
    ```

4. Open your web browser and go to `http://127.0.0.1:8000/` to see the application.

## Usage

### User Registration and Authentication

- Register a new user by clicking on the "Register" link and filling out the registration form.
- Log in using your registered email and password.
- Log out by clicking the "Logout" link.

### Task Management

- Create a new task by clicking the "Create Task" button and filling out the form.
- View your tasks on the main page.
- Update a task by clicking the "Edit" button next to a task and updating the form.
- Delete a task by clicking the "Delete" button next to a task.
- Undo a Task marked as done by clicking 'Undo' button

## Project Snapshots
![Screenshot from 2024-06-20 18-45-11](https://github.com/Omwamii/HelloAdaWebTask/assets/100716410/717f3bee-c3cf-4a0f-8f42-fbb905a50c58)
![Screenshot from 2024-06-20 18-45-48](https://github.com/Omwamii/HelloAdaWebTask/assets/100716410/885222c8-16db-4c8e-8182-af51013e9660)
![Screenshot from 2024-06-20 18-46-33](https://github.com/Omwamii/HelloAdaWebTask/assets/100716410/1e7743d4-57cd-4e28-bc72-b3bfead52a8b)
![Screenshot from 2024-06-20 18-39-47](https://github.com/Omwamii/HelloAdaWebTask/assets/100716410/d6b9c8fc-265c-454e-9429-30ce083681b6)
