from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.messages import get_messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView

from account.forms import RegistrationForm, CustomAuthenticationForm, UserUpdateForm
from account.models import User


class AccountLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = "account/login.html"


def custom_login(request):
    form = CustomAuthenticationForm(request.POST or None)
    if form.is_valid():
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username is not None and password:
            user = authenticate(
                request, username=username, password=password
            )
            login(request, user)
            return redirect("account:profile")
    return render(request, "account/login.html", {"form": form})


class RegisterView(CreateView):
    model = User
    template_name = 'account/register.html'
    form_class = RegistrationForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")
            user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
            login(request, user)
            return redirect("homepage")
        return render(request, "account/register.html", {"form": form, 'messages': get_messages(request)})


class UserProfile(DetailView, LoginRequiredMixin):
    model = User
    pk_url_kwarg = None
    query_pk_and_slug = None

    def get_queryset(self):
        return self.request.user


@login_required
def profile(request):
    return render(request, "account/profile.html", {"user": request.user})


class UserProfileUpdate(UpdateView, LoginRequiredMixin):
    model = User
    form_class = UserUpdateForm
    template_name = "account/profile_edit.html"
    success_url = reverse_lazy("account:profile")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context

    def put(self, *args, **kwargs):
        form = self.form_class(self.request.POST or None, self.request.FILES or None)
        if form.is_valid():
            form.save()
        return render(self.request, "account/profile_edit.html", {"form": form})
