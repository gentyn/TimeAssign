from django.test import TestCase, Client
from ta_app import models
from ta_app.sitelogic import validate
import datetime

#TODO since validate code is still waiting on some external stuff to be testable
#TODO this data prep might not be quite right. unfortunately its also huge and messy

class DataWithConflicts(TestCase):
    def setUp(self):
        data1 = models.myUser(username="Chair", password="any", name="Chair",
                              usertype="chair", email="any@any.com")
        data1.id = 100
        data1.save()

        data2 = models.myUser(username="Inst", password="any", name="Inst",
                              usertype="instructor", email="any@any.com")
        data2.id = 200
        data2.save()

        data3 = models.myUser(username="ta1", password="any", name="ta1",
                              usertype="ta", email="any@any.com")
        data3.id = 300
        data3.save()

        data4 = models.myUser(username="ta2", password="any", name="ta2",
                              usertype="ta", email="any@any.com")
        data4.id = 400
        data4.save()

        data5 = models.myUser(username="ta3", password="any", name="ta3",
                              usertype="ta", email="any@any.com")
        data5.id = 500
        data5.save()

        data6 = models.Course(course_name="stuff1", start_time=datetime.time(00, 00),
                              end_time=datetime.time(1, 00), mon_flag=True, instructor=200,
                              ta1=300, ta2=400, coursetype='LEC')
        data6.id = 100
        data6.save()

        data7 = models.Course(course_name="stuff2", start_time=datetime.time(00, 00),
                              end_time=datetime.time(1, 00), mon_flag=True, ta1=400, ta2=500,
                              ta3=400, coursetype='LEC')
        data7.id = 200
        data7.save()

        data8 = models.Course(course_name="lab1", start_time=datetime.time(3, 00),
                              end_time=datetime.time(4, 00), mon_flag=True, coursetype='LAB',
                              lectureid=100, ta1=300) #no conflict
        data8.id = 300
        data8.save()

        data9 = models.Course(course_name="lab2", start_time=datetime.time(3, 00),
                              end_time=datetime.time(4, 00), mon_flag=True, coursetype='LAB',
                              lectureid=100, ta1=400) #one conflict
                            #a break starts during this lab
        data9.id = 400
        data9.save()

        data0 = models.Course(course_name="lab3", start_time=datetime.time(5, 00),
                              end_time=datetime.time(6, 00), mon_flag=True, coursetype='LAB',
                              lectureid=200, ta1=400) #one conflict
                            #a break ends during this lab
        data0.id = 500
        data0.save()

        dataA = models.Course(course_name="lab4", start_time=datetime.time(5, 00),
                              end_time=datetime.time(6, 00), mon_flag=True, coursetype='LAB',
                              lectureid=200, ta1=500) #one conflict
                            #this lab starts & ends during a break
        dataA.id = 600
        dataA.save()

        dataB = models.Course(course_name="lab5", start_time=datetime.time(3, 00),
                              end_time=datetime.time(4, 00), tues_flag=True, coursetype='LAB',
                              lectureid=200, ta1=400) #one conflict
                             #a break starts & ends during this lab
        dataB.id = 700
        dataB.save()

        dataC = models.Break(userid=300, mon_flag=True, start_time=datetime.time(12,00),
                             end_time=datetime.time(13, 00)) #no conflict

        dataC.id = 100
        dataC.save()

        dataD = models.Break(userid=300, tues_flag=True, start_time=datetime.time(0,00),
                             end_time=datetime.time(13, 00)) #no conflict

        dataD.id = 200
        dataD.save()

        dataE = models.Break(userid=400, mon_flag=True, start_time=datetime.time(0, 00),
                             end_time=datetime.time(1, 00)) #no conflict
                             #but does overlap a lecture this TA has a lab for

        dataE.id = 300
        dataE.save()

        dataF = models.Break(userid=400, tues_flag=True, start_time=datetime.time(12, 00),
                             end_time=datetime.time(13, 00)) #no conflict

        dataF.id = 400
        dataF.save()

        dataG = models.Break(userid=400, mon_flag=True, start_time=datetime.time(3, 30),
                             end_time=datetime.time(5, 30)) #two conflicts
                            #starts during one lab and ends during another

        dataG.id = 500
        dataG.save()

        dataH = models.Break(userid=400, tues_flag=True, start_time=datetime.time(3, 15),
                             end_time=datetime.time(3, 45)) #one conflict
                             #starts & ends during a lab

        dataH.id = 600
        dataH.save()

        dataI = models.Break(userid=500, start_time=datetime.time(4, 00),
                             end_time=datetime.time(7, 00), mon_flag=True) #one conflict
                             #a lab starts & ends during this break

        dataI.id = 700
        dataI.save()

