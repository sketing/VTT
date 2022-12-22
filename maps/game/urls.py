from django.urls import path

from maps.game.views import MapView

app_name = "game"
urlpatterns = [path("map", view=MapView.as_view())]
