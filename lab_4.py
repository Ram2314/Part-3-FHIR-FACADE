"""
Instructions to Complete the API with Facade Pattern


In this exercise, you will combine all the previous exercises along with the Facade design pattern to complete the assignment. The goal is to create a Flask API that utilizes the PatientDataFacade class to perform CRUD operations (Create, Read, Delete) on patient data stored in a CSV file. Follow the steps below to complete the task.

1. Import the necessary libraries:
    - Import PatientDataFacade from the facade module.
    - Import Flask, jsonify, and request from the flask module.

2. Initialize the Flask application:
    - Create a Flask app instance.

3. Initialize the PatientDataFacade:
    - Create an instance of the PatientDataFacade class with the path to the CSV file.

4. Define the GET endpoint to retrieve patient data:
    - Use the @app.route decorator to define a GET endpoint '/patient/<int:patient_id>'.
    - Implement a function `get_patient` that:
        a. Uses the facade to retrieve patient data based on the patient ID.
        b. Returns the response and status code from the facade.

5. Define the POST endpoint to add new patient data:
    - Use the @app.route decorator to define a POST endpoint '/patient'.
    - Implement a function `add_patient` that:
        a. Gets the new patient data from the request.
        b. Uses the facade to add the new patient data.
        c. Returns the response and status code from the facade.

6. Define the DELETE endpoint to delete patient data:
    - Use the @app.route decorator to define a DELETE endpoint '/patient/<int:patient_id>'.
    - Implement a function `delete_patient` that:
        a. Uses the facade to delete patient data based on the patient ID.
        b. Returns the response and status code from the facade.

7. Run the Flask application:
    - Use `app.run` to start the Flask app on host '0.0.0.0' and port '5001' with debug mode enabled.
"""

