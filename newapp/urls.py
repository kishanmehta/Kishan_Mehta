from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/",views.add,name="add"),
    path("addrec/",views.addrec,name="addrec"),
    path("details/<str:name>/delete/",views.delete,name="delete"),
    path("details/<str:name>/delete/deleterec/",views.deleterec,name="deleterec"),
    path("details/<str:name>/update/",views.update,name="update"),
    path("details/<str:name>/update/uprec/",views.uprec,name="uprec"),
    path("details/<str:name>/",views.details,name="details"),
]