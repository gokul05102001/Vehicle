from django.contrib import admin
from django.urls import path
from . import views
app_name='vehicleapp'
urlpatterns = [
    path('',views.home,name='home'),
    path('details/<int:vehicles_id>/',views.details,name='details'),
    path('add/',views.add_vehicle,name='add_vehicle'),
    path('updates/<int:id>/',views.updates,name='updates'),
    path('delete/<int:id>/',views.delete,name='delete')

]
