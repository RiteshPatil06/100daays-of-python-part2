import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

#token here

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# response.raise_for_status()
# print(response.text)

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

graphpixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"

today = datetime.now()
today_date = today.strftime("%Y%m%d")
# print(today.strftime("%Y%m%d"))

pixel_config = {
    # "date": today_date,
    "quantity": input("How many kilometers did you cycle today? "),
}

# response = requests.post(url=graphpixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{today_date}"

response = requests.put(url=put_endpoint, json=pixel_config, headers=headers)
print(response.text)