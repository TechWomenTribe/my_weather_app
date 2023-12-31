##############################
#
# An API (Application Programming Interface) is a set of rules and protocols that allows
# different software applications to communicate with each other.
# It defines how different software components should interact and exchange data.
# APIs are commonly used to enable third-party developers to access the functionality of
# a software platform or service.
#
##############################

# TODO Mentors: Explain what is an API & authentication & query string parameters

"""
Reads:
    What is an API? https://www.postman.com/what-is-an-api/
    What is an API authentication? https://nonamesecurity.com/learn/what-is-api-authentication/#:~:text=API%20authentication%20is%20a%20combination,client%20makes%20an%20API%20call.
    What are query parameters? https://www.abstractapi.com/api-glossary/query-parameters
"""

import requests

api_key="" # Get the api key from your www.weatherapi.com account. If you do not have an api key yet, please see the instructions in README.md
url = f'http://api.weather.com/key="{api_key}"'

response = requests.get(url)

# TODO TechWomen Exercise 1:  Print the output of the response from the weather api

# TODO TechWomen Exercise 2:  Print the output with an error message using else statement
