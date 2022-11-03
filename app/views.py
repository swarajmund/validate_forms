from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.forms import *

def validate_forms(request):
    sf = StudentForm()
    d = {'form':sf}
    if request.method == 'POST':
        form_data = StudentForm(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))
    return render(request,'validate_forms.html',d)