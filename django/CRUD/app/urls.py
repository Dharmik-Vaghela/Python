from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.InsertPage,name="insertpage"),
    path("insert/",views.InsertData,name="insert"),
    path("showdata/",views.ShowData,name="showdata"),
    path("editpage/<int:pk>",views.EditPage,name="editpage"),
    path("updatedata/<int:pk>",views.UpdateData,name="updatedata"),
    path("delete/<int:pk>",views.DeleteData,name="delete")
]