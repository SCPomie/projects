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


CharField	For short text strings (e.g., names, emails). max_length required.
TextField	For large text fields (e.g., descriptions).
IntegerField	For integers.
FloatField	For floating-point numbers.
BooleanField	For True/False values.
DateTimeField	For date and time.
DateField	For date only.
EmailField	For email addresses (with validation).
URLField	For URLs (with validation).
FileField	For uploading files.
ImageField	For uploading images.


Common Options:
max_length: Maximum length for CharField.
unique: Ensures field value is unique.
null: If True, allows NULL values in the database.
blank: If True, allows the field to be empty in forms.
default: Sets a default value.
choices: Restricts choices for a field.
help_text: Provides a description for the field in the admin panel.
