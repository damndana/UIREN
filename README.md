# Sxodim.SDU - Student Social Platform

A Django-based social platform for SDU students to connect, participate in events, and manage their campus activities.

## Features

- User Authentication (Sign In/Register)
- Event Management
- Space Booking System
- Club Management
- Interactive Campus Map
- AI Helper
- Points System for Event Participation

## Tech Stack

- Python 3.12
- Django 5.1.7
- SQLite Database
- HTML/CSS/JavaScript
- Bootstrap (for styling)

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/yourusername/sxodim-sdu.git
cd sxodim-sdu
```

2. Create and activate a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Visit http://127.0.0.1:8000/ in your browser

## Project Structure

```
sxodim-sdu/
├── core/                 # Project settings
├── main/                 # Main application
│   ├── migrations/      # Database migrations
│   ├── static/         # Static files (CSS, JS, images)
│   ├── templates/      # HTML templates
│   ├── models.py       # Database models
│   ├── views.py        # View functions
│   └── urls.py         # URL routing
├── manage.py           # Django management script
├── requirements.txt    # Project dependencies
└── README.md          # This file
```

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 