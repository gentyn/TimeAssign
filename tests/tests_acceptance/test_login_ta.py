import django.test
from ta_app import models


class TestLoginScreen(django.test.TestCase):
    def setUp(self):
        models.myUser.objects.create(username="RegularTa", password="defaultPassword", name="Jannis",
                                     usertype="ta", email="ta@email.com", assignedInstructor=0)

    def test_bad_username(self):
        #self.assertEqual(app.command("DefaultBad"), "User not found.\nEnter user:")
        c = django.test.Client()
        resp = c.post("/", {'username': 'DefaultBad', 'pass': ''})
        self.assertEquals(resp.context.get("message"), "Login Failed")

    def test_good_username(self):
        #self.assertEqual(app.command("TA1"), "Password:")
        c = django.test.Client()
        resp = c.post("/", {'username': 'RegularTa', 'pass': ''})
        self.assertEquals(resp.context.get("message"), "Login Failed")

    def test_bad_PW(self):
        c = django.test.Client()
        resp = c.post("/", {'username': 'RegularTa', 'pass': 'badPAss'})
        self.assertEquals(resp.context.get("message"), "Login Failed")

    def test_good_PW(self):
        c = django.test.Client()
        resp = c.post("/", {'username': 'RegularTa', 'pass': 'defaultPassword'})
        self.assertRedirects(resp, '/menu/')



