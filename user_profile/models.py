from django.db import models
from django.contrib.auth.models import User
from ebash.const import AVATARS
from ebash.const import COLORS

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_name = models.CharField(max_length=20, default="user")
    color = models.IntegerField(choices=COLORS, default=0)
    avatar = models.IntegerField(choices=AVATARS, default=0)


    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('user', )
