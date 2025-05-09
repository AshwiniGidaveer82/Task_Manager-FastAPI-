🎯 Task Manager

Task Manager is a FastAPI-based web application designed for managing tasks. Users can create, view, and delete tasks. The application provides a simple interface to interact with task data and includes functionality to retrieve all tasks, add new tasks, and remove tasks by their unique IDs.

✨ Features

Task Management: Users can create new tasks by providing a title, view all tasks, and delete tasks by their unique IDs.

Task Retrieval: The application allows users to fetch a list of all tasks.

Task Deletion: Users can delete a task by specifying its unique task ID.

🚀 How It Works

Start the Application: Upon running the application, users can interact with the API to perform CRUD operations on tasks.

Create a Task: Users can send a POST request to add a new task with a title.

View Tasks: Users can view all tasks by sending a GET request.

Delete a Task: Users can delete a task by providing the unique task ID in the DELETE request.

🛠️ Technologies Used

FastAPI: The backend framework for building and serving the API.

SQLAlchemy: ORM used for database interaction.

Jinja2: Templating engine used for rendering HTML pages.

CSS: For styling the front end.

📋 How to Run the Project

1. Clone the repository:

bash
Copy
Edit
git clone https://github.com/AshwiniGidaveer82/Task_Manager.git

2. Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt

3. Run the FastAPI application:

bash
Copy
Edit
uvicorn main:app --reload

4. Access the application in the browser:

Navigate to http://127.0.0.1:8000 to interact with the Task Manager API.

