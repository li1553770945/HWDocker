cd /code
python3.6 manage.py makemigrations login work group
python3.6 manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin','admin@example.com','admin123456')" | python3.6 manage.py shell
uwsgi -i /code/uwsgi.ini
