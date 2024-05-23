
import json
import requests

url = 'https://bc58-34-42-254-168.ngrok-free.app/women_diabetes_prediction' # for public api using ngrok
# url = 'http://127.0.0.1:8000/women_diabetes_prediction' (for local api)

input_data={
    
    'Pregnancies' : 1,
    'Glucose' : 85,
    'BloodPressure' : 66 ,
    'SkinThickness' : 29,
    'Insulin' : 0,
    'BMI' : 26.6,
    'DiabetesPedigreeFunction' :  0.351,
    'Age' : 31

    } 

input_json = json.dumps(input_data)
response = requests.post(url, data = input_json)

print(response.text)
