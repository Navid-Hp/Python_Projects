import requests
from datetime import datetime
import os

GENDER = YOUR GENDER
WEIGHT_KG = YOUR WEIGHT
HEIGHT_CM = YOUR HEIGHT
AGE = YOUR AGE

APP_ID = os.environ["NT_APP_ID"]
APP_KEY = os.environ["NT_APP_KEY"]

USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = os.environ["SHEET_ENDPOINT"]

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    # ## Without Authentication
    # sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    # print(sheet_response.text)


# with Basic Authentication
sheet_response = requests.post(
  SHEET_ENDPOINT,
  json=sheet_inputs,
  auth=(
      USERNAME,
      PASSWORD,
  )
)

print(sheet_response.text)
