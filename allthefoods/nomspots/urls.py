from django.urls import path
from . import views

app_name = "nomspots"
urlpatterns = [
    path(
        route='',
        view=views.NomspotListView.as_view(),
        name='list'
    ),
    path(
        route='<slug:slug>/',
        view=views.NomspotDetailView.as_view(),
        name='detail'
    ),


]
