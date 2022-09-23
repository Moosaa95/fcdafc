

from django.db import models
from django.db.models import Sum, Count,Q
from django.urls import reverse

# Create your models here.



class PlayerInfo(models.Model):
    
    POSITIONS = (
        ("STRIKER", "STRIKER"),
        ("MIDFIELD", "MIDFIELD"),
        ("DEFENDER", "DEFENDER"),
        ("GOALKEEPER", "GOALKEEPER")
    )
    STATES = (
        ("Adamawa", "Adamawa"),
        ("AkwaIbom", "AkwaIbom"),
        ("Abia", "Abia"),
        ("Anambra", "Anambra"),
        ("Bauchi", "Bauchi"),
        ("Bayelsa", "Bayelsa"),
        ("Benue", "Benue"),
        ("Borno", "Borno"),
        ("CrossRiver", "CrossRiver"),
        ("Delta", "Delta"),
        ("Edo", "Edo"),
        ("Ekiti", "Ekiti"),
        ("Enugu", "Enugu"),
        ("Ebonyi", "Ebonyi"),
        ("FCT", "FCT"),
        ("Gombe", "Gombe"),
        ("Imo", "Imo"),
        ("Jigawa", "Jigawa"),
        ("Kano", "Kano"),
        ("Kaduna", "Kaduna"),
        ("Katsina", "Katsina"),
        ("Kebbi", "Kebbi"),
        ("Kogi", "Kogi"),
        ("Kwara", "Kwara"),
        ("Lagos", "Lagos"),
        ("Nasarawa", "Nasarawa"),
        ("Niger", "Niger"),
        ("Ogun", "Ogun"),
        ("Ondo", "Ondo"),
        ("Osun", "Osun"),
        ("Oyo", "Oyo"),
        ("Plateau", "Plateau"),
        ("Rivers", "Rivers"),
        ("Sokoto", "Sokoto"),
        ("Taraba", "Taraba"),
        ("Yobe", "Yobe"),
        ("Zamfara", "Zamfara"),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    number = models.IntegerField()
    nationality = models.CharField(max_length=50)
    height = models.CharField(max_length=30, default='cm')
    weight = models.CharField(max_length=20, default='kg')
    states = models.CharField(max_length=50, choices=STATES)

    bio = models.TextField(max_length=300)
    words = models.CharField(max_length=200, blank=True)
    position = models.CharField(max_length=10, choices=POSITIONS)
    image =  models.ImageField(upload_to ='uploads/')


    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} - {self.email}'
    
    def get_absolute_url(self):
        return reverse("get_player_detail", kwargs={"pk": self.pk})
    


    
    @classmethod
    def get_players(cls, player_id=None):
        fields = [
            "first_name",
            "last_name",
            "email",
            "number",
            "nationality",
            "height",
            "weight",
            "states",
            "bio",
            "position",
            "image"
        ]
        try:
            if player_id:
                player = cls.objects.get(id=player_id).values(*fields)
            else:
                player = cls.objects.all().values(*fields)
        except:
            player = False 
        
        return player
    


class Team(models.Model):
    # TEAM_TYPE = (
    #     ("FCDA", "FCDA"),
    #     ("OPPONENT", "OPPONENT")
    # )

    name =  models.CharField(max_length=20, unique=True)
    # team_type = models.CharField(max_length=50, choices=TEAM_TYPE)
    location = models.CharField(max_length=200)
    coach = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Opponent(models.Model):
    name =  models.CharField(max_length=20, unique=True)
    # team_type = models.CharField(max_length=50, choices=TEAM_TYPE)
    location = models.CharField(max_length=200)
    coach = models.CharField(max_length=200)

    def __str__(self):
        return self.name


    # @classmethod
    # def get_opponent_team(cls, team_type='OPPONENT'):
    #     try:
    #         opponent = cls.objects.filter(team_type=team_type).order_by(
    #             "-created_at"
    #         )
    #     except:
    #         opponent = "not found"
    #     return opponent
    

class Match(models.Model):
    MATCH_TYPE = (
        ("MATCH", "MATCH"),
        ("TRAINING", "TRAINING")
    )

    match_date = models.DateTimeField()
    location = models.CharField(max_length=200)
    match_type = models.CharField(max_length=50, choices=MATCH_TYPE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    opponent = models.ForeignKey(Opponent, on_delete=models.CASCADE)
    
    # decided_by = models.CharField(max_length=200, blank=True)
    # available_players = models.ForeignKey(PlayerInfo, on_delete=models.SET_NULL)

    # def get_opp_team():
    #     opp = Team.objects.filter(team_type__icontains="opponet").values
    #     return opp[0]
    # @classmethod
    # def get_opponent(cls):
        # return cls.opponent.get_object()

    def __str__(self):
        # opp = self.get_opp_team()
        # print(opp, 'str')
        if self.match_type == "MATCH":
            title  = f"{self.team.name} vs {self.opponent.name} time : {self.match_date}"
        else:
            title  = f"{self.team.name} vs {self.team.name} time : {self.match_date}"
        return title 




class Card(models.Model):
    CARDS = (
        ("RED", "RED"),
        ("YELLOW", "YELLOW")
    )
    name = models.CharField(max_length=20, choices=CARDS)
    booked_player = models.ForeignKey(PlayerInfo, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} -- {self.booked_player}"

    # @classmethod
    # def get_booked_players_per_match(cls, match_id)

class Goals(models.Model):
    GOAL_TYPE = (
        ("OWN GOAL", "OWN GOAL"),
        ("NORMAL GOAL", "NORMAL GOAL")
    )
    goal = models.IntegerField()
    player = models.ForeignKey(PlayerInfo, on_delete=models.CASCADE)
    goal_type = models.CharField(max_length=20, choices=GOAL_TYPE)
    time = models.IntegerField(default=0)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.player.first_name} {self.player.last_name} {self.goal_type} goal: {self.goal}"

    # def __unicode__(self):
    #     return 

    @classmethod
    def get_goals_per_player(cls, player_id=None, goal_type='NORMAL GOAL'):
        try:
            player = cls.objects.filter(player_id=player_id, goal_type=goal_type).values("player__first_name", "player__number").count()
            
            return player
        except:
            return None
    
    @classmethod
    def goal_counts(cls, player_id=None):
        try:
            players = cls.objects.values("player__first_name", "player__last_name").annotate(goals=Count('player'))
            return players
        except cls.DoesNotExist:
            return 'not found'

class MatchDetail(models.Model):
    MATCH_SCHEDULE_TYPE = (
        ("MATCH", "MATCH"),
        ("TRAINING", "TRAINING")
    )
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    match_schedule_type = models.CharField(max_length=50, choices=MATCH_SCHEDULE_TYPE)
    # goal_score = models.ForeignKey(Goals, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    result = models.CharField(max_length=20, blank=True)
    player_of_the_match = models.CharField(max_length=200, blank=True)
    opponent = models.ForeignKey(Opponent, on_delete=models.CASCADE)



    def __str__(self):
        # opp = self.get_opp_team()
        # print(opp, 'str')
        if self.match_schedule_type == "MATCH":
            title  = f"{self.team.name} vs {self.opponent.name}"
        else:
            title  = f"{self.team.name} vs {self.team.name}"
        return title 