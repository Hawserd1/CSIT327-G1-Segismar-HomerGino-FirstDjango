# CampusConnect

CampusConnect is a Django web application with custom user accounts, signup and
login pages, and a role-aware dashboard. Its pages use Bootstrap 5 from the
jsDelivr CDN.

## Requirements

- Python 3.13 or later
- Django 6.1.2

## Setup on Windows

Open PowerShell in the project directory and run:

```powershell
py -m venv .venv
.\.venv\Scripts\activate
python -m pip install Django==6.1.2
python manage.py migrate
python manage.py runserver
```

Open <http://127.0.0.1:8000/> in a browser. The dashboard requires you to log in;
new users can register at `/accounts/signup/`.

To create an administrator account for Django's admin site, run:

```powershell
python manage.py createsuperuser
```

## Main routes

| URL | Description |
| --- | --- |
| `/` | Dashboard (login required) |
| `/accounts/signup/` | Create an account |
| `/accounts/login/` | Log in |
| `/accounts/logout/` | Log out |
| `/accounts/profile/` | Edit your profile (login required) |
| `/admin/` | Django admin site |
| `/admin-panel/` | Admin-only dashboard panel |

The custom user model includes a role (student, instructor, or administrator)
and an optional course. After signup, a success message appears on the login
page. Signed-in users can update their name, email, and course from their profile;
their account role is not editable there.

## Tests

Run the Django test suite with:

```powershell
python manage.py test
```

## Production note

The checked-in settings are for local development. Before deploying, configure a
private `SECRET_KEY`, set `DEBUG = False`, configure `ALLOWED_HOSTS`, and review
Django's deployment checklist.
