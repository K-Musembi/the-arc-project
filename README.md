Simple Library Project

------------------------------------------------------------------
(Note: The project has been implemented using Python Django instead of Ruby on Rails framework due to time constraints.)

------------------------------------------------------------------
Implementation:
- Linux Ubuntu system
- Activate venv (virtual environment)
- Install dependencies: pip3 install requirements.txt
- Create local MySQL database and run database migrations
- Create a .env file with environment variables add to project directory
- Run the program: python3 manage.py runserver 0.0.0.0:8000
------------------------------------------------------------------
Usage:
- Create account as a new user
- Login after signup (Django in-built auth)
- View user profile, i.e. list of current borrowed books
- Option to borrow a book if its not yet borrowed
- Option to return a borrowed book
------------------------------------------------------------------
Tests:
- Go to main project directory
- Run command: pytest app/tests
------------------------------------------------------------------
Authors:
- Kevin Musembi [https://github.com/K-Musembi] [https://www.linkedin.com/in/kevin-musembi/]
