from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from compat import JsonResponse

from players.models import PlayerInfo 


class GetPlayerAPIView(APIView):


    def get(self, request, **kwargs):
        player_id = request.data.get("id", None)
        player_iid = request.data
        print('begin')
        for i in player_iid:
            print(i, '-=-=-=-=')
        print(player_id, '================')
        if player_id:
            player_data = PlayerInfo.get_players(player_id=player_id)
        else:
            player_data = PlayerInfo.get_players()
        return Response(data=player_data, status=status.HTTP_200_OK)
