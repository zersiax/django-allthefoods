from django.urls import path
from . import views

app_name = "nomspots"
urlpatterns = [
    path(
        route='',
        view=views.NomspotListView.as_view(),
        name='list'
    )

]
