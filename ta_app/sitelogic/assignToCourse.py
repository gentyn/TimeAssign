from ta_app import models

# populateUsers will take the session user id and return all users
# that can be assigned by the user with that id
def populateUsers(thisUser):
    try:
        fullUser = models.myUser.objects.get(id=thisUser)
        if (fullUser.usertype == "chair"):
            ret = models.myUser.objects.all().exclude(usertype="chair")
        elif (fullUser.usertype == "instructor"):
            ret = models.myUser.objects.all().filter(assignedInstructor=thisUser)
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
            ret = models.Course.objects.all()
        elif (fullUser.usertype == "instructor"):
            ret = models.Course.objects.all().filter(instructor=thisUser)
        else:
            ret = []
        return ret
    except models.myUser.DoesNotExist:
        return "Error"


# makeAssignment will take the selected user & course ids, find the type
# for the selected user, then update the appropriate value (ta or instructor)
# of the selected course to the selected user
def makeAssignment(thisUser, user, course):
    if not localVerify(thisUser, user, course):
        ret = False
    else:
        assignee = models.myUser.objects.get(name=user)
        assigned = models.Course.objects.get(course_name=course)
        if (assignee is not None) and (assigned is not None):
            if assignee.usertype == "ta":
                assigned.ta = assignee.id
            else:
                assigned.instructor = assignee.id
            assigned.save()
            ret = True
        else:
            ret = False
    return ret

# localVerify will make sure everything on the post request is kosher
def localVerify(thisUser, user, course):
    fullUser = models.myUser.objects.get(id=thisUser)
    if (user is None) or (course is None):
        ret = False
    elif (fullUser.usertype == "chair"):
        ret = True
    elif (fullUser.usertype == "instructor"):
        ta = models.myUser.objects.get(name=user)
        course = models.Course.objects.get(course_name=course)
        ret = (ta.assignedInstructor == thisUser) and (course.instuctor == thisUser)
    else:
        ret = False
    return ret