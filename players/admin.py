from django.contrib import admin
from .models import PlayerInfo, Goals, Match, MatchDetail, Card, Team, Opponent
# Register your models here.


admin.site.register(PlayerInfo)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(MatchDetail)
admin.site.register(Goals)
admin.site.register(Card)
admin.site.register(Opponent)


