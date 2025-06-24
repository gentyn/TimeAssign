from ta_app import models
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

class logMeOut():
    def logoutCheck(self, request):
        try:
            del request.session['member_id']
            del request.session['userType']
        except KeyError:
            return 'No user logged in'
        return 'You are now logged out'