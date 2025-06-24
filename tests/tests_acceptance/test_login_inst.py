import django.test
from ta_app import models

class TestLoginScreen(django.test.TestCase):
    def setUp(self):
        models.myUser.objects.create(username="ProffessorInstructor", password="defaultPassword", name="Dan", usertype="instructor",email="inst@email.com"
                                     ,assignedInstructor=0)

    def test_bad_username(self):
        c = django.test.Client()
        resp = c.post("/", {'username': 'DefaultBad', 'pass': 'defaultPassword'})
        self.assertEquals(resp.context.get("message"), "Login Failed")

    def test_good_username(self):
        c = django.test.Client()
        resp = c.post("/", {'username': 'ProffessorInstructor', 'pass': ''})
        self.assertEquals(resp.context.get("message"), "Login Failed")

    def test_bad_PW(self):
        c = django.test.Client()
        resp = c.post("/", {'username': 'ProffessorInstructor', 'pass': 'badPassword'})
        self.assertEquals(resp.context.get("message"), "Login Failed")

    def test_good_PW(self):
        c = django.test.Client()
        resp = c.post("/", {'username': 'ProffessorInstructor', 'pass': 'defaultPassword'})
        self.assertRedirects(resp, '/menu/')
