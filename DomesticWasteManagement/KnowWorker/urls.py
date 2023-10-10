from django.urls import path,include
from . import views
urlpatterns = [
    path('registerworker',views.RegisterWorker,name='registerworker'),
    path('searchworker',views.searchWorker,name='searchworker'),
    path('knowworkersubmodule',views.knowWorkerSubmodule,name='knowworkersubmodule')
]
