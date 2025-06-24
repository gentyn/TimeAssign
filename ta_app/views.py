from django.shortcuts import render, redirect
from django.views import View
from ta_app.sitelogic import login, addUser, assignToInstructor, addCourse
from ta_app.sitelogic import logout, menu
from ta_app.sitelogic import chair_assignToCourse, instructor_assignToCourse
from ta_app.sitelogic import validate
from ta_app.sitelogic import createBreak
from ta_app.models import inputHandler, myUser, Course, Break


# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'main/index.html')

    def post(self, request):
        loginInstrance = login.myUserLogin()
        loginString = loginInstrance.loginCheck(request)
        if loginString == "Logged In":
            return redirect('/menu/')
        # return render(request, 'main/index.html', {"message": "Login Success"})
        # login succeded, proceed to main menu page.
        elif loginString == "already logged in":
            return render(request, 'main/index.html', {"message": "Already logged in"})
            # we need to check the session here in our site logic, we will no longer be using the database model.
        elif loginString == "Incorrect password":
            return render(request, 'main/index.html', {"message": "Login Failed"})
            # login failed, we respond acourdingly.


class MenuView(
    View):  # currently, all the buttons in the individual pages submit post requests to them. It's sloppy, and we may want to change that functionallity here soon.
    def get(self, request):
        try:
            currentUserType = request.session["userType"]
        except KeyError:
            return redirect('/logout')  # redirect to logout if no user is logged in. This will display
            # The "No User Logged in" Message
        if currentUserType == 'chair':
            return render(request, 'main/ChairMenu.html', {'message': request.session['userType']})
        elif currentUserType == 'instructor':
            return render(request, 'main/instructorMenu.html', {'message': request.session['userType']})
        elif currentUserType == 'Instructor':
            return render(request, 'main/instructorMenu.html', {'message': request.session['userType']})
        elif currentUserType == 'ta' or 'TA': #for some reason, or works here, but does not work in instructor or chair.
            return render(request, 'main/TAMenu.html', {'message': request.session['userType']})
        # this is where we check the current users login status, and post results for user type

    def post(self, request):
        return render(request, 'main/TAMenu.html')
    # we may not need this, since all buttons will just be re-direct links. we probably want re-direct logic
    # in the HTML, but we can put it in here if that's safer or something.


class addCourseView(View):
    def get(self, request):
        try:
            currentUserType = request.session["userType"]
            if currentUserType != "chair":
                return redirect('/logout')
        except KeyError:
            return redirect('/logout')
        courses = addCourse.AddCourse.populate_lectures(request.session['member_id'])
        return render(request, 'main/addCourse.html',{"courses": courses})

    def post(self, request):
        try:
            currentUserType = request.session["userType"]
            if currentUserType != "chair":
                return redirect('/logout')
        except KeyError:
            return redirect('/logout')
        addthis = addCourse.AddCourse(request.POST["Course Name"])
        response = addthis.addCourse(request)
        courses = addCourse.AddCourse.populate_lectures(request.session['member_id'])
        return render(request, 'main/addCourse.html', {'message': response, "courses": courses})


class addUserView(View):
    def get(self, request):
        try:
            currentUserType = request.session["userType"]
            if currentUserType != "chair":
                return redirect('/logout')
        except KeyError:
            return redirect('/logout')
        return render(request, 'main/addUser.html')

    def post(self, request):
        try:
            currentUserType = request.session["userType"]
            if currentUserType != "chair":
                return redirect('/logout')
        except KeyError:
            return redirect('/logout')
        adduserInstance = addUser.AddUser()
        adduserString = adduserInstance.addUser(request)
        return render(request, 'main/addUser.html', {"message": adduserString})
        # return render(request, 'main/addUser.html')


class viewUsersView(View):
    def get(self, request):
        try:
            currentUserType = request.session["userType"]
            if currentUserType != "chair":
                return redirect('/logout')
        except KeyError:
            return redirect('/logout')
        users = myUser.objects.all()
        return render(request, 'main/viewUsers.html', {'users': users})

    def post(self, request):
        try:
            currentUserType = request.session["userType"]
            if currentUserType != "chair":
                return redirect('/logout')
        except KeyError:
            return redirect('/logout')
        return render(request, 'main/viewUsers.html')


class viewCourses(View):
    def get(self, request):
        try:
            currentUserType = request.session["userType"]
            if currentUserType != "chair":
                return redirect('/logout')
        except KeyError:
            return redirect('/logout')
        courses = Course.objects.all()
        return render(request, 'main/viewCourse.html', {'courses': courses})

    def post(self, request):
        try:
            currentUserType = request.session["userType"]
            if currentUserType != "chair":
                return redirect('/logout')
        except KeyError:
            return redirect('/logout')
        return render(request, 'main/viewCourse.html')


class editCourses(View):
    def get(self, request):
        try:
            currentUserType = request.session["userType"]
            if currentUserType != "chair":
                return redirect('/logout')
        except KeyError:
            return redirect('/logout')
        request.session["course_name"] = request.GET["Edit Course"]
        course = Course.objects.get(course_name= request.GET["Edit Course"]) # just getting the single course, instead of all the courses
        #there is a chance for null course, but with how you have to get here, it ~should~ never happen.
        startTime=course.start_time.__str__()
        endTime = course.end_time.__str__()
        return render(request, 'main/editCourse.html',{'start':startTime, 'end':endTime,'course': course})

    def post(self, request):
        try:
            currentUserType = request.session["userType"]
            if currentUserType != "chair":
                return redirect('/logout')
        except KeyError:
            return redirect('/logout')
        edit_this = addCourse.AddCourse(request.POST["Course Name"])
        response = edit_this.editCourse(request)
        if response == 'Invalid course name':
            return render(request, 'main/editCourse.html', {'message': response})
        if response == 'Empty Field':
            return render(request, 'main/editCourse.html', {'message': response})
        else:
            return redirect('/viewCourse/')

