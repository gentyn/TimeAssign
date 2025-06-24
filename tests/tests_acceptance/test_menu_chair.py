import django
from django.test import TestCase, Client
from ta_app import models

# Possible menu options:
# Add TA
# Add Instructor
# Add Course
# View/Edit TAs
# View/Edit Instructors
# View/Edit Courses
# Assign Instructor
# Assign TA
# Validate
# View Contacts
# Email Users
# User Settings
# Logout

class TestChairMenuSetup(TestCase):
    def setUp(self):
        models.myUser.objects.create(username="DoctorChair", password="DoctorChair", name="DocyC",
                                     usertype="chair", email="chair@email.com", assignedInstructor=0)


class TestChairMenu(TestChairMenuSetup):
    def test_add_ta(self):
        c = django.test.Client()
        c.post('/', {'username':'DoctorChair', 'pass':'DoctorChair'})
        resp = c.get('/addUser')
        self.assertRedirects(resp, '/addUser/', status_code=301, target_status_code=200, msg_prefix='', fetch_redirect_response=True)

    def test_add_course(self):
        c = django.test.Client()
        c.post('/', {'username': 'DoctorChair', 'pass': 'DoctorChair'})
        resp = c.get('/addCourse')
        self.assertRedirects(resp, '/addCourse/', status_code=301, target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)

    def test_ve_tas(self):
        c = django.test.Client()
        c.post('/', {'username': 'DoctorChair', 'pass': 'DoctorChair'})
        resp = c.get('/viewUsers')
        self.assertRedirects(resp, '/viewUsers/', status_code=301, target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)

    def test_ve_courses(self):
        c = django.test.Client()
        c.post('/', {'username': 'DoctorChair', 'pass': 'DoctorChair'})
        resp = c.get('/viewCourse')
        self.assertRedirects(resp, '/viewCourse/', status_code=301, target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)


    # app.command("") denotes enter
    def test_assign_ta(self):
        c = django.test.Client()
        c.post('/', {'username': 'DoctorChair', 'pass': 'DoctorChair'})
        resp = c.get('/chair_assignToCourse')
        self.assertRedirects(resp, '/chair_assignToCourse/', status_code=301, target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)

    def test_validate(self):
        c = django.test.Client()
        c.post('/', {'username': 'DoctorChair', 'pass': 'DoctorChair'})
        resp = c.get('/validate')
        self.assertRedirects(resp, '/validate/', status_code=301, target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)

    def test_logout(self):
        c = django.test.Client()
        c.post('/', {'username': 'DoctorChair', 'pass': 'DoctorChair'})
        resp = c.get('/logout')
        self.assertRedirects(resp, '/logout/', status_code=301, target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)


class testChairMenuNoUserLoggedIn(TestChairMenuSetup):
    def test_add_ta(self):
        c = django.test.Client()
        resp = c.get('/addUser', follow=True)
        self.assertRedirects(resp, '/logout/', status_code=301, target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)

    def test_menu_NoLoggin(self):
        c = django.test.Client()
        resp = c.get('/menu', follow=True)
        self.assertRedirects(resp, '/logout/', status_code=301, target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)

    def test_add_course(self):
        c = django.test.Client()
        resp = c.get('/addCourse', follow=True)
        self.assertRedirects(resp, '/logout/', status_code=301, target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)

    def test_ve_tas(self):
        c = django.test.Client()
        resp = c.get('/viewUsers', follow=True)
        self.assertRedirects(resp, '/logout/', status_code=301, target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)

    def test_ve_courses(self):
        c = django.test.Client()
        resp = c.get('/viewCourse', follow=True)
        self.assertRedirects(resp, '/logout/', status_code=301, target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)



    def test_assign_ta(self):
        c = django.test.Client()
        resp = c.get('/chair_assignToCourse', follow=True)
        self.assertRedirects(resp, '/logout/', status_code=301, target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)

    def test_validate(self):
        c = django.test.Client()
        resp = c.get('/validate', follow=True)
        self.assertRedirects(resp, '/logout/', status_code=301, target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)

    def test_logout(self):
        c = django.test.Client()
        resp = c.get('/logout')
        self.assertRedirects(resp, '/logout/', status_code=301, target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)


# we probably also want tests for TA and Instructor trying to access chair stuff.