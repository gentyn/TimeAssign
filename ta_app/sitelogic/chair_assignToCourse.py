# Chair will be able ossign TA's and Instructers to a lecture

from ta_app import models

# populateUsers will take the session user id and return all users
# that can be assigned by the user with that id
def populateUsers(thisUser):
    try:
        fullUser = models.myUser.objects.get(id=thisUser)
        if (fullUser.usertype == "chair"):
            ret = models.myUser.objects.all().exclude(usertype="chair")
        else:
            ret = []
        return ret
    except models.myUser.DoesNotExist:
        return "Error"

# populateUsers will take the session user id and return all courses
# that can be assigned to by the user with that id
def populateCourses(thisUser):
    try:
        fullUser = models.myUser.objects.get(id=thisUser)
        if (fullUser.usertype == "chair"):
            courselist = models.Course.objects.all().filter(coursetype='LEC')
            ret = id_to_name(courselist)
        else:
            ret = []
        print(ret)
        return ret
    except models.myUser.DoesNotExist:
        return "Error"

def id_to_name(courselist):
    for i in courselist:
        if not (i.ta1 == 0):
            full_ta = models.myUser.objects.get(id=i.ta1)
            i.ta1 = full_ta.name
        if not (i.ta2 == 0):
            full_ta = models.myUser.objects.get(id=i.ta2)
            i.ta2 = full_ta.name
        if not (i.ta3 == 0):
            full_ta = models.myUser.objects.get(id=i.ta3)
            i.ta3 = full_ta.name
        if not (i.ta4 == 0):
            full_ta = models.myUser.objects.get(id=i.ta4)
            i.ta4 = full_ta.name
        if not (i.instructor == 0):
            full_ta = models.myUser.objects.get(id=i.instructor)
            i.instructor = full_ta.name

    return courselist

# makeAssignment will take the selected user & course ids, find the type
# for the selected user, then update the appropriate value (ta or instructor)
# of the selected course to the selected user
def makeAssignment(thisUser, user, course):
    print(user)
    print(course)
    ret = False
    if not localVerify(thisUser, user, course):
        print(False)
        ret = False
    else:
        luser = models.myUser.objects.get(id=user)
        lcourse = models.Course.objects.get(id=course)
        if (luser is not None) and (lcourse is not None):
            if luser.usertype == "ta":
                ret = assignTA(luser,lcourse)
            elif luser.usertype == "instructor":
                lcourse.instructor = luser.id
                lcourse.save()
                ret = True
        else:
            ret = False
    return ret

def assignTA(user, course):
    #check if user is already assigned as a ta
    uid = user.id

    if(course.ta1 == uid or course.ta2 == uid or course.ta3 == uid or course.ta4 == uid):
        return False

    ret = True

    if course.ta1 == 0:
        course.ta1 = user.id
    elif course.ta2 == 0:
        course.ta2 = user.id
    elif course.ta3 == 0:
        course.ta3 = user.id
    elif course.ta4 == 0:
        course.ta4 = user.id
    else:
        ret = False

    course.save()

    return ret


# localVerify will make sure everything on the post request is kosher
def localVerify(thisUser, user, course):
    fullUser = models.myUser.objects.get(id=thisUser)
    if (user is None) or (course is None):
        ret = False
    elif (fullUser.usertype == "chair"):
        #if models.myUser.objects.get(name=user).usertype == "chair":
        #    return False
        #if not (models.Course.objects.get(course_name=course).coursetype == 0):
        #    return False

        ret = True

    elif (fullUser.usertype == "instructor"):
        ta = models.myUser.objects.get(id=user)
        course = models.Course.objects.get(id=course)
        ret = (course.instructor == thisUser)
    else:
        ret = False
    return ret