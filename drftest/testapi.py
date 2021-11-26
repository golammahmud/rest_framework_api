import requests

import requests
from requests.exceptions import HTTPError
url='http://127.0.0.1:8000/student/pervez'

try:
    response = requests.get(url)
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()
    print("Entire JSON response")
    print(jsonResponse)

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
    
