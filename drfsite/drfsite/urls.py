from django.contrib import admin
from django.urls import path, include, re_path

from pupils.views import *

from rest_framework import routers


# router = routers.SimpleRouter()
# router.register(r'pupil', PupilsViewSet)
# # router.register(r'pupil', PupilsViewSet, basename='pupil')



urlpatterns = [
    path('admin/', admin.site.urls),

    # session-based authentication
    path('api/v1/drf-auth/', include('rest_framework.urls')),

    # routers
    # path('api/v1/', include(router.urls)),

    # adding 3 urls for better understanding how to work permissions
    path('api/v1/pupil/', PupilAPIList.as_view()),
    path('api/v1/pupil/<int:pk>/', PupilAPIUpdate.as_view()),
    path('api/v1/pupil-delete/<int:pk>/', PupilAPIDestroy.as_view()),

    # viewsets
    # path('api/v1/pupil-list/', PupilsViewSet.as_view({'get': 'list'})),
    # path('api/v1/pupil-list/<int:pk>/', PupilsViewSet.as_view({'put': 'update'})),

    # path('api/v1/pupil-list/', PupilsAPIList.as_view()),
    # path('api/v1/pupil-list/<int:pk>/', PupilsAPIUpdate.as_view()),
    # path('api/v1/pupil-detail/<int:pk>/', PupilsAPIDetail.as_view()),

    # базовый класс API
    # path('api/v1/pupil-list/', PupilsAPIView.as_view()),
    # path('api/v1/pupil-list/<int:pk>/', PupilsAPIView.as_view()),

    # authentication
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
