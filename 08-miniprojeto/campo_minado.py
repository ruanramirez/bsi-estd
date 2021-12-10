import os;
import pygame;
import time;
from pygame import display;
from pygame.locals import *;
from pygame.font import *;
from random import randint;
from time import sleep, time as t;

os.environ['SDL_VIDEO_CENTERED']='1'
pygame.init()

bombas = 0
acertos = 0
tamanho = 10
fim = False

campo = [["" for j in range(tamanho)] for i in range(tamanho)]
af = [[0 for j in range(tamanho)] for i in range(tamanho)]
mband = [[0 for j in range(tamanho)] for i in range(tamanho)]

pygame.mixer.music.load('08-miniprojeto/Sound.mp3')
b_som = pygame.mixer.Sound("08-miniprojeto/Bomb.mp3")
relogio = pygame.time.Clock()
pygame.mixer.music.play()

wnd = pygame.display.set_mode( (640, 610), 0, 32)
pygame.display.set_caption('Campo minado')
pygame.mouse.set_cursor(*pygame.cursors.tri_left)

cabec = pygame.Surface((640, 80), 0, 32)
screen = pygame.Surface((640, 480), 0, 32)
pts = pygame.Surface((640, 50), 0, 32)

comp = int(screen.get_width() / tamanho)
alt = int(screen.get_height() / tamanho)

my_font = pygame.font.SysFont("Segoe UI", 20, True, False)
menu_font = pygame.font.SysFont("Segoe UI", 20, True, False)
msg_font = pygame.font.SysFont("Segoe UI", 16, True, False)

q = pygame.transform.scale(pygame.image.load('08-miniprojeto/clean.png').convert_alpha(), (comp, alt))
q2 = pygame.transform.scale(pygame.image.load('08-miniprojeto/clean2.png').convert_alpha(), (comp, alt))
band = pygame.transform.scale(pygame.image.load('08-miniprojeto/band.png').convert_alpha(), (comp, alt))
bomba = pygame.transform.scale(pygame.image.load('08-miniprojeto/img_bomb.png').convert_alpha(), (comp, alt))
logo = pygame.image.load('08-miniprojeto/logo.png').convert_alpha()

pygame.display.set_icon(bomba)

def inicio():
	global bombas, acertos, fim, jogou, campo, af, mband, relogio, tamanho

	bombas = 0
	acertos = 0
	fim = False
	jogou = False

	campo = [["" for j in range(tamanho)] for i in range(tamanho)]
	af = [[0 for j in range(tamanho)] for i in range(tamanho)]
	mband = [[0 for j in range(tamanho)] for i in range(tamanho)]

	pts.fill((0, 0, 0))
	pts.blit(menu_font.render('[m] Música - [r] Reiniciar - [x] Sair', True, (255, 255, 255)), (150, 20))

	for x in range(tamanho):
		for y in range(tamanho):
			screen.blit(q, (x * comp, y * alt))
		pygame.display.update()

def criar(x1, y1):
	global bombas

	for b in range(0, int((tamanho * tamanho) / 5)):
		a1 = randint(0, tamanho - 1)
		a2 = randint(0, tamanho - 1)
		if ((a1 != y1 or a2 != x1) and campo[a1][a2] != "*"):
			campo[a1][a2] = "*"
			bombas += 1
		else:
			b -= 1
	num = 0

	for y in range(tamanho):
		for x in range(tamanho):
			if (campo[y][x] == ""):
				for a in range((y - 1), (y + 2)):
					for b in range((x - 1), (x + 2)):
						if ((a >= 0 and b >= 0) and (a < tamanho and b < tamanho)):
							if (campo[a][b] == "*"):
								num += 1
				campo[y][x] = str(num)
				num = 0
	return True

def colorir(v):
	if( v == '1'):
		imgpeca = my_font.render(v, True, (176, 196, 222))
	elif (v == '2'):
		imgpeca = my_font.render(v, True, (50, 205, 50))
	elif (v == '3'):
		imgpeca = my_font.render(v, True, (178, 34, 34))
	else:
		imgpeca = my_font.render(v, True, (0, 0, 140))
	return imgpeca

def abrir(x, y):
	for l in range((y - 1), (y + 2)):
		for c in range((x - 1), (x + 2)):
			if ((l >= 0 and c >= 0) and (l < tamanho and c < tamanho)):
				if (mband[l][c] == 0):
					screen.blit(q2, (c * comp, l * alt))
					if(campo[l][c] != "0"):
						screen.blit(colorir(campo[l][c]), ((c * comp + (comp / 4)), l * alt))
					elif (campo[l][c] =="0" and (af[l][c] == 0 and (l != y or c != x))):
						abrir(c, l)
					af[l][c] = 1

