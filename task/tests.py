from django.test import TestCase

# Create your tests here.

from .models import Task
from .forms import NewTaskForm

class TaskModelTest(TestCase):

    def test_task_model_exist(self):
        tasks = Task.objects.count()

        self.assertEqual(tasks, 0)
    
    def test_model_has_string_representation(self):
        task = Task.objects.create(title='First Task')
        self.assertEqual(str(task), task.title)

class IndexPageTest(TestCase):
    def setUp(self) -> None:
        self.task = Task.objects.create(title='First Task')

    def test_index_page_returns_correct_response(self):
        response = self.client.get('/')
        print('test_index_page_returns_correct_response', f'{response = }')

        self.assertTemplateUsed(response, 'task/index.html')
        self.assertEqual(response.status_code, 200)
    
    def test_index_page_has_tasks(self):
        response = self.client.get('/')
        print('test_index_page_has_tasks', f'{response = }')

        self.assertContains(response, self.task.title)


class DetailPageTest(TestCase):
    def setUp(self) -> None:
        self.task = Task.objects.create(
            title='First Task', description='the description'
        )
        self.task2 = Task.objects.create(
            title='Second Task', description='second description'
        )
    
    def test_detail_page_returns_correct_response(self):
        response = self.client.get(f'/{self.task.id}/')
        print('test_detail_page_returns_correct_response', f'{response = }')

        self.assertTemplateUsed(response, 'task/detail.html')
        self.assertEqual(response.status_code, 200)

    def test_detail_page_has_correct_content(self):
        response = self.client.get(f'/{self.task.id}/')
        print('test_detail_page_has_correct_content', f'{response = }')

        self.assertContains(response, self.task.title)
        self.assertContains(response, self.task.description)
        self.assertNotContains(response, self.task2.title)
        self.assertNotContains(response, self.task2.description)

class NewPageTest(TestCase):
    # def setUp(self) -> None:
        # self.form = NewTaskForm

    def test_new_page_returns_correct_response(self):
        response = self.client.get(f'/new/')
        print('test_new_page_returns_correct_response', f'{response = }')

        self.assertTemplateUsed(response, 'task/new.html')
        self.assertEqual(response.status_code, 200)

    def test_form_can_be_valid(self):
        # self.assertTrue(issubclass(self.form, NewTaskForm))
        self.assertTrue('title' in NewTaskForm.Meta.fields)
        self.assertTrue('description' in NewTaskForm.Meta.fields)

        form = NewTaskForm({
            'title': 'the title',
            'description': 'the description'
        })
        self.assertTrue(form.is_valid())
    
    def test_new_page_form_rendering(self):
        response = self.client.get('/new/')
        print('test_new_page_form_rendering', f'{response = }')

        self.assertContains(response, '<form')
        self.assertContains(response, 'csrfmiddlewaretoken')
        self.assertContains(response, '<label for')
    
