from django.db import models





class PontoTuristico(models.Model):
    
    nome = models.CharField(max_length=150)
    descricao = models.TextField(max_length=15)



    def __str__(self):
        return self.nome
