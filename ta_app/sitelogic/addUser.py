# the AddUser object takes the current user, verifies if the current user is chair,
# takes the name, username and usertype of the new user being created,
# generates a random password, and creates the user

from ta_app import models
from django.core.exceptions import ObjectDoesNotExist

class AddUser():
    usertype = ""
    username = ""
    name = ""
    password = ""
    email = ""

    #runForm has been replaced by command()

    #Checks if there is an active session
    def addUser(self, request):

        if(not self.checkSession(request)):
            return "no user logged in"

        tryaddUsername = request.POST['username']

        if(self.userexist(tryaddUsername)):
            return "User Already Exist, try adding a different username"
        else:
            #self.username = input[1]
            self.username = request.POST['username']
            self.password = request.POST['pass']
            self.usertype = request.POST['usertype']
            self.name = request.POST['realName']
            self.email = request.POST['email']

            if(not self.blankfields()):
                return "Error: Please fill in all the fields"

            models.myUser.objects.create(name=self.name,username=self.username,usertype=self.usertype,email=self.email,password=self.password, assignedInstructor=0)

            return "Created User"

    def checkSession(self,request):
        validsession = True
        try:
            currentSession = request.session['member_id']
        except KeyError: #this means there is not a user currently Logged in
            validsession = False

        return validsession

    def userexist(self, username):
        try:
            newUser = models.myUser.objects.get(username=username)
            return True
        except models.myUser.DoesNotExist:
            return False

    def blankfields(self):
        if(self.username == ""):
            return False
        elif(self.name == ""):
            return False
        elif(self.usertype == ""):
            return False
        elif(self.password == ""):
            return False
        elif(self.email == ""):
            return False
        else:
            return True



