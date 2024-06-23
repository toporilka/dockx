from django.db import models

# Create your models here.
class User(models.Model):
    class Meta():
        verbose_name = 'Пользователи'
        ordering = ['-id_user']
    id_user = models.IntegerField(null=False, primary_key=True, db_index=True)
    
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
    class Meta():
        verbose_name = 'Клиент'
        ordering = ['-id_client']
    id_client = models.IntegerField(null=False, primary_key=True, db_index=True)

    name_client = models.CharField(max_length=100,
                            null=False)
    second_name_client = models.CharField(max_length=100,
                                   null=False)
    id_user = models.ForeignKey('User',
                                null=False,
                                on_delete=models.CASCADE)
    status = models.CharField(max_length=40,
                            default="Не в работе",
                            choices={("Не в работе", "Не в работе"),
                                    ("В работе", "В работе"),
                                    ("В архиве", "В архиве")},
                            null=False)
    def __str__(self) -> str:
        return str(self.id_client)