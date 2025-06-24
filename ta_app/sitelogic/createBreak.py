from django.db import models
import re
from ta_app import models


# Returns false if field is empty
def check_empty(field):
    if field is None or field == "":
        return False
    else:
        return True


class AddBreak:
    break_name = ""
    start_time = ""
    end_time = ""
    mon_flag = False
    tues_flag = False
    wed_flag = False
    thu_flag = False
    fri_flag = False
    sat_flag = False
    userid = ""

    def __init__(self, bre):
        self.bre = bre

    def addBreak(self, request):
        if check_empty(request.POST["Break Name"]):
            self.break_name = request.POST["Break Name"]
            monday = False
            tuesday = False
            wednesday = False
            thursday = False
            friday = False
            saturday = False
            if request.POST.get('M', False) == 'on':
                monday = True
            if request.POST.get('T', False) == 'on':
                tuesday = True
            if request.POST.get('W', False) == 'on':
                wednesday = True
            if request.POST.get('R', False) == 'on':
                thursday = True
            if request.POST.get('F', False) == 'on':
                friday = True
            if request.POST.get('S', False) == 'on':
                saturday = True
            models.Break.objects.create(break_name=request.POST["Break Name"], start_time=request.POST['startTime'],
                                         end_time=request.POST['endTime'], mon_flag=monday, tues_flag=tuesday, wed_flag=wednesday, thurs_flag=thursday,
                                         fri_flag=friday, sat_flag=saturday,
                                         userid=request.session["member_id"])
            return "Break Created"

        else:
            return "Invalid break name"

    def editBreak(self, request):
        if check_empty(request.POST["Break Name"]):
            self.break_name = request.POST["Break Name"]
            m = models.Break.objects.get(break_name=request.POST["Break Name"])
            m.start_time = request.POST["startTime"]
            m.end_time = request.POST["endTime"]
            monday = False
            tuesday = False
            wednesday = False
            thursday = False
            friday = False
            saturday = False
            if request.POST.get('M', False) == 'on':
                monday = True
            if request.POST.get('T', False) == 'on':
                tuesday = True
            if request.POST.get('W', False) == 'on':
                wednesday = True
            if request.POST.get('R', False) == 'on':
                thursday = True
            if request.POST.get('F', False) == 'on':
                friday = True
            if request.POST.get('S', False) == 'on':
                saturday = True
            m.mon_flag = monday
            m.tues_flag = tuesday
            m.wed_flag = wednesday
            m.thurs_flag = thursday
            m.fri_flag = friday
            m.sat_flag = saturday
            m.mon_flag = self.mon_flag
            m.tues_flag = self.tues_flag
            m.wed_flag = self.wed_flag
            m.thurs_flag = self.thu_flag
            m.fri_flag = self.fri_flag
            m.sat_flag = self.sat_flag
            #m.day = request.POST["day"]
            #self.enter_days(m.day)
            #m.day = self.days
            if m.start_time == "" or m.end_time == "":
                return "Empty Field"
            else:
                m.save()
                return "Break Edited"
        else:
            return "Invalid break name"

    def enter_days(self, str):
        str = re.search('[M]?[T]?[W]?[R]?[F]?[S]?', str).group(0)
        if str != "":
            self.days = str
            return
        return "Enter days again"