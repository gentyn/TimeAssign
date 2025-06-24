from django.db import models
import datetime
import re
from ta_app import models


# Returns false if field is empty
def check_empty(field):
    if field is None or field == "":
        return False
    else:
        return True


def valid_time(field):
    if len(field) != 4 or not field.isdigit() \
            or not (0 <= int(field[0:2]) <= 23) or not (0 <= int(field[2:4]) <= 59):
        return False
    return True


class AddCourse:
    course_name = ""
    start_time = ""
    end_time = ""
    #days = ""
    instructor = ""
    ta = ""
    courseType = ""
    mon_flag = False
    tues_flag = False
    wed_flag = False
    thu_flag = False
    fri_flag = False
    sat_flag = False

    def __init__(self, course):
        self.course = course

    def addCourse(self, request):
        if check_empty(request.POST["Course Name"]):
            self.course_name = request.POST["Course Name"]
            monday = False
            tuesday = False
            wednesday = False
            thursday = False
            friday = False
            saturday = False
            if request.POST.get('M', False) == 'on':
                monday = True
            if request.POST.get('T', False) == 'on':
                tuesday = True
            if request.POST.get('W', False) == 'on':
                wednesday = True
            if request.POST.get('R', False) == 'on':
                thursday = True
            if request.POST.get('F', False) == 'on':
                friday = True
            if request.POST.get('S', False) == 'on':
                saturday = True
                #whoever designed this check box functionallity should be executed by firing squad.

            lid = request.POST['availablelectures']
            ctype = request.POST['CourseType']

            print(ctype)
            print(lid)

            if(ctype == 'LAB' and lid == 'LEC'):
                return "A lab must be assinged to a lecture"

            if(ctype == 'LEC' and not(lid == '0')):
                return "A lecture cannot have another lecture assigned"

            models.Course.objects.create(course_name=request.POST["Course Name"], start_time=request.POST['startTime'],
                                         end_time=request.POST['endTime'], mon_flag=monday, tues_flag=tuesday, wed_flag=wednesday, thurs_flag=thursday,
                                         fri_flag=friday, sat_flag=saturday, coursetype=request.POST['CourseType'],
                                         lectureid=request.POST['availablelectures'])
            return "Course Created"

        else:
            return "Invalid course name"
        #if valid_time(request.POST["startTime"]):
        #    self.start_time = datetime.time(request.POST["startTime"])
        #else:
        #    return "Invalid start time"
        #if valid_time(request.POST["endTime"]):
        #    self.end_time = datetime.time(request.POST["endTime"])
        #else:
        #    return "Invalid end time"
        #parseDayString = request.POST['day']
        #parseDayString = re.search('[M]?[T]?[W]?[R]?[F]?[S]?', parseDayString).group(0)
        #if parseDayString != "":
        #    self.days = parseDayString
        #else:
        #    return "Invalid day(s)"
        #if check_empty(request.POST['instructor']):
        #    self.instructor = request.POST['instructor']
        #else:
        #    self.instructor = None
        #if check_empty(request.POST['ta']):
        #    self.ta = request.POST['ta']
        #else:
        #    self.ta = None
        #try:
        #    models.Course.objects.get(course_name=self.course_name, start_time=self.start_time,
        #                              end_time=self.end_time, day=self.days) # we have no check for time because of formatting issues, to fix
        #    models.Course.objects.get(course_name=self.course_name, day=self.days)
        #    return "Course already exists"
        #except models.Course.DoesNotExist:
        #    models.Course.objects.create(
         #       course_name=self.course_name,
         #       start_time=self.start_time,
         #       end_time=self.end_time,
         #       day=self.days,
         #       instructor=self.instructor,
         #       ta=self.ta
         #   )
            return "Course created"

    def editCourse(self, request):
        if check_empty(request.POST["Course Name"]):
            self.course_name = request.POST["Course Name"]
            m = models.Course.objects.get(course_name=request.POST["Course Name"])
            m.start_time = request.POST["startTime"]
            m.end_time = request.POST["endTime"]
            monday = False
            tuesday = False
            wednesday = False
            thursday = False
            friday = False
            saturday = False
            if request.POST.get('M', False) == 'on':
                monday = True
            if request.POST.get('T', False) == 'on':
                tuesday = True
            if request.POST.get('W', False) == 'on':
                wednesday = True
            if request.POST.get('R', False) == 'on':
                thursday = True
            if request.POST.get('F', False) == 'on':
                friday = True
            if request.POST.get('S', False) == 'on':
                saturday = True
            m.mon_flag = monday
            m.tues_flag = tuesday
            m.wed_flag = wednesday
            m.thurs_flag = thursday
            m.fri_flag = friday
            m.sat_flag = saturday
            m.mon_flag = self.mon_flag
            m.tues_flag = self.tues_flag
            m.wed_flag = self.wed_flag
            m.thurs_flag = self.thu_flag
            m.fri_flag = self.fri_flag
            m.sat_flag = self.sat_flag

            #m.day = request.POST["day"]
            #self.enter_days(m.day)
            #m.day = self.days
            m.instructor = request.POST["instructor"]
            m.ta1 = request.POST["ta"]
            if m.start_time == "" or m.end_time == "" or m.instructor == "" or m.ta == "":
                return "Empty Field"
            else:
                m.save()
                return "Course Edited"
        else:
            return "Invalid course name"

    # Add uses the name of a course, start time,
    # end time, days of the week, instructor (optional), and ta (optional)
    # and adds it to the database
    def add(self):
        models.Course.objects.create(
            course_name=self.course_name,
            start_time=self.start_time,
            end_time=self.end_time,
            days=self.days,
            instructor=self.instructor,
            ta=self.ta
        )

    # Remove takes in the name of a course, start time,
    # end time, days of the week, and removes it from the database
    def remove(self, course_name, start_time, end_time, days):
        models.Course.objects.remove(
            course_name=course_name,
            start_time=start_time,
            end_time=end_time,
            days=days
        )

    # Resets values of course
    def clear_values(self):
        self.course_name = ""
        self.start_time = ""
        self.end_time = ""
        self.days = ""
        self.instructor = ""
        self.ta = ""

    def command(self, str):
        if self.course_name == "":
            return self.enter_name(str[1])
        elif self.start_time == "":
            return self.enter_start_time(str[2])
        elif self.end_time == "":
            return self.enter_end_time(str[3])
        elif self.days == "":
            return self.enter_days(str[4])
        elif self.instructor == "":
            return self.enter_instructor(str[5])
        elif self.ta == "":
            return self.enter_ta(str[6])

    def enter_name(self, str):
        if check_empty(str):
            self.course_name = str
            return
        return "Enter course name again"

    def enter_start_time(self, str):
        if valid_time(str):
            self.start_time = time(int(str[0:2]), int(str[2:4]))
            return
        return "Enter start time again"

    def enter_end_time(self, str):
        if valid_time(str):
            self.end_time = time(int(str[0:2]), int(str[2:4]))
            return
        return "Enter end time again"

    def enter_days(self, str):
        str = re.search('[M]?[T]?[W]?[R]?[F]?[S]?', str).group(0)
        if str != "":
            self.days = str
            return
        return "Enter days again"

    def enter_instructor(self, str):
        if check_empty(str):
            self.instructor = str
        else:
            self.instructor = None

    def enter_ta(self, str):
        if check_empty(str):
            self.ta = str
        else:
            self.ta = None

    def populate_lectures(self):
        return models.Course.objects.all().filter(coursetype='LEC')

    #        valid = False
    #        while not valid:
    # Django output "Course Name: "
    #            valid_name = False
    #            while not valid_name:
    #                print("Course Name: ")  # TODO remove
    #                read = input()  # TODO Django input
    #                if check_empty(read):
    #                    valid_name = True
    #                    course_name = read

    # Django output "Start Time: "
    #            valid_start = False
    #            while not valid_start:
    #                print("Start Time: ")  # TODO remove
    #                read = input()  # TODO Django input
    #                if valid_time(read):
    #                    valid_start = True
    #                    start_time = time(int(read[0:2]), int(read[2:4]))

    #            # Django output "End Time: "
    #            valid_end = False
    #            while not valid_end:
    #                print("End Time: ")  # TODO remove
    #                read = input()  # TODO Django input
    #                if valid_time(read):
    #                    valid_end = True
    #                   start_time = time(int(read[0:2]), int(read[2:4]))

    # Django output "Days: "
    #            valid_days = False
    #            while not valid_days:
    #                print("Days: ")  # TODO remove
    #                read = input()  # TODO Django input
    #                read = re.search('[M]?[T]?[W]?[R]?[F]?[S]?', read).group(0)
    #                if read != "":
    #                    valid_days = True
    #                    days = read
    #
    #            # Django output "Instructor: "
    #            print("Instructor: ")  # TODO remove
    #            read = input()  # TODO Django input
    #            if check_empty(read):
    #                instructor = read
    #            else:
    #                instructor = None

    #            # Django output "TA: "
    #            print("TA: ")  # TODO remove
    #            read = input()  # TODO Django input
    #            if check_empty(read):
    #                ta = read
    #            else:
    #                ta = None
    #
    #            # Checks if course already exists, if not it is created
    #            if not Course.objects.get(course_name=course_name, start_time=start_time, end_time=end_time, days=days):
    #                self.add(course_name, start_time, end_time, days, instructor, ta)
    #               return True
    #            # Django output "Course already exists!"

    # Add TA to course
    # TA is of type User
    def add_ta(self):
        pass

    # Get TA from course
    # TA is of type User
    def get_ta(self):
        pass

    # Remove TA from course
    # TA is of type User
    def remove_ta(self):
        pass

    # Add instructor to course
    # Instructor is of type User
    def add_instructor(self):
        pass

    # Get instructor from course
    # Instructor is of type User
    def get_instructor(self):
        pass

    # Remove Instructor from course
    # Instructor is of type User
    def remove_instructor(self):
        pass

# ta = property(get_ta(),add_ta(),remove_ta())
# instructor = property(get_instructor(),add_instructor(),remove_instructor())
