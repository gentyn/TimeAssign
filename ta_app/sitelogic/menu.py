from ta_app import models
from django.core.exceptions import ObjectDoesNotExist

def menuPopulator(request):
    userType = request.session['userType']
    if userType == 'chair':
        return 'https://www.w3schools.com'
        #return '<a href="https://www.w3schools.com">Visit W3Schools.com!</a>'
    return userType