class DataNoConflicts(TestCase):
    def setUp(self):
        data1 = models.myUser(username="Chair", password="any", name="Chair",
                              usertype="chair", email="any@any.com")
        data1.id = 100
        data1.save()

        data2 = models.myUser(username="Inst", password="any", name="Inst",
                              usertype="instructor", email="any@any.com")
        data2.id = 200
        data2.save()

        data3 = models.myUser(username="ta1", password="any", name="ta1",
                              usertype="ta", email="any@any.com")
        data3.id = 300
        data3.save()

        data4 = models.myUser(username="ta2", password="any", name="ta2",
                              usertype="ta", email="any@any.com")
        data4.id = 400
        data4.save()

        data5 = models.myUser(username="ta3", password="any", name="ta3",
                              usertype="ta", email="any@any.com")
        data5.id = 500
        data5.save()

        data6 = models.Course(course_name="stuff1", start_time=datetime.time(00, 00),
                              end_time=datetime.time(1, 00), mon_flag=True, instructor=200,
                              ta1=300, ta2=400, ta3=500, coursetype='LEC')
        data6.id = 100
        data6.save()

        data7 = models.Course(course_name="stuff2", start_time=datetime.time(00, 00),
                              end_time=datetime.time(1, 00), mon_flag=True, ta1=400, ta2=500,
                              coursetype='LEC')
        data7.id = 200
        data7.save()

        data8 = models.Course(course_name="lab1", start_time=datetime.time(3, 00),
                              end_time=datetime.time(4, 00), mon_flag=True, coursetype='LAB',
                              lectureid=100, ta1=300)
        data8.id = 300
        data8.save()

        data9 = models.Course(course_name="lab2", start_time=datetime.time(3, 00),
                             end_time=datetime.time(4, 00), mon_flag=True, coursetype='LAB',
                              lectureid=100, ta1=400)
        data9.id = 400
        data9.save()

        data0 = models.Course(course_name="lab3", start_time=datetime.time(5, 00),
                             end_time=datetime.time(6, 00), mon_flag=True, coursetype='LAB',
                              lectureid=200, ta1=400)
        data0.id = 500
        data0.save()

        dataA = models.Course(course_name="lab4", start_time=datetime.time(5, 00),
                             end_time=datetime.time(6, 00), mon_flag=True, coursetype='LAB',
                              lectureid=200, ta1=500)
        dataA.id = 600
        dataA.save()

        dataB = models.Course(course_name="lab5", start_time=datetime.time(3, 00),
                              end_time=datetime.time(4, 00), tues_flag=True, coursetype='LAB',
                              lectureid=100, ta1=400)
        dataB.id = 700
        dataB.save()

        dataC = models.Break(userid=300, mon_flag=True, start_time=datetime.time(12,00),
                             end_time=datetime.time(13, 00)) #no conflict

        dataC.id = 100
        dataC.save()

        dataD = models.Break(userid=300, tues_flag=True, start_time=datetime.time(12,00),
                             end_time=datetime.time(13, 00)) #no conflict

        dataD.id = 200
        dataD.save()

        dataE = models.Break(userid=400, mon_flag=True, start_time=datetime.time(0, 00),
                             end_time=datetime.time(1, 00)) #no conflict
                             #but does overlap with a lecture this TA is listed on

        dataE.id = 300
        dataE.save()

        dataF = models.Break(userid=400, tues_flag=True, start_time=datetime.time(12, 00),
                             end_time=datetime.time(13, 00)) #no conflict

        dataF.id = 400
        dataF.save()

        dataG = models.Break(userid=400, mon_flag=True, start_time=datetime.time(13, 30),
                             end_time=datetime.time(15, 30)) #no conflict

        dataG.id = 500
        dataG.save()

        dataH = models.Break(userid=400, tues_flag=True, start_time=datetime.time(13, 15),
                             end_time=datetime.time(13, 45)) #no conflict

        dataH.id = 600
        dataH.save()

        dataI = models.Break(userid=500, start_time=datetime.time(14, 00),
                             end_time=datetime.time(17, 00)) #no conflict

        dataI.id = 700
        dataI.save()

