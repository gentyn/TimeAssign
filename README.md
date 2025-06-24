# Time Assignment System

A Django web application for managing time assignments, courses, and user roles.

## Features

- User management (Add, view, edit users)
- Course management (Add, view, edit courses)
- Role-based access (Chair, Instructor, TA)
- Schedule management
- Break management
- Validation system

## Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd tyndallr-time-assign-4983df0ca2bf
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run database migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

6. Open your browser and navigate to `http://127.0.0.1:8000/`

## Project Structure

- `ta_app/` - Main Django application
- `templates/` - HTML templates
- `static/` - Static files (CSS, images)
- `tests/` - Test files
- `timeassign/` - Django project settings

## Technologies Used

- Django 5.2.3
- Python 3.x
- SQLite database
- HTML/CSS templates 