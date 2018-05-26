from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm

def _form_view(request, template_name, form_class=ContactForm):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = form_class()
    return render(request, template_name, {'form': form})
    #return HttpResponseRedirect("http://youtube.com/")


def new_form(request):
    return _form_view(request, template_name='new_form.html')