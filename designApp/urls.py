from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("contact",views.contact_us,name="contact"),
    path("items",views.items,name="items"),
    path("systems",views.systems,name="systems"),
    path("systemView/<int:id>",views.systemView,name="systemView"),
]

#Django Admin SuperUser details = Name: shivam , Password: shivam
# check contacts table in it