from django.db import models
import datetime

class Jogador(models.Model):
    """Docstring for Jogador"""
    identificacao = models.AutoField()
    nome = models.CharField()
    apelido = models.CharField()
    data_nascimento = models.DateField()
    numero = models.IntegerField()
    posicao = models.CharField()
    qualidade = models.IntegerField()
    cartoes = models.IntegerField()
    suspencao = models.BooleanField(null=False)
    time = models.ForeignKey('Time', models.SET_NULL, null=True)

    def __str__(self):
        retorno = "{}: {} - {} ({}) - {} CONDIÇÃO: {}".format(self.posicao, self.numero, self.nome, self.apelido, self.data_nascimento, self.suspenso)
        return retorno

    def verificar_condicao_jogo(self):
        if self.cartoes >= 3:
            return True
        else:
            return False

    def aplicar_cartao(self, quantidade):
        self.quantidade = quantidade
        self. cartoes += self.quantidade
        return self.cartoes     

    def cumprir_suspencao(self):
        self.cartoes = 0
        self.suspenso = False