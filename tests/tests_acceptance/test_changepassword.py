"""import unittest

from Project import Project


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.pw = Project()
        app.command("DefaultChair") #default username
        app.command("DefaultPW") #default pw
        app.command("User Settings") #access user management

class TestLoginScreen(TestLogin):
    def test_select_changePW(self):
        self.assertEqual(app.command("Change PW"), "Changing password\nEnter current password: ")

    app.command("Change PW") #access Change PW

    def test_bad_oldPW(self): #enter an incorrect PW
        self.assertEqual(app.command("DefaultBad"), "Incorrect password.\nUser Settings")

    def test_good_old(self): #valid password
        self.assertEqual(app.command("DefaultPW"), "Enter new password: ")

    app.command("DefaultPW") #enter current PW

    def test_validate_noPW(self):  #only new PW that won't be accepted is nothing, app does nothing
        self.assertEqual(app.command(""), "")

    def test_new_PW(self): #new password is entered
        self.assertEqual(app.command("anyPW"), "Password changed")

    app.command("anyPw") #new PW
    app.command("Back") #back out to home menu
    app.command("Logout") #logout
    app.command("DefaultChair") #enter user to log back in

    def test_old_doesnt_work(self): #the previous PW no longer functions
        self.assertEqual(app.command("DefaultPW"), "Incorrect password.\Enter user:")

    def test_new_works(self): #the new password works
        self.assertEqual(app.command("anyPW"), "Home Menu")
        """