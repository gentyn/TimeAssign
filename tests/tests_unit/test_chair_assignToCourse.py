from _ast import mod

from django.test import TestCase
from ta_app import models
from ta_app.sitelogic import chair_assignToCourse
import datetime

class TestAssignToCourse(TestCase):
    def setUp(self):
        data1 = models.myUser(username="Chairzy", password="any", name="Chairzy",
                      usertype="chair", email="any@any.com")
        data1.id = 100
        data1.save()

        data2 = models.myUser(username="Instructo", password="any", name="Instructo",
                      usertype="instructor", email="any@any.com")
        data2.id = 200
        data2.save()

        data3 = models.myUser(username="Grad", password="any", name="Grad",
                             usertype="ta", email="any@any.com")
        data3.id = 300
        data3.save()

        data3 = models.myUser(username="Grad1", password="any", name="Grad1",
                              usertype="ta", email="any@any.com")
        data3.id = 400
        data3.save()

        data4 = models.Course(course_name="stuff1", start_time=datetime.time(00, 00),
                             end_time=datetime.time(1, 00), mon_flag=True, instructor=200, coursetype=0)
        data4.id = 100
        data4.save()

        data5 = models.Course(course_name="stuff2", start_time=datetime.time(00, 00),
                             end_time=datetime.time(1, 00), mon_flag=True, coursetype=0)
        data5.id = 200
        data5.save()

class TestPopulateUsers(TestAssignToCourse):
    def testChair(self):
        # the testing DB user with id 100 has type "Chair"
        self.assertEqual(list(chair_assignToCourse.populateUsers(100)), list(models.myUser.objects.all().exclude(usertype="chair")))

    def testInstructor(self):
        # the testing DB user with id 200 has type "Instructor"
        self.assertEqual(list(chair_assignToCourse.populateUsers(200)), [])

    def testTA(self):
        # the testing DB user with id 300 has type "TA"
        self.assertEqual(list(chair_assignToCourse.populateUsers(300)), [])

    def testBadArg(self):
        self.assertEqual("Error", chair_assignToCourse.populateUsers(1.5))

class TestPopulateCourses(TestAssignToCourse):
    def testChair(self):
        # the testing DB user with id 100 has type "Chair"
        self.assertEqual(list(chair_assignToCourse.populateCourses(100)), list(models.Course.objects.all().filter(coursetype="LEC")))

    def testInstructor(self):
        # the testing DB user with id 200 has type "Instructor"
        self.assertEqual(list(chair_assignToCourse.populateCourses(200)), [])

    def testTA(self):
        # the testing DB user with id 300 has type "TA"
        self.assertEqual(list(chair_assignToCourse.populateCourses(300)), [])

    def testBadArg(self):
        self.assertEqual("Error", chair_assignToCourse.populateCourses(1.5))

class TestMakeAssign(TestAssignToCourse):
    def testTA1(self):
        # the testing DB user with id 300 has type "TA", course with id 100 is has assigned instructor 200
        self.assertTrue(chair_assignToCourse.makeAssignment(200, 300, 100))
        self.assertEqual(300, models.Course.objects.get(id=100).ta1)

    def testTA2(self):
        # the testing DB user with id 300 has type "TA", course with id 100 is has assigned instructor 200
        self.assertTrue(chair_assignToCourse.makeAssignment(200, 300, 100))
        self.assertEqual(300, models.Course.objects.get(id=100).ta1)
        self.assertTrue(chair_assignToCourse.makeAssignment(200, 400, 100))
        self.assertEqual(400, models.Course.objects.get(id=100).ta2)

    def testduplicateassignments(self):
        # the testing DB user with id 300 has type "TA", course with id 100 is has assigned instructor 200
        self.assertTrue(chair_assignToCourse.makeAssignment(200, 300, 100))
        self.assertEqual(300, models.Course.objects.get(id=100).ta1)
        self.assertFalse(chair_assignToCourse.makeAssignment(200, 300, 100))

    def testInstruct(self):
        self.assertTrue(chair_assignToCourse.makeAssignment(100, 200, 200))
        self.assertEqual(200, models.Course.objects.get(id=200).instructor)

    def testBad(self):
        self.assertFalse(chair_assignToCourse.makeAssignment(300, 100, 100))
        self.assertEqual(200, models.Course.objects.get(id=100).instructor)
        self.assertEqual(0, models.Course.objects.get(id=100).ta)

class TestLocalVerify(TestAssignToCourse):
    def testGoodChair(self):
        self.assertTrue(chair_assignToCourse.localVerify(100, 200, 200))

    def testGoodInstruct(self):
        self.assertTrue(chair_assignToCourse.localVerify(200, 400, 100))

    def testBadTA(self):
        self.assertTrue(chair_assignToCourse.localVerify(200, 100, 100))

    def testBadCourse(self):
        self.assertFalse(chair_assignToCourse.localVerify(200, 300, 200))

    def testBadBoth(self):
        self.assertFalse(chair_assignToCourse.localVerify(200, 100, 200))

    def testTA(self):
        self.assertFalse(chair_assignToCourse.localVerify(300, 100, 100))