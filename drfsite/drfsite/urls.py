from django.contrib import admin
from django.urls import path

from pupils.views import PupilsAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/pupil-list/', PupilsAPIView.as_view()),
    path('api/v1/pupil-list/<int:pk>/', PupilsAPIView.as_view()),
]
