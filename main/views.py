from django.shortcuts import render
from .models import Bio
from .forms import InterestForm

def main(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def interest(request):
    context = {}

    form = InterestForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            # save the form data to model
            form.save()
            notes = Bio.objects.all()
            response = {'notes': notes}
            return render(request, 'lab4_index.html', response)

    context['form'] = form
    return render(request, "lab4_form.html", context)


