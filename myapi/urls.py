# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
#router.register(r'heroes', views.HeroViewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('index/',views.index),
    path('para_view/',views.ParaView, name="summary"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
