import requests
import numpy as np

if __name__ == '__main__':
    payload = {}
    headers = {}

    # Test basic response
    url = "http://127.0.0.1:5000"

    response = requests.request("GET", url, headers=headers, data=payload)
    print(f"Testing default rote ------------------------------------------------------------------\n{response.text}\n")

    # Test response with JSON data
    url = "http://127.0.0.1:5000/json_get"

    response = requests.request("GET", url, headers=headers, data=payload)
    json_response = response.json()
    print(f"Testing GET and JSON return -----------------------------------------------------------\n{json_response}\n")

    # Test posting JSON data
    url = "http://127.0.0.1:5000/json_post"

    x = np.array([[1, 2],
                  [3, 4]])
    y = np.array([[5, 6],
                  [7, 8]])
    test_data = {"x": x.tolist(), "y": y.tolist()}
    response = requests.request("POST", url, json=test_data)
    print(f"Testing POST and JSON data -----------------------------------------------------------------\n{response}\n")

    # Test POST and GET with JSON data
    url = "http://127.0.0.1:5000/json_get_post"

    x = np.array([[1, 2],
                  [3, 4]])
    y = np.array([[5, 6],
                  [7, 8]])
    test_data = {"x": x.tolist(), "y": y.tolist()}
    response = requests.request("POST", url, json=test_data)
    json_response = response.json()
    print(f"Testing POST and GET with JSON data ---------------------------------------------------\n{json_response}\n")
