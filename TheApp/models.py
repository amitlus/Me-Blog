from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, models.PROTECT)
# models.PROTECT is an on_delete value which protect the source model and if he is not existed or having a problem he raises an Error to alert us

    # additional
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='TheApp/profile_pics',blank=True)

    def __str__(self):
        return self.user.username
