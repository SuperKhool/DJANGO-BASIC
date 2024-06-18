from django.urls import path
from .views import employees_detail
urlpatterns = [
    path('<int:pk>',employees_detail,name='employes_details')

]