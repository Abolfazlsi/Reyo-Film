from django.urls import path, re_path
from blog import views

app_name = "blog"
urlpatterns = [
    re_path(r"blog-detail/(?P<slug>[-\w]*)/", views.BlogDetailsView.as_view(), name="blog_details"),
    path("blog-list/", views.BlogListView.as_view(), name="blog_list"),
]
