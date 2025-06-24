import django
from django.test import TestCase
from ta_app import models

class TestAddCourse(TestCase):
    def setUp(self):
        models.Course.objects.create(course_name='iAlreadyExist', start_time="10:00:00", end_time="10:50:00", mon_flag=True, wed_flag=True, fri_flag=True, coursetype='LEC')
        models.myUser.objects.create(username="DoctorChair", password="DoctorChair", name="DocyC",usertype="chair", email="chair@email.com", assignedInstructor=0)
        models.myUser.objects.create(username="iAlreadyExist", password="password", name="I Already",
                                     usertype="ta", email="ta@email.com", assignedInstructor=0)



class TestAddCourses(TestAddCourse):
  #assume course ialreadyexist already exists
    def test_reused_course(self):
        c = django.test.Client()
        c.post('/', {"username": "DoctorChair", "pass": "DoctorChair"})
        response = c.post('/addCourse/', {"Course Name":"iAlreadyExists", "startTime":"11:00:00", "endTime":"11:50:00","mon_flag":"True", "CourseType":"LEC","availablelectures" :"1"})
        #need to check if addCourse is still in the database here, since we have no confirmation messages, and that size is still 1
        self.assertEquals(response.context.get("message"), "A lecture cannot have another lecture assigned") # no message

    def test_good_format(self):
        c = django.test.Client()
        c.post('/', {"username": "DoctorChair", "pass": "DoctorChair"})
        response = c.post('/addCourse/',{"Course Name": "New Course", "startTime": "11:00:00", "endTime": "11:50:00","mon_flag":"True", "CourseType":"LEC","availablelectures" :"0"})
        self.assertEquals(response.context.get("message"), "Course Created")

    def test_bad_format_time(self):
        c = django.test.Client()
        c.post('/', {"username": "DoctorChair", "pass": "DoctorChair"})
        response = c.post('/addCourse/',{"Course Name": "New Course", "startTime": "3:00:00", "endTime": "2:50:00","availablelectures" :"0","CourseType":"LEC"})
        self.assertEquals(response.context.get("message"), "Invalid Format")

    def test_online(self):
        c = django.test.Client()
        c.post('/', {"username": "DoctorChair", "pass": "DoctorChair"})
        response = c.post('/addCourse/', {"Course Name": "New Course", "startTime": "13:00:00", "endTime": "13:00:00", #arbitrary time
                                          "day": "MWF", "CourseType":"ON","availablelectures" :"0"})
        self.assertEquals(response.context.get("message"), "Course Created")