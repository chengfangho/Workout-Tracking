import requests
import datetime
import os

APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']

GENDER = "male"
WEIGHT_KG = "60"
HEIGHT_CM = "173"
AGE = "24"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_text = input("Tell me which exercises you did: ")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/<ID>/myWorkouts/workouts"

date = datetime.datetime.now().strftime("%m/%d/%Y")
time = datetime.datetime.now().strftime("%X")

exercise_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

exercise_response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
exercise_result = exercise_response.json()

for exercise in exercise_result["exercises"]:
    sheet_params = {
        'workout': {
            'date': date,
            'time': time,
            'exercise': exercise["name"].title(),
            'duration': exercise["duration_min"],
            'calories': exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(url=sheet_endpoint, json=sheet_params)
    print(sheet_response.text)
