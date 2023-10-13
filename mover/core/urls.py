
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("mover.urls")),
    path("accounts/", include("django.contrib.auth.urls"))
]

if settings.DEBUG:
    # Add URLs for debugging purposes
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),

    ]
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
