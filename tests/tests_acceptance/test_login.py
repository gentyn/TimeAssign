import django.test
from ta_app import models

#Acceptance tests for PBIs "Chair can login"
# and "TA's and instructors can login"
#There are no specific tests for the two different stories, since login
#should be agnostic to user type

class TestLogin(django.test.TestCase):
	def setUp(self):
		models.myUser.objects.create(username="DoctorChair", password="DoctorChair", name="DocyC",
									 usertype="chair", email="chair@email.com", assignedInstructor=0)


class TestLoginScreen(TestLogin):
	def test_bad_username(self): #Test for invalid username, with good password
		c = django.test.Client()
		resp = c.post("/", {'username':'BadUser', 'pass':'DoctorChair'})
		self.assertEquals(resp.context.get("message"), "Login Failed")


	def test_validate_noone(self): #Test for no username entered
		#self.assertEqual(app.command(""), "")
		c = django.test.Client()
		resp = c.post("/", {'username':'', 'pass':'DoctorChair'})
		self.assertEquals(resp.context.get("message"), "Login Failed")

	def test_good_username(self): #Test for valid username
		#self.assertEqual(app.command("DefaultChair"), "Password:")
		c = django.test.Client()
		resp = c.post("/", {'username':'DoctorChair', 'pass':''})
		self.assertEquals(resp.context.get("message"), "Login Failed") #Login Failed

	def test_validate_noPW(self): #Valid user, no password entered
		c = django.test.Client()
		resp = c.post("/", {'username':'DoctorChair', 'pass':''})
		self.assertEquals(resp.context.get("message"), "Login Failed") #Login Failed

	def test_bad_PW(self): #Valid user, invalid password
		c = django.test.Client()
		resp = c.post("/", {'username':'DoctorChair', 'pass':'badPass'})
		self.assertEquals(resp.context.get("message"), "Login Failed") #Login Failed

	def test_good_PW(self): #Valid user & password
		c = django.test.Client()
		resp = c.post("/", {'username':'DoctorChair', 'pass':'DoctorChair'})
		self.assertRedirects(resp, '/menu/')