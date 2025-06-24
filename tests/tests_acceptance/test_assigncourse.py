from django.test import TestCase, Client
from ta_app import models

#this will happen when the Assign Instructor or Assign TA command is chosen from the menu.
#we'll
class testChairAssignSetup(TestCase):
    def setUp(self):
        models.myUser.objects.create(username="DoctorChair", password="DoctorChair", name="DocyC",
                                     usertype="chair", email="chair@email.com", assignedInstructor=0)
        models.Course.objects.create(course_name='CS 361, Software Engineering', tues_flag=True, thurs_flag=True, start_time='11:00:00',
                                     end_time='11:50:00', coursetype='Lecture')
        models.myUser.objects.create(username="RegularTa", password="defaultPassword", name="Jannis",
                                     usertype="ta", email="ta@email.com", assignedInstructor=0)
        models.myUser.objects.create(username="MarvinTa", password="defaultPassword", name="Marvin",
                                     usertype="ta", email="ta2@email.com", assignedInstructor=0)
        models.myUser.objects.create(username="ProffessorInstructor", password="defaultPassword", name="Dan",
                                     usertype="instructor", email="inst@email.com", assignedInstructor=0)
        #jannis is 2, Marvin is 3, Dan is 4, (chair is 1)
        #there is only 1 course, it is 1

#format of assigning courses will be "Assign <Instructor Name> to <Course Name>"
class testChairAssign(testChairAssignSetup):
    def testAssignTa(self):
        c = Client()
        c.post("/", {'username': 'DoctorChair', 'pass': 'DoctorChair'})
        resp = c.post("/chair_assignToCourse/", {'availableUsers':2, 'availableCourses':1})
        self.assertEquals(resp.context.get("message"), "Assignment successful")

    def testAssignInstructor(self):
        c = Client()
        c.post("/", {'username': 'DoctorChair', 'pass': 'DoctorChair'})
        resp = c.post("/chair_assignToCourse/", {'availableUsers':4, 'availableCourses':1})
        self.assertEquals(resp.context.get("message"), "Assignment successful")
#        chair.addInstructor(Inst.Rock)
#        self.assertEquals(app.command("Assign Jason Rock to CS361"), "Assigned Instructor Jason Rock to CS361")

    def testAssignTA2(self):
        c = Client()
        c.post("/", {'username': 'DoctorChair', 'pass': 'DoctorChair'})
        resp = c.post("/chair_assignToCourse/",
                      {'availableUsers': 2, 'availableCourses': 1})
        self.assertEquals(resp.context.get("message"), "Assignment successful")
        resp = c.post("/chair_assignToCourse/",
                      {'availableUsers': 3, 'availableCourses': 1})
        self.assertEquals(resp.context.get("message"), "Assignment successful")

    #       #app.command("back")
        #app.comand("Assign TA")
        #self.assertEquals(app.command("Assign Laura Crumpo to CS361"), raise ValueError("No TAs to assign to course"))

    def testAssignAll3(self):
        c = Client()
        c.post("/", {'username': 'DoctorChair', 'pass': 'DoctorChair'})
        resp = c.post("/chair_assignToCourse/", {'availableUsers': 2, 'availableCourses': 1})
        self.assertEquals(resp.context.get("message"), "Assignment successful")
        resp = c.post("/chair_assignToCourse/", {'availableUsers':3, 'availableCourses':1})
        self.assertEquals(resp.context.get("message"), "Assignment successful")
        resp = c.post("/chair_assignToCourse/", {"availableUsers":4,'availableCourses':1 })
        self.assertEquals(resp.context.get("message"), "Assignment successful")