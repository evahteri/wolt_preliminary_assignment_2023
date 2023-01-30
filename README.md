# My Solution for Preliminary Assignment for Engineering Positions Summer 2023

This API is made for Wolt's preliminary assignment 2023. Details on the assignment can be found [here](https://github.com/woltapp/engineering-summer-intern-2023). This is my solution for the backend version.

## Instructions

### Install and Launch

Make sure you have Python version 3.10 or higher to make sure the program functions correctly.

To launch the API locally you need to run these commands:

In the root directory:

- ```python3 -m venv venv``` to prepare virtual environment

- ```source venv/bin/activate``` to activate virtual environment

- ``` pip install -r requirements.txt ``` to install dependencies

- ```cd src/ ``` to go to the src folder

- ``` flask run ``` to launch the API on http://localhost:5000/

### Using the API

Test the application with a POST request with, for example, Postman's desktop application.

All requests should be directed to "http://localhost:5000/" as that is the only endpoint.

Note that the API works only with correct POST requests, other types of requests are unallowed.

### Running tests

Automated tests can be run inside the virtual environment:

- ```source venv/bin/activate``` to activate virtual environment

- ```pytest``` to run tests

Run these to check test coverage:

- ```coverage run --branch -m pytest```

- ```coverage report -m```

- ```coverage html``` To create a visual representation of test coverage. You can see it from created folder "htmlcov" and copying the path of index.html to the url field of your browser.

