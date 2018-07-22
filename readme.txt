CELERY version = 4+
Django version = 2+
django-celery-beat version = 1.1.1
python 3



How to run!!
1.clone the repo.
2.install rabbitMQ.
3.Make a virtual env.
4.install python libraries from requirements.txt.
5.Using cmd go to project lib do python manage.py migrate and then start server,
6.in your CMD type "set FORKED_BY_MULTIPROCESSING=1" if u are using windows else there is no need for this command.
7.Run server and go to django admin page localhost:8000/admin/ and use testapp and testing as username and password.
8.After login in the admin page u will see a "periodic tasks" in the page.
9.Go to interval and make an interval.
10.Go back and go to Periodic tasks and look for the tasks name defined in testapp/settings.py and apply interval to the tasks
   in ur django page(periodic tasks)
11.Open another terminal and type "celery -A testapp worker -l info" to run ur celery worker
12.Open one more terminal and type "celery -A testapp beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler"
   to run ur celery beat to make ur tasks use the scheduler and send tasks periodically to worker.
13.Check ur worker for if tasks are being received or not.

-------------------------------Working of celery, django, celery beat and rabbitMQ--------------------------------------