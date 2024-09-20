from django.test import TestCase

# Create your tests here.

from .models import Task


class TaskModelTest(TestCase):

    def test_task_model_exist(self):
        tasks = Task.objects.count()

        self.assertEqual(tasks, 0)
    
    def test_model_has_string_representation(self):
        task = Task.objects.create(title='First Task')
        self.assertEqual(str(task), task.title)

class IndexPageTest(TestCase):
    def test_index_page_returns_correct_response(self):
        response = self.client.get('/')
        print('test_index_page_returns_correct_response', f'{response = }')

        self.assertTemplateUsed(response, 'task/index.html')
        self.assertEqual(response.status_code, 200)
    
    def test_index_page_has_tasks(self):
        task = Task.objects.create(title='First Task')

        response = self.client.get('/')
        print('test_index_page_has_tasks', f'{response = }')

        self.assertContains(response, task.title)

