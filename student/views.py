from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, authenticate, logout
from .forms import UserAuthenticationForm


def loginView(request, *args, **kwargs):

    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("home")

    destination = get_redirect_if_exists(request)
    if request.POST:
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                destination = get_redirect_if_exists(request)
                if destination:
                    return redirect(destination)
                return redirect("home")
        else:
            context["login_form"] = form

    return render(request, 'login.html', context)


def registerView(request, *args, **kwargs):

    user = request.user
    if user.is_authenticated:
        return HttpResponse(f"You are already authenticated as {user.email}.")
    context = {}


    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = get_redirect_if_exists(request)


            if destination:
                return redirect(destination)
            return redirect("home")
        else:
            context['registration_form'] = form
    return render(request, 'register.html')


    
def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get("next"):
            redirect = str(request.GET.get("next"))



def logoutView(request):
    logout(request)
    return redirect("home")


def addCreditCard(request):

    return render(request, 'connect-credit-card-view.html')

def addBank(request):    
    return render(request, 'connect-bank-view.html')


def studentView(request):
    return render(request, 'student.html')

def accountSettings(request):
    return render(request, 'account-settings.html', {'user':request.user})

def applyFirst(request):
    return render(request, 'first-apply-form.html', {'user':request.user})

def applySecond(request):
    return render(request, 'second-apply-form.html', {'user':request.user})

def applyThird(request):
    return render(request, 'third-apply-form.html', {'user':request.user})


def successMessage(request):
    return render(request, 'apply-success.html', {'user':request.user})
