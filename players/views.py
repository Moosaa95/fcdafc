from multiprocessing import context

from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView 
from .models import PlayerInfo

# Create your views here.

class HomeView(View):
    template = "index.html"
    context = {}
    
    def get(self, request, *args, **kwargs):
        players = PlayerInfo.objects.all()
        self.context["players"] = players
        return render(request, self.template, self.context)


class PlayerDetailView(View):
    template = "player_detail.html"
    context = {}
    def get(self, request, *args, **kwargs):
        return render(request, self.template, self.context)



class PlayerDetail(DetailView):
    model = PlayerInfo
    template_name='player_details.html'
    context_object_name = 'player'
    # slug_field: str

