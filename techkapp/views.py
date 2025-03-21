from django.shortcuts import render
from django.http import JsonResponse
import pickle
import os
import numpy as np
from django.conf import settings
from django.shortcuts import redirect

def redirect_to_app(request):
    return redirect("https://unrivaled-wisp-9b8fe6.netlify.app")


# # Load ML models
# def load_model(filename):
#     model_path = os.path.join(settings.BASE_DIR, 'techkapp/ml_models', filename)
#     with open(model_path, 'rb') as file:
#         return pickle.load(file)

# crop_recommender = load_model('crop_recommender.pkl')
# # yield_predictor = load_model('yield_predictor.pkl')
# label_encoder = load_model('label_encoder.pkl')
# scaler = load_model('scaler.pkl')

# Home Page
def home(request):
    return render(request, 'home.html')

# Crop Recommendation Page
def crop(request):
    return render(request, 'crop.html')

# def crop_recommend(request):
#     return render('https://unrivaled-wisp-9b8fe6.netlify.app')

# Predict Crop based on user input
# def predict_crop(request):
#     if request.method == 'POST':
#         soil_type = request.POST.get('soil_type')  # Assuming soil type is categorical
#         rainfall = float(request.POST.get('rainfall'))
#         temperature = float(request.POST.get('temperature'))

#         # Encode soil type (if label encoding is needed)
#         soil_type_encoded = label_encoder.transform([soil_type])[0]

#         # Prepare input data
#         input_data = np.array([[soil_type_encoded, rainfall, temperature]])
#         input_data = scaler.transform(input_data)  # Scale the input

#         # Predict crop
#         prediction = crop_recommender.predict(input_data)
#         crop_name = label_encoder.inverse_transform(prediction)[0]

#         return render(request, 'report.html', {'recommended_crop': crop_name})

#     return render(request, 'crop.html')

# # Predict Yield (if required)
# def predict_yield(request):
#     if request.method == 'POST':
#         features = [float(request.POST.get(param)) for param in ['feature1', 'feature2', 'feature3']]  # Replace with actual feature names
        
#         # Prepare input data
#         input_data = np.array([features])
#         input_data = scaler.transform(input_data)

#         # Predict yield
#         # yield_prediction = yield_predictor.predict(input_data)[0]

#         # return JsonResponse({'predicted_yield': yield_prediction})

#     return render(request, 'crop_tips.html')

def crop_tips(request):
    return render(request,'crop_tips.html')

def weather(request):
    return render(request,'weather.html')

def counter(request):
    text = request.GET['text']
    text1 = request.GET['text1']
    text2 = request.GET['text2']
    text3 = request.GET['text3']
    text4 = request.GET['text4']
    text5 = request.GET['text5']
    text6 = request.GET['text6']
    return render(request,'crop.html')
