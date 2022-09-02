import email
from operator import mod
from pyexpat import model
from turtle import position
from django.db import models
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