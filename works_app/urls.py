from django.urls import path, include
from works_app.views import WorkListView, WorkViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'works', WorkViewSet)

urlpatterns = [
    path('', WorkListView.as_view(), name='works_list'),
    path('api/', include(router.urls)),
]