class TestBad(DataWithConflicts):
    def testValidateBadChair(self):
        #run validate as a Chair, expect all the conflicts & only conflicts back
        results = list(models.Course.objects.all().filter(coursetype='LAB').exclude(ta1=300))
        c = Client() #user 100, usertype 'chair'
        c.post('/', {'username': 'Chair', 'pass': 'any'})
        resp = c.get('/validate', follow=True)
        self.assertEquals(resp.context.get("message"), "The following labs have scheduling conflicts with their TAs' personal schedules: ")
        self.assertEquals(resp.context.get("conflicts"), results)

    def testValidateBadInstruct(self):
        #run validate as an instructor, expect all the conflicts for labs tied to
        # that instructor's courses & only those conflicts back
        results = list(models.Course.objects.all().filter(coursetype='LAB').filter(lectureid=100).exclude(ta1=300))
        c = Client() #user 200, usertype 'instructor'
        c.post('/', {'username': 'Inst', 'pass': 'any'})
        resp = c.get('/validate', follow=True)
        self.assertEquals(resp.context.get("message"), "The following labs have scheduling conflicts with their TAs' personal schedules: ")
        self.assertEquals(resp.context.get("conflicts"), results)

    def testValidateBadTA(self):
        #run validate as a ta, expect all that TA's conflicts & only those conflicts back
        results = list(models.Course.objects.all().filter(coursetype='LAB').filter(ta1=400))
        c = Client() #user 300, usertype 'ta'
        c.post('/', {'username': 'ta2', 'pass': 'any'})
        resp = c.get('/validate', follow=True)
        self.assertEquals(resp.context.get("message"), "The following labs have scheduling conflicts with their TAs' personal schedules: ")
        self.assertEquals(resp.context.get("conflicts"), results)

class TestGood(DataNoConflicts):
    def testValidateGoodChair(self):
        #run validate as a chair, expect no conflicts
        c = Client() #user 100, usertype 'chair'
        c.post('/', {'username': 'Chair', 'pass': 'any'})
        resp = c.get('/validate', follow=True)
        self.assertEquals(resp.context.get("message"), "No labs with scheduling conflicts.")
        self.assertEquals(resp.context.get("conflicts"), [])

    def testValidateGoodInstruct(self):
        # run validate as an instructor, expect no conflicts
        c = Client() #user 200, usertype 'instructor'
        c.post('/', {'username': 'Inst', 'pass': 'any'})
        resp = c.get('/validate', follow=True)
        self.assertEquals(resp.context.get("message"), "No labs with scheduling conflicts.")
        self.assertEquals(resp.context.get("conflicts"), [])

    def testValidateGoodTA(self):
        # run validate as a ta, expect no conflicts
        c = Client() #user 300, usertype 'ta'
        c.post('/', {'username': 'ta1', 'pass': 'any'})
        resp = c.get('/validate', follow=True)
        self.assertEquals(resp.context.get("message"), "No labs with scheduling conflicts.")
        self.assertEquals(resp.context.get("conflicts"), [])

class TestEmpty(TestCase):
    #without any assigned labs or TA schedules, we do not have
    #any conflicts

    def setUp(self):
        data1 = models.myUser(username="Chair", password="any", name="Chair",
                              usertype="chair", email="any@any.com")
        data1.id = 100
        data1.save()

        data2 = models.myUser(username="Inst", password="any", name="Inst",
                              usertype="instructor", email="any@any.com")
        data2.id = 200
        data2.save()

        data3 = models.myUser(username="ta1", password="any", name="ta1",
                              usertype="ta", email="any@any.com")
        data3.id = 300
        data3.save()

    def testValidateGoodChair(self):
        # run validate as a chair, expect no conflicts
        c = Client() #user 100, usertype 'chair'
        c.post('/', {'username': 'Chair', 'pass': 'any'})
        resp = c.get('/validate', follow=True)
        self.assertEquals(resp.context.get("message"), "No labs with scheduling conflicts.")
        self.assertEquals(resp.context.get("conflicts"), [])

    def testValidateGoodInstruct(self):
        # run validate as an instructor, expect no conflicts
        c = Client() #user 200, usertype 'instructor'
        c.post('/', {'username': 'Inst', 'pass': 'any'})
        resp = c.get('/validate', follow=True)
        self.assertEquals(resp.context.get("message"), "No labs with scheduling conflicts.")
        self.assertEquals(resp.context.get("conflicts"), [])

    def testValidateGoodTA(self):
        # run validate as a ta, expect no conflicts
        c = Client() #user 300, usertype 'ta'
        c.post('/', {'username': 'ta1', 'pass': 'any'})
        resp = c.get('/validate', follow=True)
        self.assertEquals(resp.context.get("message"), "No labs with scheduling conflicts.")
        self.assertEquals(resp.context.get("conflicts"), [])