django-admin startproject project_name .

python manage.py startapp app_name


python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser


create own url in app folder

add url and app inside the app folder

LOGIN_URL = "index"
LOGIN_REDIRECT_URL = "index"
LOGOUT_REDIRECT_URL = "index"
