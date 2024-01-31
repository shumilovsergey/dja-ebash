from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    color = models.CharField(max_length=20, default="0")
    avarar = models.CharField(max_length=20, default="😎")
    wrong_password_count = models.IntegerField(default=0)
    auth_status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('user', )