from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, View, UpdateView
from account.models import User
from account.forms import RegisterForm, LoginForm, UserEditForm
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import reverse_lazy


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = "account/register.html"
    success_url = reverse_lazy("account:login")


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home:home")
        form = LoginForm()
        return render(request, "account/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"]
            )
            if user is not None:
                login(request, user)
                return redirect("home:home")
            else:
                form.add_error("username", "this user does not exists")
        return render(request, "account/login.html", {"form": form})


def log_out(request):
    logout(request)
    return redirect("home:home")


class PasswordReset(PasswordResetView):
    template_name = "account/password_reset_form.html"
    success_url = reverse_lazy("account:password_reset_done")


class PasswordResetDone(PasswordResetDoneView):
    template_name = "account/password_reset_done.html"


class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = "account/password_reset_confirm.html"
    success_url = reverse_lazy("account:password_reset_complete")


class PasswordResetComplete(PasswordResetCompleteView):
    template_name = "account/password_reset_complete.html"


class UserEditView(View):
    def get(self, request):
        if request.user.is_anonymous:
            return redirect("account:login")
        user = request.user
        form = UserEditForm(instance=user)
        if request.user.is_authenticated:
            return render(request, "account/user_edit.html", {"form": form})

    def post(self, request):
        user = request.user
        form = UserEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("account:user-_profile")
        return render(request, "account/user_edit.html", {"form": form})
