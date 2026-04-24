from django.urls import path
from . import views


urlpatterns=[
    path("create",views.create,name="create"),
    path("getList",views.get_list,name="create"),
    path("deleteOne",views.delete_one,name="create"),
    path("updateOne",views.update_one,name="create"),
]