from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, DetailView, ListView
from blog.models import Blog, Comment


class BlogDetailsView(DetailView):
    model = Blog
    template_name = "blog/blog_details.html"

    def post(self, request, slug):
        blog = get_object_or_404(Blog, slug=slug)
        text = request.POST.get("text")
        parent_id = request.POST.get("parent_id")
        if request.user.is_authenticated:
            comment = Comment.objects.create(blog=blog, text=text, user=request.user, parent_id=parent_id)
            return JsonResponse({
                "status": "success",
                "comment_text": comment.text,
                "user_username": comment.user.username,
                "user_profile_image": comment.user.profile_image.url,
                "created_at": comment.created_at
            })


class BlogListView(ListView):
    model = Blog
    template_name = "blog/blog_list.html"
    paginate_by = 18
