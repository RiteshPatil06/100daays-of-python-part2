from datetime import datetime
import requests
import os

GENDER = "Male"
WEIGHT_KG = 65
HEIGHT_CM = 182
AGE = 21

NUTRITIONIX_API_ID = os.environ.get("NUTRITIONIX_API_ID")
NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
token = os.environ.get("token")

SHEETY_API_GET = os.environ.get("SHEETY_API_GET")
SHEETY_API_POST = os.environ.get("SHEETY_API_POST")

NUTRITION_API_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'

exercise_text = input("Tell me which exercises you did: ")

nutrition_header = {
    'x-app-id': NUTRITIONIX_API_ID,
    'x-app-key': NUTRITIONIX_API_KEY
}

nutrition_parameter = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE

}
nutrition_response = requests.post(url=NUTRITION_API_ENDPOINT,headers=nutrition_header, json=nutrition_parameter )
nutrition_response.raise_for_status()
nutrition_response_json = nutrition_response.json()
print(nutrition_response_json)


today = datetime.now()
today_date = today.strftime("%d/%m/%Y")
today_time = today.strftime("%H:%M:%S")

for exercise in nutrition_response_json["exercises"]:
    post_parameter = {
            "sheet1": {
                "date": today_date,
                "time": today_time,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"],
            }
    }



#Bearer Token Authentication
bearer_headers = {
"Authorization": f"Bearer {token}"
}

sheety_response_post = requests.post(SHEETY_API_POST, json=post_parameter, headers=bearer_headers)
sheety_response_post.raise_for_status()
sheety_response_text = sheety_response_post.text
print(sheety_response_text)

