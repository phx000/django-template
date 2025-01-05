import time

from django.test import TestCase
from django.db import connection
from api.tasks import test_task
from celery.result import AsyncResult

class ConnectionTests(TestCase):
    def test_db_connection(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM django_migrations")
            result = cursor.fetchall()
        self.assertNotEqual(result,None)

    def test_queue_connection(self):
        result=test_task.delay()
        self.assertIsInstance(result,AsyncResult)

