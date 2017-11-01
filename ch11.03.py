
class Employee():
    def __init__(self,firstname, lastname, year_wage =5000):
        self.lastname=lastname.title()
        self.firstname=firstname.title()
        self.year_wage=year_wage

    def give_raise(self, wage_raise = 5000):
        get_new_wage=int(self.year_wage) + int(wage_raise)
        return get_new_wage




import unittest

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.my_emplyee = Employee("Alt", "HU")

    def test_give_default_raise(self):
        self.my_emplyee.give_raise()
        self.assertEqual(10000, self.my_emplyee.give_raise())

    def test_give_custom_raise(self):
        new_wage=self.my_emplyee.give_raise(wage_raise="600")
        self.assertEqual(5600,new_wage)


unittest.main()
