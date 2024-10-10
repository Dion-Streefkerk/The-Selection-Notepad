# TheSelectionNotePad

**TheSelectionNotePad** is a full-stack web application designed for managing personal notes with seamless interaction between the frontend and backend.

## Table of Contents

- [Tech Stack](#tech-stack)
  - [Frontend](#frontend)
  - [Backend](#backend)
- [Project Setup Guide](#project-setup-guide)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Backend Setup](#2-backend-setup)
    - [a. Navigate to the Backend Directory](#a-navigate-to-the-backend-directory)
    - [b. Create and Activate a Virtual Environment](#b-create-and-activate-a-virtual-environment)
    - [c. Configure Python Interpreter in VSCode](#c-configure-python-interpreter-in-vscode)
    - [d. Install Backend Dependencies](#d-install-backend-dependencies)
    - [e. Run the Backend Server](#e-run-the-backend-server)
  - [3. Frontend Setup](#3-frontend-setup)
    - [a. Navigate to the Frontend Directory](#a-navigate-to-the-frontend-directory)
    - [b. Install Frontend Dependencies](#b-install-frontend-dependencies)
    - [c. Install Additional Frontend Packages](#c-install-additional-frontend-packages)
    - [d. Run the Frontend Development Server](#d-run-the-frontend-development-server)
  - [4. Access the Application](#4-access-the-application)
- [Features](#features)
- [Additional Instructions](#additional-instructions)

## Tech Stack

### Frontend
- **Vue.js**: Dynamic and reactive user interface.
- **Vue Router**: Handles navigation between different pages.

### Backend
- **Flask (Python)**: Lightweight web framework for building APIs.
- **SQLAlchemy**: ORM for managing and interacting with the SQLite database.
- **SQLite**: Lightweight database suitable for this application.

## Project Setup Guide

### 1. Clone the Repository
Start by cloning the project from the GitHub repository and navigating into the project folder:

  ```bash
  git clone <repository-url>
  cd <project-folder>
  ```
### 2. Backend Setup

#### a. Navigate to the Backend Directory

  ```bash
  cd backend
  ```
#### b. Create and Activate a Virtual Environment

**Create the Environment:**
  ```bash
  python -m venv venv
   ```

### Activate the Virtual Environment

To ensure that all dependencies are managed correctly, activate the virtual environment using the appropriate command for your operating system.

- **Windows:**

    ```bash
    venv\Scripts\activate
    ```

- **macOS/Linux:**

    ```bash
    source venv/bin/activate
    ```

#### c. Configure Python Interpreter in VSCode
Before installing dependencies, ensure that VSCode uses the correct Python interpreter from your virtual environment:

1. Open VSCode.
2. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS) to open the Command Palette.
3. Type `Python: Select Interpreter`.
4. Choose the interpreter from your virtual environment (`venv`).

#### d. Install Backend Dependencies
With the virtual environment activated and the Python interpreter configured, install the necessary backend dependencies:

  ```bash
  pip install -r requirements.txt
  ```
#### e. Run the Backend Server
Start the Flask server:

  ```bash
  python app.py
  ```
The server will be available at: http://127.0.0.1:5000

### 3. Frontend Setup

#### a. Navigate to the Frontend Directory
  ```bash
  cd ../frontend
  ```
#### b. Install Frontend Dependencies
Ensure you have [Node.js](https://nodejs.org/) installed, then install the required packages:

  ```bash
  npm install
  ```
#### c. Install Additional Frontend Packages
Install Bootstrap and Axios, which are essential for styling and API communication:

- **Install Bootstrap for Frontend Styling:**
  ```bash
  npm install bootstrap
  ```
- **Install Axios for API Requests:**
  ```bash
  npm install axios
  ```
#### d. Run the Frontend Development Server
Start the Vue.js development server:

```bash
npm run serve
```
The frontend will run at: http://localhost:8080.

### 4. Access the Application
Ensure both the backend and frontend servers are running:

- **Backend:** [http://127.0.0.1:5000](http://127.0.0.1:5000)
- **Frontend:** [http://localhost:8080](http://localhost:8080)

You can now access **TheElectionNotePad** application in your browser.

## Features

- **User Management:** Users can register and log in to manage their notes.
- **Note Management:** Users can create, edit, delete, and manage notes, which are private to each user.
- **Authentication:** JWT (JSON Web Token) is used for managing user sessions to ensure secure interactions.
- **Axios for Frontend-Backend Communication:** Axios handles HTTP requests between Vue.js and Flask.

## Additional Instructions

### Configuring Python Interpreter in VSCode (Detailed)
To ensure VSCode uses the correct Python interpreter from your virtual environment:

1. Open VSCode.
2. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS) to open the Command Palette.
3. Type `Python: Select Interpreter` and press `Enter`.
4. From the list, select the interpreter located in your project's `venv` folder (e.g., `./venv/bin/python` or `.\venv\Scripts\python.exe`).

This step ensures that all Python-related operations in VSCode use the dependencies from your virtual environment.

### Contact

For any further questions or support, feel free to reach out to the maintainer:

- **Email:** dionstreefkerk10@gmail.com
- **GitHub:** [@yourusername](https://github.com/Dion-Streefkerk)
- 
## Happy Note-taking! 📝

You can log in with the following credentials to explore The Election Notepad:

- **Username:** `TestAccount`
- **Password:** `Test123!`

## Happy Note-taking! 📝

You can log in with the following credentials to explore The Election Notepad:

- **Username:** `TestAccount`
- **Password:** `Test123!`

There are already some pre-made notes, so you can get an idea of what you can do with the notepad, like **organizing your functions**. I've added a code editor-like format to the forms, complete with color and structure using **highlight.js**
