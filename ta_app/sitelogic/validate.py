from ta_app import models

#this is the topmost Validate function that determines
#who what labs we're validating based on the current
#user, then called validateLab() on each of those
#labs. It returns a list of conflicted labs.
#The scope of what is validated:
#Chair - all labs
#Instructor - all labs tied to that instructor's
#    lectures
#TA - all labs assigned to that TA
def validateScope(thisUser, userType):
    conflicts = []
    labs = models.Course.objects.all().filter(coursetype='LAB')
    if (userType != 'instructor'):
        if (userType == 'ta'):
            labs = list(labs.filter(ta1=thisUser))
        elif (userType == 'chair'):
            labs = list(labs)

        for currentLab in labs:
            if not validateLab(currentLab):
                conflicts.append(currentLab)
    else: #if instructor
        lectures = models.Course.objects.all().filter(instructor=thisUser)
        for lecture in lectures:
            labsForLecture = labs.filter(lectureid=(lecture.id))
            for currentLab in labsForLecture:
                if not validateLab(currentLab):
                    conflicts.append(currentLab)

    return conflicts


#This is an intermediate Validate function that
#finds the TA associated with the passed in lab,
#then calls validateEach() on each tied to that
#TA. It returns true if no conflict, false if
#there is a conflict
def validateLab(currentLab):
    breaks = models.Break.objects.all().filter(userid=(currentLab.ta1))
    valid = True

    for currentBreak in breaks:
        if not validateEach(currentLab, currentBreak):
            valid = False

    return valid

#This is the validate function that does the
#actual comparisons, looking at the passed in
#lab and break to see if they overlap. If they
#do, it returns false, otherwise return true.
def validateEach(currentLab, currentBreak):
    mon = currentLab.mon_flag and currentBreak.mon_flag
    tues = currentLab.tues_flag and currentBreak.tues_flag
    wed = currentLab.wed_flag and currentBreak.wed_flag
    thurs = currentLab.thurs_flag and currentBreak.thurs_flag
    fri = currentLab.fri_flag and currentBreak.fri_flag
    sat = currentLab.sat_flag and currentBreak.sat_flag

    valid = True

    if mon or tues or wed or thurs or fri or sat:
        lStart = currentLab.start_time
        lEnd = currentLab.end_time
        bStart = currentBreak.start_time
        bEnd = currentBreak.end_time

        overlapStart = bStart < lStart and lStart < bEnd
        overlapEnd = lStart < bStart and bStart < lEnd
        overlapWholeL = bStart < lStart and lEnd < bEnd
        overlapWholeB = lStart < bStart and bEnd < lEnd

        valid = not (overlapStart or overlapEnd or overlapWholeL or overlapWholeB)

    return valid