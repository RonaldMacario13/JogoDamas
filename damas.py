import pygame
from pygame import event

#Configuração de tela/tabuleiro
largura,altura=720,600
linhas,colunas=8,8
tamanhoTabuleiro=largura//colunas

#Declaração das cores
branco= (255,255,255)
preto= (0,0,0)
vermelho= (173,19,31)
azul=(3,73,122)
verde=(0,169,130)

fps=60

vitoria= pygame.display.set_mode((largura, altura)) #Aqui é a configuração do display
pygame.display.set_caption("Jogo de Damas - Programação 1") #Aqui é o nome que vai aparecer na janela que abrir

class tabuleiro:
	def __init__(self):
		self.tabuleiro = []
		self.pecaSelecionada = None
		self.vermelhoEsquerda = self.azulEsquerda = 12
		self.rainhaVermelha = self.rainhaAzul = 0

	def cubosTabuleiro(self,vitoria):
		win.fill(preto)




def loop(): #Função que mantém o programa aberto
	manterAberto=True
	limitarFps=pygame.time.Clock()
	while manterAberto:
		limitarFps.tick(fps)
		pass

	for fechar in pygame.event.get():
		if fechar.type==pygame.QUIT:
			manterAberto=False

		if fechar.type == pygame.MOUSEBUTTONDOWN:
			pass

	pygame.QUIT()

loop()