"""
Instructions to Complete the Basic POST API

In this exercise, you will create a basic Flask API that allows adding new patient data to a CSV file and returns the added data as a JSON response. Follow the steps below to complete the task.

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

4. Define a route to add patient data:
    - Use the @app.route decorator to define a POST endpoint '/patient'.
    - Implement a function `add_patient` that:
        a. Gets the JSON data from the request.
        b. Appends the new patient data to the DataFrame.
        c. Saves the updated DataFrame back to the CSV file.
        d. Returns the data of the added patient as a JSON response with a 201 status code.

5. Run the Flask application:
    - Use `app.run` to start the Flask app on host '0.0.0.0' and port '5001' with debug mode enabled.
"""
