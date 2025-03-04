from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm,EmailAuthenticationForm
from django.views.generic import CreateView
from django.views.generic import TemplateView

class SignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('base')  # تغییر مسیر به صفحه اصلی پس از ثبت‌نام
    template_name = 'registration/signup.html'
    

    def signup(request):
        if request.method == 'post':
            form = CustomUserCreationForm(request.post)
            if form.is_valid():
                form.save()
                return redirect('base')
        else:
            form = CustomUserCreationForm()
        return render(request,'signup.html' , {'form':form} )

class CustomLoginView(View):
    def get(self, request):
        form = EmailAuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request):
        form = EmailAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('base')
        return render(request, 'registration/login.html', {'form': form})


    