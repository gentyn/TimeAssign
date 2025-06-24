from django.test import TestCase
from ta_app.sitelogic.addCourse import *


class TestAddCourse(TestCase):
    def setUp(self):
        pass


class TestCheckEmpty(TestAddCourse):
    def test_check_empty1(self):
        self.assertFalse(check_empty(""))

    def test_check_empty2(self):
        self.assertFalse(check_empty(None))

    def test_check_empty3(self):
        self.assertTrue(check_empty("This is a string"))


class TestValidTime(TestAddCourse):
    def test_valid_time(self):
        self.assertTrue(valid_time("1234"))

    def test_valid_time2(self):
        self.assertFalse(valid_time("2400"))

    def test_valid_time3(self):
        self.assertFalse(valid_time("1260"))

    def test_valid_time_short(self):
        self.assertFalse(valid_time("123"))

    def test_valid_time_long(self):
        self.assertFalse(valid_time("12345"))

# def test_addSuccess(self):
#    pass

# def test_addSuccessOnline(self):
#    pass

# def test_addPreexisting(self):
#    pass

# def test_badForm_strings(self):
#    pass

# def test_badForm_time(self):
#    pass
