from django.urls import include, path
from rest_framework import routers
from genericview import views

router = routers.DefaultRouter()
# router.register(r'course', views.CourseViewSet,basename='genericview-detail')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    path('',views.CourseListCreateAPIView.as_view(),name='student_api'),
    path('<slug:slug>/',views.CourseRetrieveUpdateDestroyAPIView.as_view(),name='genericview-detail'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]