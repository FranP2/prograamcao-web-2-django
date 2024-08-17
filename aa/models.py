from django.db import models

# Create your models here.
# Estado tem um relacionamento de muitos para muitos com Cidade
class Estado(models.Model):
    nome = models.CharField(max_length=100)
    cidades = models.ManyToManyField('Cidade')

    def _str_(self):
        return self.nome


# Cidade tem um relacionamento de muitos para um com Estado
class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    populacao = models.PositiveIntegerField()

    def _str_(self):
        return f"{self.nome} (população: {self.populacao})"


# Capital tem um relacionamento de um para um com Cidade
class Capital(models.Model):
    cidade = models.OneToOneField(Cidade, on_delete=models.CASCADE)

    def _str_(self):
        return f"Capital de {self.cidade.nome}"


# Pessoa sem relacionamento
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)

    def _str_(self):
        return self.nome