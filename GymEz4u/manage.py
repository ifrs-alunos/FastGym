#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GymEz4u.settings')

from futebol.models.jogador import Jogador
from futebol.models.base import *


ricardo = Jogador(1, "Ricardo", "Ricardão", 2000, 2, 4, 1, "Goleiro", 90, 0, False)
ronaldo = Jogador(2, "Ronaldo", "Ronaldão", 1971, 10, 6, 2, "Zagueiro", 60, 0, False)
robson = Jogador(3, "Robson", "Robi", 1967, 5, 7, 3, "Zagueiro", 70, 0, False)
richard = Jogador(4, "Richard", "Rich", 1990, 12, 3, 4, "Zagueiro", 80, 0, False)
rian = Jogador(5, "Rian", "Ri", 1982, 12, 10, 8, "Centroavante", 90, 0, False)
ruan = Jogador(6, "Ruan", "Ru", 1972, 10, 20, 5, "Lateral", 50, 0, False)
roberto = Jogador(7, "Roberto", "Robe", 1962, 2, 4, 6, "Lateral", 80, 0, False)
rafael = Jogador(8, "Rafael", "Rafa", 2000, 2, 4, 7, "Zagueiro", 70, 0, False)
reginaldo = Jogador(9, "Reginaldo", "Regi", 2000, 2, 4, 9, "Atacante", 80, 0, False)
rocao = Jogador(10, "Rocao", "Roc", 2000, 2, 4, 10, "Atacante", 100, 0, False)
rampaneli = Jogador(11, "Rampaneli", "Rampa", 2000, 2, 8, 11, "Atacante", 90, 0, False)
joao = Jogador(12, "João", "Jão", 2000, 2, 4, 1, "Goleiro", 80, 0, False)
jorge = Jogador(13, "Jorge", "Jorge", 2000, 2, 4, 20, "Atacante", 60, 0, False)
joze = Jogador(14, "Jozé", "zé", 2000, 2, 4, 15, "Zagueiro", 50, 0, False)
jean = Jogador(15, "Jean", "Jeje", 2000, 2, 4, 16, "Zagueiro", 40, 0, True)
joseph = Jogador(16, "Joseph", "Joph", 2000, 2, 4, 17, "Centroavante", 60, 0, False)
carlos = Jogador(17, "Carlos", "Carlinhos", 2000, 2, 4, 22, "Lateral", 70, 0, False)
david = Jogador(18, "David", "Dav", 2000, 2, 4, 23, "Lateral", 60, 0, True)

jogador = [ricardo, ronaldo, robson, richard, rian, ruan, roberto, rafael, reginaldo, rocao, rampaneli, joao, jorge, joze, jean, joseph, carlos, david]

for x in jogador:
    print(x)

def jogo():
    funcaojogo = input('Escolha a opção:\n\n 1) Adicionar Jogador:\n 2) Adicionar Time\n3)Informações jogadores de um time\n4)Informações times')
    if funcaojogo == '1':
        nome = input('Nome:')
        apelido = input('Apelido:')
        ano = input('Ano de nascimento:')
        mes = input('Mês de nascimento:')
        dia = input('Dia de nascimento:')
        num = input('Número:')
        posicao = input('Posição:\n\n 1) Goleiro\n 2) Atacante\n 3) Centro-Avante\n 4) Zagueiro\n 5) Lateral Esquerdo\n 6) Lateral Direito')
        qualidade= input('Qualidade entre 0-100:')
        cartoes = input('Quantidade de cartões recebidos')
        suspenso = input('Jogador suspenso?\n\n 1) sim\n 2)não')

        if posicao == '1':
            stat = 'Goleiro'
        elif posicao =='2':
            stat = 'Atacante'
        elif posicao == '3':
            stat = 'Centro-Avante'
        elif posicao == '4':
            stat = 'Zagueiro'
        elif posicao == '5':
            stat = 'Lateral Esquerdo'
        else:
            stat = 'Lateral Direito'
        
        if suspenso == "1":
            suspensao = True
        else:
            suspensao = False