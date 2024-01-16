#!/usr/bin/python3

"""
Module docstring explaining the purpose of the module.
"""

class BaseModel:
    """
    Base class for Airbnb objects.
    """

    def __init__(self, name, description):
        """
        Initialize a new Airbnb object.

        Args:
        - name (str): The name of the object.
        - description (str): The description of the object.
        """
        self.name = name
        self.description = description

    def display_info(self):
        """
        Display information about the Airbnb object.
        """
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")

    def update_description(self, new_description):
        """
        Update the description of the Airbnb object.

        Args:
        - new_description (str): The new description.
        """
        self.description = new_description

# Ensure the script is executable
if __name__ == "__main__":
    obj = BaseModel("Example Object", "This is a sample object.")
    obj.display_info()
    obj.update_description("Updated description.")
    obj.display_info()

