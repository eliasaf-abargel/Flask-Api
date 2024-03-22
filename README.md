# Flask-API Project
<p align="center">
  <img src="image.png" width="64" height="64" alt="Flask-API Icon">
</p>


Flask-API is a RESTful API framework built with Flask, designed to streamline the process of managing tasks. With a focus on simplicity and efficiency, this project offers endpoints for creating, reading, updating, and deleting tasks, backed by data persistence in a JSON file.

## Features

- **Create Tasks**: Easily add new tasks with a title and details.
- **List All Tasks**: Retrieve a comprehensive list of tasks.
- **Fetch Task Details**: Access specific tasks by their unique ID.
- **Update Tasks**: Modify the title and details of existing tasks.
- **Delete Tasks**: Remove tasks from the system.

Data persistence is ensured through the use of a JSON file, making data management straightforward and reliable.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.11 or higher
- pip package manager

## Installation

Follow these steps to get your Flask-API up and running:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Flask-Api.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Flask-Api
   ```
3. Create and activate a virtual environment:
   - For Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - For macOS and Linux:
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Set the necessary environment variables and start the Flask development server:

- For Windows:
  ```bash
  set FLASK_APP=main.py
  set FLASK_ENV=development
  ```
- For macOS and Linux:
  ```bash
  export FLASK_APP=main.py
  export FLASK_ENV=development
  ```

Run the server with:

```bash
flask run
```

Access the API at: http://localhost:5000.

## API Endpoints

- `GET /tasks`: List all tasks.
- `GET /tasks/:id`: Fetch a specific task by its ID.
- `POST /tasks`: Create a new task. Requires a JSON payload with `title` and `details`.
- `PUT /tasks/:id`: Update an existing task. Send a JSON payload with `title` and/or `details`.
- `DELETE /tasks/:id`: Remove a task by its ID.

## Contributing

We welcome contributions! If you have suggestions for improvements or encounter any issues, please feel free to open an issue or submit a pull request.


