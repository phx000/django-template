from celery import shared_task

# todo delete this
@shared_task
def test_task():
    return "TEST TEXT"