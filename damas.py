import pygame
from pygame.version import ver

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
rosa= (255,203,219)

fps=60

vitoria = pygame.display.set_mode((largura, altura)) #Aqui é a configuração do display
pygame.display.set_caption("Jogo de Damas - Programação 1") #Aqui é o nome que vai aparecer na janela que abrir

class tabuleiro:
	def __init__(self):
		self.tabuleiro = []
		self.pecaSelecionada = None
		self.vermelhoEsquerda = self.azulEsquerda = 12
		self.rainhaVermelha = self.rainhaAzul = 0

	def cubosTabuleiro(self,vitoria):
		vitoria.fill(preto)
		for linha in range(linhas):
			for col in range(linha % 2,linhas,2):
				pygame.draw.rect(vitoria, vermelho, (linha*tamanhoTabuleiro, col*tamanhoTabuleiro, tamanhoTabuleiro, tamanhoTabuleiro))

	def criaçãoFundo(self):
		pass

class pecas:

	padding = 10
	bordas = 2

	def __init__(self, linha, col, cor):
		self.linha= linha
		self.col = col
		self.cor = cor
		self.rainha = False

		if self.cor == vermelho:
			self.direcao = -1
		else:
			self.direcao = 1
		
		self.x=0
		self.y=0
		self.posicao()
	
	def posicao(self):
		self.x = tamanhoTabuleiro * self.col + tamanhoTabuleiro // 2
		self.y= tamanhoTabuleiro * self.linha +tamanhoTabuleiro // 2

	def virarRainha(self):
		self.rainha = True

	def desenho(self, vitoria):
		raio = tamanhoTabuleiro//2 - self.padding
		pygame.draw.circle(vitoria, rosa, (self.x,self.y), raio + self.bordas)
		pygame.draw.circle(vitoria, self.cor, (self.x,self.y), raio )

	def __repr__(self):
		return str(self.cor)
		
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
	
	tabuleiro.desenharCubos(vitoria)
	pygame.display.update()

	pygame.QUIT()

loop()