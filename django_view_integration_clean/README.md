# django_view_integration (CLEAN, one-command demo)

## Run
1) Open PowerShell **in this folder** (the one with manage.py).
2) Run:

   pip install Django
   python manage.py migrate
   python manage.py runserver

Open: http://127.0.0.1:8000/
- Root redirects to /items/
- Favicon is included (no noisy 404)
- DB is pre-seeded with a few items after `migrate`
