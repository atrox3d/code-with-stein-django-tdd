from django.test import TestCase

# Create your tests here.

from .models import Task


class TaskModelTest(TestCase):

    def test_task_model_exist(self):
        tasks = Task.objects.count()

        self.assertEqual(tasks, 0)
    