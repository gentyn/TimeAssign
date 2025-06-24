

from ta_app import models

# PopulateInstructor will take the session id and return all the users with usertype as Instructor
# that can be assigned by
def populateinstructor(thisUser):
    fullUser = models.myUser.objects.get(id=thisUser)
    if (fullUser.usertype == "chair"):
        ret = models.myUser.objects.all().filter(usertype='Instructor')
    else:
        ret = []

    return ret

# PopulateInstructor will take the session id and return all the users with usertype as TA
    # that can be assigned by
def populateta(thisUser):

    fullUser = models.myUser.objects.get(id=thisUser)

    if (fullUser.usertype == "chair"):
        ret = models.myUser.objects.all().filter(usertype="TA")
    else:
        ret = []

    return ret

    # AssignInstructor will take the selected Instructor and TA used id
    # and update the appropriate value of the selected Instructor to the selected TA
def makeAssignment(thisUser, Ins, TA):
    if not validate(thisUser, Ins, TA):
        ret = False
    else:
        assignee = models.myUser.objects.get(id=TA)
        assigned = models.myUser.objects.get(id=Ins)
        assignee.assignedInstructor = assigned.id
        assignee.save()
        ret = True
    return ret

    # Validate will return true if the assignment is valid otherwise false
def validate(thisUser, Ins, TA):

    #return True

    if (TA == None) or (Ins == None):
        ret = False

    assignee = models.myUser.objects.all().get(id=TA)
    assigned = models.myUser.objects.get(id=Ins)

    if ( not assignee.usertype == "TA"):
        print(assignee.usertype)
        ret = False
    elif (not assigned.usertype == "Instructor"):
        ret = False
    else:
        ret = True

    return ret

