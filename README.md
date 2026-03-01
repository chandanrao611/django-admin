**Django:**
**Step 1:** Install Python (Check First)
            python –version
**Step 2:** Create Virtual Environment (Very Important)
            python -m venv venv
            venv\Scripts\activate
**Step 3:** Install Django
            pip install django
            django-admin –version
**Step 4:** Create New Django Project
            django-admin startproject myproject
**Step 5:** Run Server
            python manage.py runserver
**Step 6:** Create App (Very Important)
            python manage.py startapp myapp

**Create app inside that folder**
  python manage.py startapp hotel_admin apps/hotel_admin
**Step 7:** Apply Migrations
            python manage.py makemigrations
            python manage.py migrate
**Step 8:** Enable Admin Panel
            Create admin user:
              python manage.py createsuperuser
**_Command	Purpose_**
runserver	Start server
makemigrations	Create migration file
migrate	Apply database changes
createsuperuser	Create admin login
