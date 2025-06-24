from django.test import TestCase
from ta_app import models
from ta_app.sitelogic import assignToCourse
import datetime

class TestAssignToCourse(TestCase):
    def setUp(self):
        data1 = models.myUser(username="Chairzy", password="any", name="Chairzy",
                      usertype="chair", email="any@any.com")
        data1.id = 100
        data1.save()

        data2 = models.myUser(username="Instructor", password="any", name="Instructo",
                      usertype="instructor", email="any@any.com")
        data2.id = 200
        data2.save()

        data3 = models.myUser(username="Grad", password="any", name="Grad",
                             usertype="ta", email="any@any.com", assignedInstructor=2)
        data3.id = 300
        data3.save()

        data4 = models.Course(course_name="stuff1", start_time=datetime.time(00, 00),
                             end_time=datetime.time(1, 00), mon_flag=True, instructor=200)
        data4.id = 100
        data4.save()

        data5 = models.Course(course_name="stuff2", start_time=datetime.time(00, 00),
                             end_time=datetime.time(1, 00), mon_flag=True)
        data5.id = 200
        data5.save()

class TestPopulateUsers(TestAssignToCourse):
    def testChair(self):
        # the testing DB user with id 100 has type "Chair"
        self.assertEqual(list(assignToCourse.populateUsers(100)), list(models.myUser.objects.all().exclude(usertype="chair")))

    def testInstructor(self):
        # the testing DB user with id 200 has type "Instructor"
        self.assertEqual(list(assignToCourse.populateUsers(200)), list(models.myUser.objects.all().filter(assignedInstructor=200)))

    def testTA(self):
        # the testing DB user with id 300 has type "TA"
        self.assertEqual(list(assignToCourse.populateUsers(300)), [])

    def testBadArg(self):
        self.assertEqual("Error", assignToCourse.populateUsers(1.5))

class TestPopulateCourses(TestAssignToCourse):
    def testChair(self):
        # the testing DB user with id 100 has type "Chair"
        self.assertEqual(list(assignToCourse.populateCourses(100)), list(models.Course.objects.all()))

    def testInstructor(self):
        # the testing DB user with id 200 has type "Instructor"
        self.assertEqual(list(assignToCourse.populateCourses(200)), list(models.Course.objects.all().filter(instructor=200)))

    def testTA(self):
        # the testing DB user with id 300 has type "TA"
        self.assertEqual(list(assignToCourse.populateCourses(300)), [])

    def testBadArg(self):
        self.assertRaises(TypeError, assignToCourse.populateCourses(1.5))

class TestMakeAssign(TestAssignToCourse):
    def testTA(self):
        # the testing DB user with id 300 has type "TA", course with id 100 is has assigned instructor 200
        self.assertFalse(assignToCourse.makeAssignment(200, "Grad", "stuff1"))
        self.assertEqual(300, models.Course.objects.get(id=100).ta1)

    def testInstruct(self):
        self.assertTrue(assignToCourse.makeAssignment(100, "Instructor", "stuff2"))
        self.assertEqual(200, models.Course.objects.get(id=200).instructor)

    def testBad(self):
        self.assertFalse(assignToCourse.makeAssignment(300, "Chairzy", "stuff1"))
        self.assertEqual(200, models.Course.objects.get(id=100).instructor)
        self.assertEqual(0, models.Course.objects.get(id=100).ta)

class TestLocalVerify(TestAssignToCourse):
    def testGoodChair(self):
        self.assertTrue(assignToCourse.localVerify(100, "Instructo", "stuff2"))

    def testGoodInstruct(self):
        self.assertFalse(assignToCourse.localVerify(200, "Grad", "stuff1"))

    def testBadTA(self):
        self.assertFalse(assignToCourse.localVerify(200, "Chairzy", "stuff1"))

    def testBadCourse(self):
        self.assertFalse(assignToCourse.localVerify(200, "Grad", "stuff2"))

    def testBadBoth(self):
        self.assertFalse(assignToCourse.localVerify(200, "Chairzy", "stuff2"))

    def testTA(self):
        self.assertFalse(assignToCourse.localVerify(300, "Chairzy", "stuff1"))