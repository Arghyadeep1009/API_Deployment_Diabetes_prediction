# Diabetes Prediction API

This repository contains the code for a FastAPI-based web service for predicting diabetes in women using a trained machine learning model. The service accepts input parameters through a POST request and returns a prediction indicating whether the person is diabetic or not. The model is exposed both locally and publicly using ngrok.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Example Request](#example-request)
- [Dependencies](#dependencies)

## Installation

To run the Diabetes Prediction API, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/diabetes-prediction-api.git
   cd diabetes-prediction-api
   ```

2. **Install the required Python packages:**
   ```bash
   pip install fastapi uvicorn pickle5 pydantic scikit-learn requests pyngrok nest-asyncio
   ```

3. **Ensure you have the trained model saved as `trained_model.sav` in the root directory of the project.**

## Usage

### Running the API locally

1. **Start the FastAPI server:**
   ```bash
   uvicorn main:app --reload
   ```

2. **The API will be accessible at `http://127.0.0.1:8000`**

### Running the API publicly using ngrok

1. **Set your ngrok authtoken:**
   ```bash
   ngrok authtoken <YOUR_NGROK_AUTH_TOKEN>
   ```

2. **Run the API with ngrok tunneling:**
   ```bash
   python main.py
   ```

3. **The public URL for the API will be printed in the console output.**

## API Endpoints

### `POST /women_diabetes_prediction`

Predicts whether a person is diabetic based on input parameters.

#### Request Body

The request body should be a JSON object with the following fields:

- `Pregnancies`: int
- `Glucose`: int
- `BloodPressure`: int
- `SkinThickness`: int
- `Insulin`: int
- `BMI`: float
- `DiabetesPedigreeFunction`: float
- `Age`: int

#### Response

The response will be a string indicating whether the person is diabetic or not.

- `"The person is not diabetic"`
- `"The person is diabetic"`

## Example Request

You can use the following example to test the API:

### Using `requests` library in Python

```python
import json
import requests

url = 'http://127.0.0.1:8000/women_diabetes_prediction' # for local
# url = 'https://<your-ngrok-url>/women_diabetes_prediction' # for public using ngrok

input_data = {
    'Pregnancies': 1,
    'Glucose': 85,
    'BloodPressure': 66,
    'SkinThickness': 29,
    'Insulin': 0,
    'BMI': 26.6,
    'DiabetesPedigreeFunction': 0.351,
    'Age': 31
}

input_json = json.dumps(input_data)
response = requests.post(url, data=input_json)

print(response.text)
```

## Dependencies

- `fastapi`
- `uvicorn`
- `pickle5`
- `pydantic`
- `scikit-learn`
- `requests`
- `pyngrok`
- `nest-asyncio`

Install these dependencies using `pip`:

```bash
pip install fastapi uvicorn pickle5 pydantic scikit-learn requests pyngrok nest-asyncio
```

## Acknowledgements

Special thanks to the developers of FastAPI, scikit-learn, and ngrok for providing the tools and libraries used in this project.
