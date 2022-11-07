from django.test import TestCase
from django.urls import reverse
from links.models import CustomUser, Link


class TestUserRegistration(TestCase):
    def test_register_form(self):
        data = {
            'username': 'Tester1',
            'email': 'Tester1@gmail.com',
            'password1': 'testingpassword',
            'password2': 'testingpassword',
        }
        response = self.client.post(reverse('accounts:signup'), data)
        # 302 is for 'redirect', which means user registration is successful, 
        # any code other than 302 means test failed.
        self.assertEqual(response.status_code, 302)


class SignInViewTest(TestCase):
    def test_wrong_username(self):
        response = self.client.post('/login/', {'username': 'wrong', 'password': '12test12'})
        self.assertEqual(response.status_code, 200)
        # test should fail, because we're expecting 404 code, not 200

    def test_wrong_password(self):
        response = self.client.post('/login/', {'username': 'test', 'password': 'wrong'})
        self.assertEqual(response.status_code, 200)
        # test should fail, because we're expecting 404 code, not 200


class PriceTrackerView(TestCase):
    def test_anonymous_cannot_see_restricted_page(self):
        response = self.client.get(reverse("links:tracker"))
        self.assertRedirects(response, "/accounts/login/?next=/")

    def test_authenticated_user_can_see_restricted_page(self):
        user = CustomUser.objects.create_user("testingModel," "testingdev.io", "some_pass")
        self.client.force_login(user=user)
        response = self.client.get(reverse("links:tracker"))
        self.assertEqual(response.status_code, 200)

class TestSubmitLink(TestCase):
    def test_post_request_can_create_new_link(self):
        data = {
            'url': 'https://www.jumia.ma/lc-waikiki-ensemble-de-pyjama-en-velours-imprime-a-manches-longues-pour-bebe-garcon-58749374.html'
        }
        response = self.client.post(reverse("links:tracker"), data=data)
        self.assertEqual(response.status_code, 302)
