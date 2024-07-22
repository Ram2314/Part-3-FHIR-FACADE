"""
Instructions to Complete the Basic GET API

In this exercise, you will create a basic Flask API that retrieves patient data from a CSV file and returns it as a JSON response. Follow the steps below to complete the task.

1. Import the necessary libraries:
    - Import Flask from the flask module.
    - Import jsonify from the flask module.
    - Import pandas as pd.

2. Load the data:
    - Use pandas to read the CSV file named 'Clinical Data_Discovery_Cohort.csv'.
    - This will simulate a database containing patient data.

3. Create a Flask application:
    - Initialize a Flask app instance.

4. Define a route to get patient data:
    - Use the @app.route decorator to define a GET endpoint '/patient/<int:patient_id>'.
    - Implement a function `get_patient` that takes `patient_id` as an argument.
    - Filter the DataFrame to find the specified patient ID.
    - If the patient ID exists in the DataFrame, convert the data to a dictionary and return it as a JSON response.
    - If the patient ID does not exist, return a JSON error message with a 404 status code.

5. Run the Flask application:
    - Use `app.run` to start the Flask app on host '0.0.0.0' and port '5001' with debug mode enabled.

"""