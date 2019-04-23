
# File: views.py
# Project: Social-Media-Analysis
# Team: Bayer-Social-Media-Analysis
# Programmer: Carl Grissom
# Description: 



from django.shortcuts import render_to_response

def index(request):
    return render_to_response('sentiment/index.html' )
