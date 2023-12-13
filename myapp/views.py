from django.shortcuts import render
from django.http import HttpResponse
import joblib
import numpy as np

# Create your views here.
def home(request):
    return render(request,'index.html')
def cancerForm(request):
    return render(request,'cancer_form.html')
def prediction(request):
    model = joblib.load('E:\cancerPredictionSystemProject\cancerPrediction\myapp\predictmodel.joblib')
    if request.method=='POST':
        user_deatils=[
            int(request.POST['age']),
            int(request.POST['gender']),
            int(request.POST['air_pollution']),
            int(request.POST['alcohol_use']),
            int(request.POST['dust_allergy']),
            int(request.POST['occupational_hazards']),
            int(request.POST['genetic_risk']),
            int(request.POST['chronic_lung_disease']),
            int(request.POST['balanced_diet']),
            int(request.POST['obesity']),
            int(request.POST['smoking']),
            int(request.POST['passive_smoking']),
            int(request.POST['chest_pain']),
            int(request.POST['coughing_of_blood']),
            int(request.POST['fatigue']),
            int(request.POST['weight_loss']),
            int(request.POST['shortness_of_breath']),
            int(request.POST['wheezing']),
            int(request.POST['swallowing_difficulty']),
            int(request.POST['clubbing_of_fingernails']),
            int(request.POST['frequent_cold']),
            int(request.POST['dry_cough']),
            int(request.POST['snoring']),
        ]
        prediction=model.predict([user_deatils])
        return render(request,'cancer_result.html',{'result':prediction[0]})
    return render(request,'index.html')