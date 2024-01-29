# Getting Started with your Flask / React project

This project uses Create-React-App, Flask and SQLite.

## Available Scripts

You will need to be running two scrips in two separate terminal tabs / windows.

One will be for for running the Flask server, and the other for the React server.

---

## Install dependencies

### For Flask

First, make sure you drop into the `/api` directory, create and then run a virtual environment:

`python -m venv venv && source venv/bin/activate`

(For future sessions, only `source venv/bin/activate` will be needed to start the virtual environment. I recommend aliasing this command!)

Then install all dependencies `pip install -r requirements.txt` (only the first time)

### For React

In your other Terminal window, in the root of the project directory, run `npm install` (only the first time)

---

## Run the servers

### For Flask

Ensure that your virtual environment is running (You should see a `(venv)` at the end of your prompt)

Then _move back to the root of the project_ and run

`npm run start-api`

This will run the Flask server on port 5000

### For the React server

Run `npm run start`

This will start your React dev server on port 3000.

You should now be able to see the app in the browser.

---

## To stop the app:

### For Flask

Use `ctrl + C` to stop the server
Run `deactivate` to stop the virtual environment. You do not need to move into the `/api` directory first. (You do need to in order to _start_ the virtual environment, though.)

### For React

Use `ctrl + C` to stop the server.

---

### Quick Setup: New Clone
- Flask
    - `cd /api`
    - `python -m venv venv && source venv/bin/activate`
    - `pip install -r requirements.txt`
    - `cd ../recipe-app`
    - `npm run start-api`
### Quick Setup: Existing Clone
- Flask
    - `source venv/bin/activates`
- React
    - in root directory `/recipe-app`
    - `npm run start`

Have fun! 😎 🎉 💻
