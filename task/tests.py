from django.test import TestCase

# Create your tests here.

from .models import Task


class TaskModelTest(TestCase):

    def test_task_model_exist(self):
        tasks = Task.objects.count()

        self.assertEqual(tasks, 0)
    
    def test_model_has_string_representation(self):
        task = Task.objects.create(
            title='First Task',
            # description=
        )
        self.assertEqual(str(task), task.title)
    