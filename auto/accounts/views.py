from django.contrib.auth import authenticate, login, get_user_model
from django.views.generic import CreateView, FormView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm, RegisterForm

# Create your views here.


class LoginView(View):
    form_class = LoginForm
    success_url = '/'
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print('already logged in. redirecting...')
            print(request.user)
            logout(request)
        form = LoginForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            request = self.request
            next_ = request.GET.get('next')
            next_post = request.POST.get('next')
            redirect_path = next_ or next_post or None
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                try:
                    del request.session['guest_email_id']
                except:
                    pass
                if is_safe_url(redirect_path, request.get_host()):
                    return redirect(redirect_path)
                else:
                    return redirect("/")
            return render(request, self.template_name, {'form': form})


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = '/login/'
