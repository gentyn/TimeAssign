from django.test import TestCase
from django.test import Client

from ta_app import models
from ta_app.sitelogic import addUser



class testuserexist(TestCase):
    testTA = addUser.AddUser
    def setUp(self):
        self.testTA.name = "testTA"
        self.testTA.usertype = "TA"
        self.testTA.email = "testTA@email.com"
        self.testTA.password = "testTA"
        self.testTA.username = "testTA"

        models.myUser.objects.create(name="testTA", username="testTA", usertype="TA", email="testTA@email.com",
                                 password="testTA", assignedInstructor=0)

    def testgooduserexist(self):
        self.assertTrue(addUser.AddUser.userexist(self.testTA,"testTA"))

    def testbaduserexist(self):
        self.assertFalse(addUser.AddUser.userexist(self.testTA,"testTA1"))


class testblankfileds(TestCase):
    testTA = addUser.AddUser
    def setUp(self):
        self.testTA.name = "testTA"
        self.testTA.usertype = "TA"
        self.testTA.email = "testTA@email.com"
        self.testTA.password = "testTA"
        self.testTA.username = "testTA"

    def testGoodUser(self):
        self.assertTrue(addUser.AddUser.blankfields(self.testTA))

    def testBlankUsername(self):
        self.testTA.username = ""
        self.assertFalse(addUser.AddUser.blankfields(self.testTA))

    def testBlankName(self):
        self.testTA.name = ""
        self.assertFalse(addUser.AddUser.blankfields(self.testTA))

    def testBlankPassword(self):
        self.testTA.password = ""
        self.assertFalse(addUser.AddUser.blankfields(self.testTA))

    def testBlankUsertype(self):
        self.testTA.usertype = ""
        self.assertFalse(addUser.AddUser.blankfields(self.testTA))

    def testBlankEmail(self):
        self.testTA.email = ""
        self.assertFalse(addUser.AddUser.blankfields(self.testTA))