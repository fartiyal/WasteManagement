from django.urls import path,include
from . import views
urlpatterns = [
    path('segrategarbage',views.segrateGarbage,name='segrateGarbage'),
    
]
