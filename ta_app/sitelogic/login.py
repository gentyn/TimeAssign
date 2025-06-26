from ta_app import models
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class myUserLogin():

    def loginCheck(self, request):
        try:
            currentSession = request.session['member_id']
            return "already logged in"
            #untested, but I'm pretty sure this works.
        except KeyError: #this means there is not a user currently logged in.
            username = request.POST.get('username')
            password = request.POST.get('pass')
            
            # First try Django's auth system
            user = authenticate(username=username, password=password)
            if user is not None:
                # If it's a Django auth user, create or update corresponding myUser
                try:
                    m = models.myUser.objects.get(username=username)
                except ObjectDoesNotExist:
                    # Create corresponding myUser if doesn't exist
                    m = models.myUser(
                        username=username,
                        password=password,  # Note: This is not secure but maintaining compatibility
                        name=username,
                        usertype='chair' if user.is_superuser else 'ta'
                    )
                    m.save()
                
                request.session['member_id'] = m.id
                request.session['userType'] = m.usertype
                return "Logged In"
            
            # If Django auth fails, try the legacy system
            try:
                m = models.myUser.objects.get(username=username)
                if m.password == password:
                    request.session['member_id'] = m.id
                    request.session['userType'] = m.usertype
                    return "Logged In"
                else:
                    return "Incorrect password"
            except ObjectDoesNotExist:
                return "Incorrect password"