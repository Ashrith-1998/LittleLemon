# Little Lemon Restaurant API

## Meta Back-End Developer Capstone Project

This project is a RESTful API developed using Django and Django REST Framework as part of the Meta Back-End Developer Professional Certificate Capstone.

The API allows users to:

- View menu items
- Add, update and delete menu items
- Create and manage restaurant bookings
- Authenticate users using Djoser Token Authentication
- Access the Django Admin Panel

---

## Technologies Used

- Python 3.x
- Django
- Django REST Framework
- MySQL
- Djoser
- Token Authentication

---

## Project Structure

```
littlelemon/
│
├── littlelemon/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── restaurant/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   ├── tests.py
│   └── permissions.py
│
├── manage.py
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project folder

```bash
cd littlelemon
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Database Configuration

Create a MySQL database

```sql
CREATE DATABASE littlelemon;
```

Update the database credentials inside

```
littlelemon/settings.py
```

Run migrations

```bash
python manage.py migrate
```

Create a superuser

```bash
python manage.py createsuperuser
```

Run the development server

```bash
python manage.py runserver
```

---

## API Endpoints

### Menu

GET

```
/restaurant/menu/items/
```

POST

```
/restaurant/menu/items/
```

GET Single Item

```
/restaurant/menu/items/<id>/
```

---

### Booking

```
/restaurant/booking/tables/
```

---

### Authentication

Generate Token

```
/restaurant/api-token-auth/
```

Djoser Authentication

```
/auth/
```

---

## Testing

Run unit tests

```bash
python manage.py test
```

Run project checks

```bash
python manage.py check
```

---

## Admin Panel

```
http://127.0.0.1:8000/admin/
```

---

## Author

Ashrith BC

Meta Back-End Developer Capstone Project