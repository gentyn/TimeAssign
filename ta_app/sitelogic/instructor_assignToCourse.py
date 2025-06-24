# Chair will be able ossign TA's and Instructers to a lecture

from ta_app import models

# populateUsers will take the session user id and return all users
# that can be assigned by the user with that id

# this function will return all the TA's assigned to the all the Instructor's courses.
def populateUsers(thisUser):
    fullUser = models.myUser.objects.get(id=thisUser)
    #if (fullUser.usertype == "chair"):
    #    ret = models.myUser.objects.all().exclude(usertype="chair")

    currentcourses = models.Course.objects.all().filter(instructor=thisUser)
    talist = []
    tas = ["ta1","ta2","ta3","ta4"]
    for i in currentcourses:
        #print(models.myUser.objects.all().filter(id=i.ta1))
        #print(models.myUser.objects.all().filter(id=i.ta1))

        if not (i.ta1 == 0):
            talist.extend(models.myUser.objects.all().filter(id=i.ta1))
        if not (i.ta2 == 0):
            talist.extend(models.myUser.objects.all().filter(id=i.ta2))
        if not (i.ta3 == 0):
            talist.extend(models.myUser.objects.all().filter(id=i.ta3))
        if not (i.ta4 == 0):
            talist.extend(models.myUser.objects.all().filter(id=i.ta4))

    return talist

# populateUsers will take the session user id and return all courses
# that can be assigned to by the user with that id
def populateCourses(thisUser):
    #fullUser = models.myUser.objects.get(id=thisUser)
    #if (fullUser.usertype == "chair"):
    #    ret = models.Course.objects.all()
    currentcourses = models.Course.objects.all().filter(instructor=thisUser)
    courselist = []

    for i in currentcourses:
        print(i)
        courselist.extend(models.Course.objects.all().filter(lectureid=i.id))

    ret = id_to_name(courselist)

    return ret

def id_to_name(courselist):
    for i in courselist:
        ta_id = i.ta1
        if not (ta_id == 0):
            full_ta = models.myUser.objects.get(id=ta_id)
            i.ta1 = full_ta.name
        if not (i.instructor == 0):
            full_ta = models.myUser.objects.get(id=i.instructor)
            i.instructor = full_ta.name

    return courselist


# makeAssignment will take the selected user & course ids, find the type
# for the selected user, then update the appropriate value (ta or instructor)
# of the selected course to the selected user
def makeAssignment(thisUser, user, course):
    if not localVerify(thisUser, user, course):
        ret = False
    else:
        luser = models.myUser.objects.get(id=user)
        lcourse = models.Course.objects.get(id=course)
        if (luser is not None) and (lcourse is not None):
            if luser.usertype == "ta":
                lcourse.ta1 = luser.id
                lcourse.save()
            ret = True
        else:
            ret = False
    return ret

# localVerify will make sure everything on the post request is kosher
def localVerify(thisUser, user, course):
    fullUser = models.myUser.objects.get(id=thisUser)
    if (user is None) or (course is None):
        ret = False
    elif (fullUser.usertype == "instructor"):
        #course = models.Course.objects.get(course_name=course)
        #ret = (course.instuctor == thisUser)
        ret = True
    else:
        ret = False
    return ret