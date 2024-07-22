"""
Instructions to Complete the Facade Design Pattern for Patient Data Management

In this exercise, you will implement a Facade design pattern to manage patient data stored in a CSV file. The Facade will provide a simplified interface to perform CRUD operations (Create, Read, Update, Delete) on the patient data. Follow the steps below to complete the task.

1. Import the necessary libraries:
    - Import pandas as pd.

2. Define the PatientDataFacade class:
    - Create a class `PatientDataFacade` that will act as the facade.
    - Implement the `__init__` method to initialize the class with a file path to the CSV file and load the data into a pandas DataFrame.

3. Implement the get_patient method:
    - Define a method `get_patient` that takes a patient ID as a parameter.
    - Filter the DataFrame for the specified patient ID.
    - If the patient data exists, return the patient data as a dictionary with a 200 status code.
    - If the patient data does not exist, return an error message with a 404 status code.

4. Implement the add_patient method:
    - Define a method `add_patient` that takes a new patient data dictionary as a parameter.
    - Append the new patient data to the DataFrame.
    - Save the updated DataFrame back to the CSV file.
    - Return the new patient data with a 201 status code.

5. Implement the delete_patient method:
    - Define a method `delete_patient` that takes a patient ID as a parameter.
    - Filter the DataFrame for the specified patient ID.
    - If the patient data exists, delete the patient data from the DataFrame.
    - Save the updated DataFrame back to the CSV file.
    - Return a success message with a 200 status code.
    - If the patient data does not exist, return an error message with a 404 status code.
"""