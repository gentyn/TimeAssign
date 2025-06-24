from django.db import models


# Create your models here.
class Super(models.Model):
    name = models.CharField(max_length=20)

#legacy code, we do not need this anymore
class inputHandler:
    name = models.CharField(max_length=1)

class myUser(models.Model):
    username = models.CharField(max_length=50, default='NewUser')
    password = models.CharField(max_length=20, default='password')
    name = models.CharField(max_length=50, default='NewName')
    usertype = models.CharField(max_length=10, default='ta')
    email = models.EmailField(max_length=50, default='newUser@email.com')
    assignedInstructor = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return 'UserID = %s, Username = %s, Name = %s UserType = %s  Email = %s' % (self.id,
            self.username, self.name, self.usertype, self.email)

#Added 5 new fields (coursetype, lectureid, ta1, ta2, ta3, ta4)
#essentially "ta" should be replaced by "ta1"

class Course(models.Model):
    LECTURE = 'LEC'
    LAB = 'LAB'
    ONLINE = 'ON'
    GRADING = 'GRD'
    typesOfCourses = [
        (LECTURE, 'Lecture'),
        (LAB, 'Lab'),
        (ONLINE, 'Online'),
        (GRADING, 'Grading'),
    ]
    course_name = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()

    mon_flag = models.BooleanField(default=False)
    tues_flag = models.BooleanField(default=False)
    wed_flag = models.BooleanField(default=False)
    thurs_flag = models.BooleanField(default=False)
    fri_flag = models.BooleanField(default=False)
    sat_flag = models.BooleanField(default=False)

    coursetype = models.CharField(max_length=3, choices=typesOfCourses, default=LECTURE)
    lectureid = models.IntegerField(null=True, blank=True, default=0) #default to 0 if its a lecture, stores lecture id if its a lab
    ta = models.IntegerField(null=True, blank=True, default=0) #TODO do we still want this field? I could see it getting confusing
    ta1 = models.IntegerField(null=True, blank=True, default=0)
    ta2 = models.IntegerField(null=True, blank=True, default=0)
    ta3 = models.IntegerField(null=True, blank=True, default=0)
    ta4 = models.IntegerField(null=True, blank=True, default=0)
    instructor = models.IntegerField(null=True, blank=True, default=0)  # we allow nulls here, because maybe these things are not assigned yet.

    def __str__(self):
        return 'CourseID = %s, CourseName = %s, Instructor = %s, Coursetype = %s, lectureid = %s, ta = %s, ta1 = %s, ta2 = %s, ta3 = %s, ta4 = %s' \
               % (self.id,self.course_name, self.instructor, self.coursetype, self.lectureid, self.ta, self.ta1, self.ta2, self.ta3, self.ta4)


class Break(models.Model):
    break_name = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()

    mon_flag = models.BooleanField(default=False)
    tues_flag = models.BooleanField(default=False)
    wed_flag = models.BooleanField(default=False)
    thurs_flag = models.BooleanField(default=False)
    fri_flag = models.BooleanField(default=False)
    sat_flag = models.BooleanField(default=False)
    userid = models.IntegerField(null=True, blank=True, default=0)
