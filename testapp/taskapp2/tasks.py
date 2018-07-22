from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery()


@app.task
def task_two():
    """
    a simple task that prints hello
    replace everything with ur task under the function.
    """
    a = 'task_two'
    print(a)
    return a


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    """
    registering the task or making the task periodic and independent of any api call or hit.
    """
    sender.add_periodic_task(100, task_two.s())
