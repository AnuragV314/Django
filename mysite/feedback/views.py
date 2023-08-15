from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import FeedbackForm
# Create your views here.

def feedback(request):
    if request.method =='POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['email'])
            print('data saved.')
        else:
            return render(request, "feedback/home.html", {'form':form})
    else:
        form = FeedbackForm()

        return render(request, "feedback/home.html", {'form':form})



