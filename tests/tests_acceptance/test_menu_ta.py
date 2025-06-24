import django
from django.test import TestCase, Client
from ta_app import models

# Possible menu options:
# View/Edit Schedule
# Change password
# Logout

class TestTaMenuSetup(TestCase):
    def setUp(self):
        models.myUser.objects.create(username="teststudent1989", password="teststudent1989", name="taylorswift",
                                     usertype="ta", email="swaggu@email.com", assignedInstructor=0)


class TestTaMenu(TestTaMenuSetup):


    def test_ve_sched(self):
        c = django.test.Client()
        c.post('/', {'username': 'teststudent1989', 'pass': 'teststudent1989'})
        resp = c.get('/editSchedule')
        self.assertRedirects(resp, '/editSchedule/', status_code=301, target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)


    def test_logout(self):
        c = django.test.Client()
        c.post('/', {'username': 'teststudent1989', 'pass': 'teststudent1989'})
        resp = c.get('/logout')
        self.assertRedirects(resp, '/logout/', status_code=301, target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)


class testChairMenuNoUserLoggedIn(TestTaMenuSetup):

    def test_menu_NoLogin(self):
        c = django.test.Client()
        resp = c.get('/menu', follow=True)
        self.assertRedirects(resp, '/logout/', status_code=301, target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)

    def test_ve_sched(self):
        c = django.test.Client()
        resp = c.get('/logout')
        self.assertRedirects(resp, '/logout/', status_code=301, target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)

    def test_logout(self):
        c = django.test.Client()
        resp = c.get('/logout', follow=True)
        self.assertRedirects(resp, '/logout/', status_code=301, target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)
