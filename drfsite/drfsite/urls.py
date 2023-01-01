from django.contrib import admin
from django.urls import path, include

from pupils.views import *

from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'pupil', PupilsViewSet)
# router.register(r'pupil', PupilsViewSet, basename='pupil')



urlpatterns = [
    path('admin/', admin.site.urls),

    # routers
    path('api/v1/', include(router.urls)),

    # viewsets
    # path('api/v1/pupil-list/', PupilsViewSet.as_view({'get': 'list'})),
    # path('api/v1/pupil-list/<int:pk>/', PupilsViewSet.as_view({'put': 'update'})),

    # path('api/v1/pupil-list/', PupilsAPIList.as_view()),
    # path('api/v1/pupil-list/<int:pk>/', PupilsAPIUpdate.as_view()),
    # path('api/v1/pupil-detail/<int:pk>/', PupilsAPIDetail.as_view()),

    # базовый класс API
    # path('api/v1/pupil-list/', PupilsAPIView.as_view()),
    # path('api/v1/pupil-list/<int:pk>/', PupilsAPIView.as_view()),
]
