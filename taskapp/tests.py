from django.contrib.auth import get_user_model, authenticate
from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse

from .models import Task, TaskStatus
from .forms import TaskForm
from django.contrib.auth.models import User

# run test :  python manage.py test
class TaskModelTest(TestCase):
    """
    tests for model Task
    """
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username="developer1", password="qwerty123")
        cls.task = Task.objects.create(creator=user, assignee=user, title='Testing model')

    def test_title_max_length(self):
        task = Task.objects.get(id=1)
        max_length = task._meta.get_field('title').max_length
        self.assertEqual(max_length, 255)

    def test_title_default_edited(self):
        self.assertEqual(self.task.edited, False)

    def test_model_content(self):
        self.assertEqual(self.task.title, "Testing model")


class TaskStatusModelTest(TestCase):
    """
    tests for model TaskStatus
    """

    @classmethod
    def setUpTestData(cls):
        cls.task = TaskStatus.objects.create(name='Done')

    def test_str_representation(self):
        self.assertEqual(self.task.__str__(), self.task.name)

    def test_model_description_is_null(self):
        self.assertEqual(self.task.description, "")


class UrlTest(TestCase):
    """
    test for urls
    """

    @classmethod
    def setUpTestData(self):
        User.objects.create(username="developer1", password="qwerty123")
        authenticate(username="developer1", password="qwerty123")

    def testLoginPage(self):
        response = self.client.get(reverse('login'), follow=True)
        self.assertEqual(response.status_code, 200)

    def testCreateTaslPage(self):
        response = self.client.get(reverse('create_task'), follow=True)
        self.assertEqual(response.status_code, 200)

    def testProfilePage(self):
        response = self.client.get(reverse('profile', args=[1]), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("home"), follow=True)
        self.assertTemplateUsed(response, "main.html")



class FormsTest(TestCase):
    """
    test for forms
    """

    def test_valid_task_form(self):
        user = User.objects.create(username="developer1", password="qwerty123")
        task = Task.objects.create(creator=user, assignee=user, title='Testing model')
        data = {'title': task.title, 'creator': task.creator}
        form = TaskForm(data=data)
        self.assertTrue(form.is_valid())
