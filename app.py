from fastapi import FastAPI
from main import *
from app import *
import pickle

app = FastAPI()

# Loading the model here.
pickle_in = open("model.pkl", "rb")
classifier = pickle.load(pickle_in)

@app.get('/')
def test():
    return {'message': 'Call the `/predict` to start the prediction with the data.!'}

@app.post('/predict')
def predict(data : cancer_class):
    mean_radius = float(data.mean_radius)
    mean_perimeter = float(data.mean_perimeter)
    mean_area = float(data.mean_area)
    mean_compactness = float(data.mean_compactness)
    mean_concavity = float(data.mean_concavity)
    mean_concave_points = float(data.mean_concave_points)
    radius_error = float(data.radius_error)
    perimeter_error = float(data.perimeter_error)
    area_error = float(data.area_error)
    worst_radius = float(data.worst_area)
    worst_perimeter = float(data.worst_perimeter)
    worst_area = float(data.worst_area)
    worst_compactness = float(data.worst_compactness)
    worst_concavity = float(data.worst_concavity)
    worst_concave_points = float(data.worst_concave_points)
    prediction = int(classifier.predict([[mean_radius, mean_perimeter, mean_area, mean_compactness, mean_concavity, mean_concave_points, radius_error,
                                     perimeter_error, area_error, worst_radius, worst_perimeter, worst_area, worst_compactness, worst_concavity, worst_concave_points]]))
    return {"prediction": prediction}