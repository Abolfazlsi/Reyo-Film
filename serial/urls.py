from django.urls import path, re_path
from serial import views

app_name = "serial"
urlpatterns = [
    re_path(r"serial-detail/(?P<slug>[-\w]*)/", views.SerialDetailView.as_view(), name="serial_detail"),
    re_path(r"serial-rating/(?P<slug>[-\w]*)/", views.SerialRatingsView.as_view(), name="serial_rating"),
    re_path(r"serial-download/(?P<slug>[-\w]*)/", views.SerialDownload.as_view(), name="serial_download"),
    path("serials-list/", views.SerialListView.as_view(), name="serials_list"),
    path("search/", views.SearchView.as_view(), name="search"),
    re_path(r"category/(?P<slug>[-\w]*)/", views.CategoryDetailView.as_view(), name="category_detail"),
]
