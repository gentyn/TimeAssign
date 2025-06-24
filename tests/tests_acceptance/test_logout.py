import django.test
from ta_app import models


class TestLogout(django.test.TestCase):
    def setUp(self):
        models.myUser.objects.create(username="RegularTa", password="defaultPassword", name="Jannis",
                                     usertype="ta", email="ta@email.com", assignedInstructor=0)
        models.myUser.objects.create(username="ProffessorInstructor", password="defaultPassword", name="Dan",
                                     usertype="instructor", email="inst@email.com", assignedInstructor=0)
        models.myUser.objects.create(username="DoctorChair", password="DoctorChair", name="DocyC",
                                     usertype="chair", email="chair@email.com", assignedInstructor=0)

class TestLogoutScreen(TestLogout):
    def test_good_PW_Chair(self):
        c = django.test.Client()
        resp = c.get('/logout')
        self.assertRedirects(resp, '/logout/', status_code=301, target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)
        #not sure how to test for this.

        #test cases for: logout when logged in
        #test case for: logout when not logged in
        #need to test for each user type, since they will each be seeing different menus.