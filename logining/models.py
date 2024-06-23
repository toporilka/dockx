from django.db import models

# Create your models here.
class User(models.Model):

    id_user = models.IntegerField(null=False, primary_key=True)
    
    email_user = models.EmailField()
    
    password_user = models.CharField(max_length=250,
                                    null=False,
                                    blank=False)
    tag_user = models.CharField(max_length=100,
                                null=False,
                                blank=False)

    def __str__(self) -> str:
        return str(self.id_user)
    
class Client(models.Model):
    id_client = models.IntegerField(null=False, primary_key=True)

    name_client = models.CharField(max_length=100,
                            null=False)
    second_name_client = models.CharField(max_length=100,
                                   null=False)
    id_user = models.ForeignKey('User',
                                null=False,
                                unique=True,
                                on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.id_client)