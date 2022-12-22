from django.views.generic import TemplateView

# from django.shortcuts import render
# beep boop


class MapView(TemplateView):
    template_name = "game/battlemap.html"
