def menu():

	print ("menu de opções\n")
	print ("1 - Inserir;")
	print("2 - atualizar;")
	print("3 - remover;")
	print("sair. \n")
menu()


def menu(c = '-'):
	print (c*15)
	print ("Menu de opções")
	print (c*15)
	print ("1 - Inserir")
	print ("2 - atualizar")
	print ("3 - remover")
	print ("4 - sair")
	print (c*15)
menu()

def soma(a,b):
	print("Valor de %d + %d = %d" %(a, b, a+b))
soma(5,10)

def media_lista(lista):
	media = sum(lista)/len(lista)
	return media
valores=[1, 4, 4, 6, 2, 7, 8]
media = media_lista(valores)
print("media = %.2f" %media)
	


def media_lista(lista):
	media = sum(lista)/len(lista)
	return media
valores=[1, 4, 4, 6, 2, 7, 8]
media = media_lista(valores)
print("media = %.2f" %media)
	

def analise_lista(lista):
	maior = max(lista)
	menor = min(lista)
	media = sum(lista) / len(lista)

	maior, menor, media = analise_lista(valores)
	print("maior = %.2f" %maior)
'''----------------------------------------------------------------------------------'''
	import random

	def gera_inteiro():
		return(random.radiant(a,b))

	print("------------------- O JOGO DE ADIVINHAÇÃO ---------------------")



	for X in range(10):
		print(random.radiant(1,100))


	numero = gera_inteiro(1,10)

	acertou = False

	i = 0
	while i<5:
		chute=int(input("Numero entre 1 e 10: "))
		if chute== numero:
			acertou=true
			break

		i+=1

	if acertou:
		print("Você acertou! O número gerado foi o %d." %numero)
	else:
		print("Que pena... O número gerado foi o %d. Tente novamente." %numero)

	import turtle

	screen = turtle.screen()

	reliquia = turtle.Turtle()

	reliquia.shape('turtle')

	reliquia.color('blue')
	reliquia.pensize(3)
	reliquia.forward(150)
	reliquia.left(90)
	reliquia.forward(75)

	screen.exitonclick()

	import turtle
	def desenha_quadrado(tartaruga,tamanho,cor):
		tartaruga.color(cor)
		for i in range(4):
			tartaruga.forward(tamanho)
			tartaruga.left(90)

			screen =turtle.Screen()
			reliquia = turtle.Turtle()
			reliquia.shape('turtle')
			desenha_quadrado(reliquia, 200, 'red')
			screen.exitonclick()