# python manage.py collectstatic --noinput 
# python manage.py migrate --noinput 
gunicorn college_management_system.wsgi:application --bind 0.0.0.0:$PORT 