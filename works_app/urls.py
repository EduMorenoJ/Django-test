from django.urls import path, include
from works_app.views import WorkListView, WorkViewSet, work_detail, work_list
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'works', WorkViewSet)

urlpatterns = [
    path('', WorkListView.as_view(), name='works_list'),
    path('api/works/docs', include(router.urls)),
    path('api/works/', work_list),
    path('api/works/<str:pk>/', work_detail),
]
