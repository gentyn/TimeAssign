import django
from django.test import TestCase, Client
from ta_app import models

# Possible menu options:
# Assign ta to course
# Logout

class TestInstMenuSetup(TestCase):
    def setUp(self):
        models.myUser.objects.create(username="testinst", password="testinst", name="JaysonRock",
                                     usertype="instructor", email="poopoo@email.com", assignedInstructor=0)

class TestChairMenu(TestInstMenuSetup):
    def test_assign_ta(self):
        c = django.test.Client()
        c.post('/', {'username': 'testinst', 'pass': 'testinst'})
        resp = c.get('/instructor_assignToCourse/')
        self.assertRedirects(resp, '/instructor_assignToCourse/', status_code=301, target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)


    def test_logout(self):
        c = django.test.Client()
        c.post('/', {'username': 'testinst', 'pass': 'testinst'})
        resp = c.get('/logout')
        self.assertRedirects(resp, '/logout/', status_code=301, target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)


class testChairMenuNoUserLoggedIn(TestInstMenuSetup):

    def test_menu_NoLogin(self):
        c = django.test.Client()
        resp = c.get('/menu', follow=True)
        self.assertRedirects(resp, '/logout/', status_code=301, target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)

    def test_assign_ta(self):
        c = django.test.Client()
        resp = c.get('/inst_assignToCourse', follow=True)
        self.assertRedirects(resp, '/logout/', status_code=301, target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)

    def test_logout(self):
        c = django.test.Client()
        resp = c.get('/logout')
        self.assertRedirects(resp, '/logout/', status_code=301, target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)
