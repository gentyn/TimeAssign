import django.test
from ta_app import models

class TestAddUser(django.test.TestCase):
	def setUp(self):
		models.myUser.objects.create(username="iAlreadyExist", password="password", name="I Already",
									 usertype="ta", email="ta@email.com", assignedInstructor=0)
		models.myUser.objects.create(username="DoctorChair", password="DoctorChair", name="DocyC",
									 usertype="chair", email="chair@email.com", assignedInstructor=0)

#so now we need to write tests for not being logged in, and being logged in.
#which is good, we'll have more tests.

class TestAddUsers(TestAddUser):
	def test_reused_username(self):
		c= django.test.Client()
		c.post('/',{"username": "DoctorChair", "pass": "DoctorChair"})
		resp = c.post('/addUser/', {"username":"iAlreadyExist"})
		self.assertEquals(resp.context.get("message"), "User Already Exist, try adding a different username")


	def test_good_format_TA(self):
		c = django.test.Client()
		c.post('/',{"username": "DoctorChair", "pass": "DoctorChair"})
		resp = c.post('/addUser/', {"username": "Dillion3", "email":"Dillion@email.com", "realName":"Dillion Pogarth", "pass":"password", "usertype":"ta"})
		self.assertEquals(resp.context.get("message"), "Created User")


	def test_good_format_Inst(self): # correctly created user
		c = django.test.Client()
		c.post('/', {"username": "DoctorChair", "pass": "DoctorChair"})
		resp = c.post('/addUser/', {"username":"RegularInstructor", "pass":"defaultPassword", "realName":"Dan",
                                     "usertype":"instructor", "email":"ta@email.com"})
		self.assertEquals(resp.context.get("message"), "Created User")

'''	def test_not_Logged_in(self): # no user logged in
		c = django.test.Client()
		resp = c.post('/addUser/', {"username":"RegularInstructor", "password":"defaultPassword", "name":"Dan", "usertype":"instructor", "email":"ta@email.com"})
		self.assertEquals(resp.context.get("message"), "no user logged in")


	def test_not_chair(self): # user is logged in, but not a chair user
		c = django.test.Client()
		c.post('/', {"username": "iAlreadyExist", "pass":"password"})
		resp = c.post('/addUser/', {"username": "RegularInstructor", "pass": "defaultPassword", "realName": "Dan",
									"usertype": "instructor", "email": "ta@email.com"})
		self.assertEquals(resp.context.get("message"), "Not chair User")
		
These 2 tests are accounted for in other tests		
		'''