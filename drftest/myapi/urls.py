from django.urls import include, path
from rest_framework import routers
from myapi import views

router = routers.DefaultRouter()
router.register(r'student', views.StudentViewSet,basename='studentapi')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    # path('',views.StudentViewSet.as_view(),name='student_api'),
    # path('<int:pk>',views.StudentViewSet.as_view(),name='student'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]