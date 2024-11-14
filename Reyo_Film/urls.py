from django.contrib import admin
from django.urls import path, include
from Reyo_Film import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('account/', include("account.urls")),
    path('serial/', include("serial.urls")),
    path('blog/', include("blog.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
