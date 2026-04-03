# URL Shortener API

A REST API built with Django and Django REST Framework that shortens long URLs.

## Tech Stack
- Django
- Django REST Framework
- PostgreSQL
- drf-spectacular (Swagger docs)

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/shorten/ | Shorten a long URL |
| GET | /api/urls/ | List of all shortened URLs |
| GET | /<short_code>/ | Redirect to original URL |

## Setup
1. Clone the repo
2. Create virtual environment and activate it
3. Install dependencies: `pip install -r requirements.txt`
4. Create `.env` file with your credentials
5. Run migrations: `python manage.py migrate`
6. Start server: `python manage.py runserver`

## API Docs
Visit `/api/schema/swagger-ui/` for interactive Swagger documentation.