class chair_assignToCourseView(View):
    def get(self, request):
        try:
            currentUserType = request.session["userType"]
        except KeyError:
            return redirect('/logout')  # redirect to logout if no user is logged in. This will display
            # The "No User Logged in" Message
        users = chair_assignToCourse.populateUsers(request.session['member_id'])
        courses = chair_assignToCourse.populateCourses(request.session['member_id'])
        return render(request, 'main/chair_assignToCourse.html',
                      {"users": users, "courses": courses})

    def post(self, request):
        try:
            currentUserType = request.session["userType"]
            if currentUserType != "chair":
                return redirect('/logout')
        except KeyError:
            return redirect('/logout')
        if chair_assignToCourse.makeAssignment(request.session['member_id'], request.POST['availableUsers'],
                                         request.POST['availableCourses']):
            message = 'Assignment successful'
        else:
            message = 'Something went wrong'
        users = chair_assignToCourse.populateUsers(request.session['member_id'])
        courses = chair_assignToCourse.populateCourses(request.session['member_id'])
        return render(request, 'main/chair_assignToCourse.html',
                      {"users": users, "courses": courses, 'message': message})

class instructor_assignToCourseView(View):
    def get(self, request):
        try:
            currentUserType = request.session["userType"]#maybe also check that the user is an instructor here.
            if currentUserType != "instructor":
                return redirect('/logout')
        except KeyError:
            return redirect('/logout')  # redirect to logout if no user is logged in. This will display
            # The "No User Logged in" Message
        users = instructor_assignToCourse.populateUsers(request.session['member_id'])
        courses = instructor_assignToCourse.populateCourses(request.session['member_id'])
        return render(request, 'main/instructor_assignToCourse.html',
                      {"users": users, "courses": courses})

    def post(self, request):
        if instructor_assignToCourse.makeAssignment(request.session['member_id'], request.POST['availableUsers'],
                                         request.POST['availableCourses']):
            message = 'Assignment successful'
        else:
            message = 'Something went wrong'
        users = instructor_assignToCourse.populateUsers(request.session['member_id'])
        courses = instructor_assignToCourse.populateCourses(request.session['member_id'])
        return render(request, 'main/instructor_assignToCourse.html',
                      {"users": users, "courses": courses, 'message': message})


class logoutView(View):
    def get(self, request):
        doLogOut = logout.logMeOut()
        logoutString = doLogOut.logoutCheck(request)
        if logoutString == 'No user logged in':
            return render(request, 'main/index.html', {'message': 'No user logged in'})
        elif logoutString == 'You are now logged out':
            return render(request, 'main/logout.html')

    def post(self, request):
        return render(request, 'main/logout.html')
    # there should never be a post request



class runValidate(View):
    def get(self, request):
        try:
            currentUser = request.session['member_id']
            currentUserType = request.session['userType']
            #we're not doing anything with the session variables at the moment, just accessing to validate
        except KeyError:
            return redirect('/logout')

        conflictList = validate.validateScope(request.session['member_id'], request.session['userType'])
        message = "The following labs have scheduling conflicts with their TAs' personal schedules: "
        if not conflictList:
            message = "No labs with scheduling conflicts."

        return render(request, 'main/validate.html', {'conflicts': conflictList, 'message': message})


class editScheduleView(View): #only ta
    def get(self, request):
        try:
            currentUserType = request.session["userType"]
            if currentUserType != "ta":
                return redirect('/logout')
        except KeyError:
            return redirect('/logout')
        breaks = Break.objects.all()
        return render(request, 'main/taEditSchedule.html', {'breaks': breaks})
    def post(self, request):
        try:
            currentUserType = request.session["userType"]
            if currentUserType != "ta":
                return redirect('/logout')
        except KeyError:
            return redirect('/logout')
        return render(request, 'main/taEditSchedule.html')


class addBreak(View):
    def get(self, request):
        try:
            currentUserType = request.session["userType"]
            if currentUserType != "ta":
                return redirect('/logout')
        except KeyError:
            return redirect('/logout')
        return render(request, 'main/addBreak.html')

    def post(self, request):
        try:
            currentUserType = request.session["userType"]
            if currentUserType != "ta":
                return redirect('/logout')
        except KeyError:
            return redirect('/logout')
        addthis = createBreak.AddBreak(request.POST["Break Name"])
        response = addthis.addBreak(request)
        return render(request, 'main/addBreak.html', {'message': response})


class editBreak(View):
    def get(self, request):
        try:
            currentUserType = request.session["userType"]
            if currentUserType != "ta":
                return redirect('/logout')
        except KeyError:
            return redirect('/logout')
        breaks = Break.objects.all()
        request.session["break_name"] = request.GET["Edit Break"]
        return render(request, 'main/editBreak.html', {'breaks': breaks})

    def post(self, request):
        try:
            currentUserType = request.session["userType"]
            if currentUserType != "ta":
                return redirect('/logout')
        except KeyError:
            return redirect('/logout')
        edit_this = createBreak.AddBreak(request.POST["Break Name"])
        response = edit_this.editBreak(request)
        return render(request, 'main/editBreak.html', {'message': response})
