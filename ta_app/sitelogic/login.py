from ta_app import models
from django.core.exceptions import ObjectDoesNotExist

class myUserLogin():

    def loginCheck(self, request):
        try:
            curentSession = request.session['member_id']
            return "already logged in"
            #untested, but I'm pretty sure this works.
        except KeyError: #this means there is not a user currently logged in.
            try:
                m = models.myUser.objects.get(username=request.POST['username'])
                if m.password == request.POST['pass']:
                    request.session['member_id'] = m.id
                    request.session['userType'] = m.usertype
                    return "Logged In"
                else:
                    return "Incorrect password"
            except ObjectDoesNotExist:
                return "Incorrect password"