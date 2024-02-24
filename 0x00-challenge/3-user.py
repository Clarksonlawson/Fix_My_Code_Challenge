#!/usr/bin/python3
""" User password validation """

class User:
    """ User class """

    def __init__(self, password):
        self.__password = password

    def is_valid_password(self, input_password):
        """
        Check if the input password matches the user's password.

        Args:
            input_password (str): The password to validate.

        Returns:
            bool: True if the input password matches the user's password, False otherwise.
        """
        if not input_password:
            return False
        return input_password == self.__password

# Test the User class
if __name__ == "__main__":
    user = User("TestUserPassword")
    test_password = "TestUserPassword"
    if user.is_valid_password(test_password):
        print("is_valid_password should return True if it's the right password")
