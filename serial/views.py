from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, TemplateView, CreateView, View
from serial.models import Serial, SerialRating, Comment, Category
from account.models import User
from serial.forms import CommentForm
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.views import PasswordResetView


class SerialDetailView(DetailView):
    model = Serial
    template_name = "serial/serial_detail.html"

    def post(self, request, slug):
        text = request.POST.get("text")
        serial = get_object_or_404(Serial, slug=slug)
        if request.user.is_authenticated:
            add_comment = Comment.objects.create(user=request.user, text=text, serial=serial)
            return JsonResponse({
                "status": "success",
                "comment_text": add_comment.text,
                "user_username": add_comment.user.username,
                "user_profile_image": add_comment.user.profile_image.url,
                "created_at": add_comment.time_since_creation()
            })

    def get_context_data(self, **kwargs, ):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            if self.request.user.ratings.filter(serial=self.object, user=self.request.user).exists():
                context["is_rate"] = True
            else:
                context["is_rate"] = False

        return context


class SerialRatingsView(View):
    def get(self, request, slug):
        serial = get_object_or_404(Serial, slug=slug)
        try:
            rating = SerialRating.objects.get(serial=serial, user=request.user)
            rating.delete()
            return JsonResponse({"response": "on_rating"})
        except:
            SerialRating.objects.create(serial=serial, user=request.user)
            return JsonResponse({"response": "rating"})


class SerialDownload(DetailView):
    model = Serial
    template_name = "serial/serial_download.html"


class SerialListView(ListView):
    model = Serial
    template_name = "serial/serials_list.html"
    paginate_by = 18


class SearchView(ListView):
    model = Serial
    template_name = "serial/serials_list.html"

    def get_queryset(self):
        q = self.request.GET.get("q")
        if q:
            return Serial.objects.filter(title__icontains=q)
        return Serial.objects.all()


class CategoryDetailView(ListView):
    model = Category
    template_name = "serial/serials_list.html"

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        return Serial.objects.filter(category__slug=slug)
