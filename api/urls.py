from django.urls import path, include
from .views import GetUUID
urlpatterns = [
    path('getuuid/', GetUUID.as_view())
]
