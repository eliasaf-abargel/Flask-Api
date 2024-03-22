# Flask-Api
![Flask-Api Project](https://www.google.com/url?sa=i&url=https%3A%2F%2Fmedium.com%2Fanalytics-vidhya%2Frestful-api-with-python-and-flask-6e65e79a5e15&psig=AOvVaw2Zwb7zbmIJqJ9xpXUKGtvm&ust=1711186461544000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCPipy7vIh4UDFQAAAAAdAAAAABAE)

Flask-Api is a RESTful API built with Flask that allows you to manage tasks. It provides endpoints for creating, reading, updating, and deleting tasks, with data persisted in a JSON file.

## Features

- Create new tasks with a title and details
- Retrieve a list of all tasks
- Retrieve a specific task by its ID
- Update the title and details of a task
- Delete a task
- Data persistence using a JSON file

## Prerequisites

- Python 3.11 or higher
- pip package manager

## Installation

1. Clone the repository: ״[git clone https://github.com/your-username/Flask-Api.git](https://github.com/eliasaf-abargel/Flask-Api.git)״
2. Navigate to the project directory: ״cd Flask-Api״
3. Create a virtual environment: ״python -m venv venv״
4. Activate the virtual environment:
- For Windows:
  ```
  venv\Scripts\activate
  ```
- For macOS and Linux:
  ```
  source venv/bin/activate
  ```

5. Install the required dependencies: ״pip install -r requirements.txt״



## Usage

1. Set the necessary environment variables:
- For Windows:
  ```
  set FLASK_APP=main.py
  set FLASK_ENV=development
  ```
- For macOS and Linux:
  ```
  export FLASK_APP=main.py
  export FLASK_ENV=development
  ```

2. Run the Flask development server: ״flask run״
3. The API will be accessible at `http://localhost:5000`.

## API Endpoints

- `GET /tasks`: Retrieve a list of all tasks.
- `GET /tasks/:id`: Retrieve a specific task by its ID.
- `POST /tasks`: Create a new task. Send a JSON payload with `title` and `details` fields.
- `PUT /tasks/:id`: Update a task by its ID. Send a JSON payload with `title` and/or `details` fields.
- `DELETE /tasks/:id`: Delete a task by its ID.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