def explodir(x, y):
	screen.blit(bomba, ((int(x)*comp), (int(y) * alt)))
	b_som.play()
	wnd.blit(screen, (0, 0))
	b = 1
	m = 0
	n = 1

	global bombas, fim, relogio

	while (b < bombas):
		for l in range(y + n - 1, y - n - 1, -1):
			if ((l >= 0 and (x - n) >= 0) and (l < tamanho and (x - n) < tamanho)):
				if (campo[l][x - n] == "*"):
					af[l][x - n] = 1
					time.sleep(0.3)
					screen.blit(bomba, ((x -n) * comp, l * alt))
					b_som.play()
					wnd.blit(screen, (0, 0))
					pygame.display.update()
					b += 1
		for l in range(y - n, y - n - 1, -1):
			for c in range(x - 1 - m, x + 2 + m):
				if((l >= 0 and c >= 0) and (l < tamanho and c < tamanho)):
					if (campo[l][c] == "*"):
						af[l][c] = 1
						time.sleep(0.3)
						screen.blit(bomba, (c * comp, l * alt))
						b_som.play()
						wnd.blit(screen, (0, 0))
						pygame.display.update()
						b += 1
		for l in range(y - n + 1, y + n, 1):
			if (( l >= 0 and (x + n) >= 0) and (l < tamanho and (x+n) < tamanho)):
				if (campo[l][x + n] == "*"):
					af[l][x + n] == 1
					time.sleep(0.3)
					screen.blit(bomba, ((x + n) * comp, l * alt))
					b_som.play()
					wnd.blit(screen, (0, 0))
					pygame.display.update()
					b += 1
		for l in range(y + n, y + n + 1, 1):
			for c in range(x + 1 + m, x - 2 - m, -1):
				if ((l >= 0 and c >= 0) and (l < tamanho and c < tamanho)):
					if (campo[l][c] == "*"):
						af[l][c] == 1
						time.sleep(0.3)
						screen.blit(bomba, (c * comp, l * alt))
						b_som.play()
						wnd.blit(screen, (0, 0))
						pygame.display.update()
						b += 1
		m += 1
		n += 1
	fim = True
	pts.blit(msg_font.render('Que pena, você perdeu! Tempo: ' + str(relogio.tick() / 1000) + 'seg', True, (230, 230, 0)), (150, 0))

def jogar(x, y):
	af[y][x] = 1
	screen.blit(q2, (x * comp, y * alt))
	if (campo[y][x] != "*"):
		if(campo[y][x] == "0"):
			abrir(x, y)
		else:
			screen.blit(colorir(campo[y][x]), ((x * comp + (comp / 4)), y * alt))
	else:
		explodir(x, y)

def bandeirar(x, y):
	acertos = 0
	bombas = 0
	fim = False

	if(mband[y][x] == 0 and af[y][x] == 0):
		if(campo[y][x] == "*"):
			acertos += 1
		mband[y][x] = 1
		screen.blit(band, ((int(x) * comp + (comp / 8)), (int(y) * alt + (alt / 8))))
	elif (af[y][x] == 0):
		if(campo[y][x] == "*"):
			acertos -= 1
		screen.blit(q, ((int(x)) * comp, (int(y)) * alt))
		mband[y][x] = 0

	if(acertos == bombas and bombas > 0):
		fim = True
		pts.blit(msg_font.render("Parabéns você ganhou! Tempo: " + str(relogio.tick() / 1000 + " seg", True, (230, 230, 0), (180, 20))))

pygame.display.update()
jogou = False
inicio()

while True:
	for e in pygame.event.get():
		if e.type == QUIT:
			exit()

		if((e.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed() == (1, 0, 0)) and fim == False):
			(x, y) = e.pos
			if((int(y) / alt) < tamanho):
				if not jogou:
					jogou = criar((int(x) / comp), (int(y) / alt))
					jogar(int(x / comp), int(y / alt))
					relogio.tick()
				elif (mband[int(y / alt)][int(x / comp)] == 0):
					jogar(int(x / comp), int(y / alt))
		if (((e.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed() == (0, 0, 1)) and fim == False) and jogou == True):
			if (int(y / alt) < tamanho):
				(x, y) = e.pos
				bandeirar(int(x/comp), int(y/alt))

		wnd.blit(cabec, (0, 480))
		wnd.blit(screen, (0, 0))
		wnd.blit(pts, (0, 560))
		cabec.blit(logo, (0, 0))

		pygame.display.update()

		if(e.type == KEYDOWN and e.key==K_r):
			inicio()
		if(e.type == KEYDOWN and e.key==K_x):
			exit()
		if(e.type == KEYDOWN and e.key==K_m):
			if pygame.mixer.music.get_busy():
				pygame.mixer.music.stop()
			else:
				pygame.mixer.music.play()
	pygame.display.update()
