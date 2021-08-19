# Report_Card_Creator
1: clone the project with gh repo clone robin-rawat/Report_Card_Creator 
2: install libraries with pip install -r requirements.txt
3: run python manage.py makemigrations
4: run python manage.py migrate
5: download redis from gh repo clone robin-rawat/Report_Card_Creator
6: run redis-server
7: run celery worker : celery -A student_manager worker -l INFO
8: run django server : python manage.py runserver.
