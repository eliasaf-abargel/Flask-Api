# main.py

from flask import Flask
from routes.task_routes import task_blueprint  # Importing the blueprint from task_routes.py
from dotenv import load_dotenv  # Importing the load_dotenv function

load_dotenv()

# main.py
app = Flask(__name__)
app.register_blueprint(task_blueprint, url_prefix='/tasks')  # Registering the blueprint

if __name__ == '__main__':
    app.run(debug=True)
