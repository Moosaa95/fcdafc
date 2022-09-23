from multiprocessing import context
from wsgiref.util import request_uri

from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView 
from .models import PlayerInfo, Team, Opponent, Match, MatchDetail, Goals

# Create your views here.

class HomeView(View):
    template = "index.html"
    context = {}
    
    def get(self, request, *args, **kwargs):
        players = PlayerInfo.objects.all()
        matches = Match.objects.all().order_by("-match_date")
        lastest_match = Match.objects.latest('match_date')
        goal = Goals.goal_counts()
        
        self.context["players"] = players
        self.context.update({"matches":matches})
        self.context.update({"lastest_match":lastest_match})
        self.context.update({"goals":goal})

        # self.context["matches"] = matches
        print(self.context, 'poopppp')
        return render(request, self.template, self.context)
    
    def post(self, request, *args, **kwargs):
        player_id = request.data.get("player_id", None)
        print(player_id)
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

