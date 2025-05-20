🏠 AirBnB Clone Project
📌 Project Overview
The AirBnB Clone is a simplified version of the AirBnB platform. In this first phase, the focus is on building the backend console — a command-line interface that allows users to interact with and manage application data. This console simulates basic object management functionalities like creation, updating, deletion, and persistent storage.

⚙️ Core Functionality
✅ Console Capabilities
The command interpreter enables:

Creating new instances of classes (e.g., User, Place)

Displaying stored objects

Updating attributes of existing instances

Deleting objects

Counting and listing instances

Persisting data via JSON file storage

🧱 Implementation Details
🔹 BaseModel
A foundational class that handles:

Initialization of instances

Serialization to dictionaries

Saving to JSON files

Deserialization back to Python objects

🔹 Object Storage
Implements a simple storage engine using:

Instance <-> Dictionary <-> JSON <-> File structure

File-based persistence via file.json

🔹 Classes
Custom classes inherit from BaseModel:

User

State

City

Amenity

Place

Review

🔹 Unit Testing
Comprehensive test coverage using Python’s unittest module

Ensures that all models and the storage engine behave as expected

💻 Using the Command Interpreter
To start the interactive console, run:

bash
Copy
Edit
./console.py
You can type help to see the list of available commands:

pgsql
Copy
Edit
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  delete  destroy  exit  help  q  quit  show  update

(hbnb) quit
🧪 Running Tests
To run all tests:

bash
Copy
Edit
python3 -m unittest discover tests
To run a specific test file:

bash
Copy
Edit
python3 -m unittest tests/test_models/test_city.py