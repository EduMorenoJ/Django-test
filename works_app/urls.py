from django.urls import path, include
from works_app.views import WorkListView, WorkViewSet, WorkDetail, WorkList
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'works', WorkViewSet)

urlpatterns = [
    path('', WorkListView.as_view(), name='works_list'),
    path('api/works/docs', include(router.urls)),
    path('api/works/', WorkList.as_view()),
    path('api/works/<str:pk>/', WorkDetail.as_view()),
]
