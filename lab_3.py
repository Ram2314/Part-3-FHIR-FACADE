"""
Instructions to Complete the Basic DELETE API

In this exercise, you will create a basic Flask API that allows deleting patient data from a CSV file based on the patient ID and returns a confirmation message as a JSON response. Follow the steps below to complete the task.

1. Import the necessary libraries:
    - Import Flask from the flask module.
    - Import jsonify and request from the flask module.
    - Import pandas as pd.

2. Load the data:
    - Use pandas to read the CSV file named 'Clinical Data_Discovery_Cohort.csv'.
    - This will simulate a database containing patient data.
    - Store the file path in a variable for later use.

3. Create a Flask application:
    - Initialize a Flask app instance.

4. Define a route to delete patient data:
    - Use the @app.route decorator to define a DELETE endpoint '/patient/<int:patient_id>'.
    - Implement a function `delete_patient` that:
        a. Filters the DataFrame for the specified patient ID.
        b. Checks if the patient data exists. If it does:
            i. Deletes the patient data from the DataFrame.
            ii. Saves the updated DataFrame back to the CSV file.
            iii. Returns a success message as a JSON response with a 200 status code.
        c. If the patient data does not exist, returns an error message as a JSON response with a 404 status code.

5. Run the Flask application:
    - Use `app.run` to start the Flask app on host '0.0.0.0' and port '5001' with debug mode enabled.
"""

