from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm
from .views import SignupPageView
# Create your tests here.

class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='will',
            email='test@gmail.com',
            password='test'
        )
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'test@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='will',
            email='test@gmail.com',
            password='test'
        )
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'test@gmail.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

class SignupPageTest(TestCase):

    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/signup.html')
        self.assertContains(self.response, 'Sing Up')

    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_resolve_url(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)
