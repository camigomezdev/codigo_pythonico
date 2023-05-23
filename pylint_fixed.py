"""This code works with Pylint

MyPerson program
"""
class MyPerson:
    """MyPerson class"""
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.asked_for_name = False

    def get_name(self):
        """
        Returns Person name
        :return: the name
        """
        self.asked_for_name = True
        return self.name

    def get_age(self):
        """
        Returns Person age
        :return: the age
        """
        return self.age

    def get_gender(self):
        """
        Returns Person gender
        :return: the gender
        """
        return self.gender


print(MyPerson('Cami', 27, 'F').get_name())
