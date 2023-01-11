import sys
from turtle import *
import random
import json
import os
from playsound import playsound
playsound('C:\\Users\\DELL\\Desktop\\visilica\\start.mp3',False) # не работает только через ыгидшьу

from myDB import *

hideturtle()

slovechki = ['Кант', 'Хроника', 'Зал', 'Галера', 'Балл', 'Вес', 'Кафель', 'Знак', 'Фильтр', 'Башня', 'Кондитер', 'Омар', 'Чан', 'Пламя', 'Банк', 'Тетерев', 'Муж', 'Камбала', 'Груз', 'Кино', 'Лаваш', 'Калач', 'Геолог', 'Бальзам', 'Бревно', 'Жердь', 'Борец', 'Самовар', 'Карабин', 'Подлокотник', 'Барак', 'Мотор', 'Шарж', 'Сустав', 'Амфитеатр', 'Скворечник', 'Подлодка', 'Затычка', 'Ресница', 'Спичка', 'Кабан', 'Муфта', 'Синоптик', 'Характер', 'Мафиози', 'Фундамент', 'Бумажник', 'Библиофил', 'Дрожжи', 'Казино', 'Конечность', 'Пробор', 'Дуст', 'Комбинация', 'Мешковина', 'Процессор', 'Крышка', 'Сфинкс', 'Пассатижи', 'Фунт', 'Кружево', 'Агитатор', 'Формуляр', 'Прокол', 'Абзац', 'Караван', 'Леденец', 'Кашпо', 'Баркас', 'Кардан', 'Вращение', 'Заливное', 'Метрдотель', 'Клавиатура', 'Радиатор', 'Сегмент', 'Обещание', 'Магнитофон', 'Кордебалет', 'Заварушка']

def line(pos1: tuple, pos2: tuple):
	speed(0)
	penup()
	goto(pos1[0], pos1[1])
	speed(3)
	pendown()
	goto(pos2[0], pos2[1])
	penup()
	speed(0)

def draw_error(numError):
	global isDrawing
	isDrawing = True
	match numError:
		case 1:
			line((-370, -250), (-25, -250))
		case 2:
			line((-50, -250), (-50, 300))
		case 3:
			line((-50, 300), (-300, 300))
		case 4:
			line((-300, 300), (-300, 250))
		case 5:
			penup()
			speed(0)
			goto(-300,250)	
			speed(3)	
			pendown()		
			pensize(7)
			circle(-40)
			speed(0)
		case 6:
			line((-300, 170), (-300, -0))
		case 7:
			line((-300, 100), (-200, 160))
		case 8:
			line((-300, 100), (-390, 160))
		case 9:
			line((-300, -0), (-200, -100))
		case 10:
			line((-300, -0), (-400, -100))
	isDrawing = False

def kvadrat(L,h:list):
	penup()
	goto(h[0],h[1])
	pendown()
	for x in range(4):		
		forward(L)
		right(90)
	penup()

def slovo(k:list, slova):
	goto(k[0],k[1])
	a = len(slova)
	X = -350
	Y = -300
	for x in range(a):		
		kvadrat(50,[X, Y])
		X = X + 75

def drawLetter(bukva,adresa):
	for x in adresa:
		penup()
		goto(-325+75*x,-350)
		write(bukva, move=False, align="center", font=("Arial", 30, "normal"))

def alfabet_menu():
	laterX = 100
	laterY = 200
	alfabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
	slovar = {}
	for x in alfabet:
		slovar[x] = (laterX,laterY)
		if laterX == 300:
			laterX = 100
			laterY -= 50
		else:
			laterX += 50
	return slovar

def print_alfabet(alfabet):	
	for x in alfabet:
		penup()
		goto(alfabet[x][0],alfabet[x][1])
		write(x, move=False, align="center", font=("Arial", 30, "normal"))

def click():		
	x = random.randint(0,1)
	if x == 0:
		playsound('C:\\Users\\DELL\\Desktop\\visilica\\click.mp3', False)
	else:
		playsound('C:\\Users\\DELL\\Desktop\\visilica\\click2.mp3', False)
def getletter(x,y):
	global listUsedLet
	global lettersDict
	# print(x,y)

	if isGame:
		if not isDrawing:
			for letter in lettersDict:
				if (lettersDict[letter][0]-25 < x < lettersDict[letter][0]+25  and lettersDict[letter][1] < y < lettersDict[letter][1]+50) and (letter not in listUsedLet):
					# print(letter)	
					penup()
					goto(lettersDict[letter][0],lettersDict[letter][1]+25)
					pendown()
					click() # не работает только через ыгидшьу
					dot(50,"white")
					chek_latter(letter)
	else:
		if (-150 < x <-50 and -300 < y < -200):
			start_game()
		elif (50 < x < 150 and -300 < y < -200):
			sys.exit()

def chek_latter(bukva):
	global schetWin
	global schetLose
	global listUsedLet
	global sicret_word
	listAdrLet = []
	if bukva in sicret_word and bukva not in listUsedLet:
		schetWin += 1
		playsound('C:\\Users\\DELL\\Desktop\\visilica\\verno.mp3', False) # не работает только через ыгидшьу
		# print("Угадал букву")
		listUsedLet.append(bukva)
		for x in range(len(sicret_word)):
			if sicret_word[x] == bukva:
				listAdrLet.append(x)
		# print(listAdrLet)
		drawLetter(bukva,listAdrLet)
	elif bukva not in listUsedLet and bukva not in sicret_word:
		schetLose += 1
		playsound('C:\\Users\\DELL\\Desktop\\visilica\\neverno.mp3', False) # не работает только через ыгидшьу
		listUsedLet.append(bukva)
		# print("Не угадал")
		draw_error(schetLose)
	chek_game(schetWin,schetLose,sicret_word)

def chek_game(win,lose,word):
	if lose == 10:
		menu("ВЫ ПРОИГРАЛИ")
		playsound('C:\\Users\\DELL\\Desktop\\visilica\\lo.mp3', False)
	elif win == len(set(word)):
		menu("ВЫ ВЫИГРАЛИ")
		playsound('C:\\Users\\DELL\\Desktop\\visilica\\wo1.mp3', False)

def menu(status,):
	global isGame
	global sicret_word
	isGame = False
	# print("Вы проиграли")
	clear()
	goto(0,300)
	write(status, move=False, align="center", font=("Arial", 50, "normal"))
	goto(0,100)
	write(sicret_word, move=False, align="center", font=("Arial", 30, "normal")) 
	goto(0,-200)
	write("Желаете продолжить?", move=False, align="center", font=("Arial", 50, "normal"))
	goto(-100,-300)
	pencolor("Green")
	write("Да", move=False, align="center", font=("Arial", 50, "normal"))
	goto(100,-300)
	pencolor("Red")
	write("Нет", move=False, align="center", font=("Arial", 50, "normal"))
	pencolor("Black")
	playerInfo['Total Scores'] += 100 -(schetLose * 10)
	mydb.dumpdb()

def start_game():
	global lettersDict
	global sicret_word
	global schetWin
	global schetLose
	global listUsedLet
	global isGame
	global isDrawing
	schetWin = 0
	schetLose = 0
	listUsedLet =[]
	isGame = True
	isDrawing = False	



	clear()

	pensize(5)
	speed(0)
	penup()
	goto(-450,400)
	playerInfo['Games'] += 1
	write(f"Игрок: {player}\tВсего игр: {playerInfo['Games']}\tВсего очков: {playerInfo['Total Scores']}", move=False, align="left", font=("Arial", 20, "normal"))

	lettersDict = alfabet_menu()
	print_alfabet(lettersDict)

	# print(sicret_word)
	sicret_word = random.choice(slovechki).lower()
	slovo([-350, -300],sicret_word)


def table():
	goto(0,0)
	dot(25)
	massiv = mydb.top10()
	y = 260
	clear()
	penup()
	goto(-275,375)
	write("Таблица рекордов:", move=False, align="left", font=("Arial", 40, "normal"))
	goto(-300,300)
	write("Имя", move=False, align="left", font=("Arial", 30, "normal"))
	goto(-125,300)
	write("Очки", move=False, align="left", font=("Arial", 30, "normal"))
	goto(60,300)
	write("Кол-во игр", move=False, align="left", font=("Arial", 30, "normal"))
	for x in range(len(massiv)):
		pensize(5)
		speed(0)
		penup()
		
		goto(-300,y)
		write(f"{massiv[x][0]:<5}\t{massiv[x][2]:>15}\t{massiv[x][1]:>15}", move=False, align="left", font=("Arial", 20, "normal"))
		y -= 50
		


mydb = FoobarDB("./mydb.db")

mydb.load("./mydb.db")
mydb.top10()
table()
while True:
	player = textinput("ИГРОК", "Введите Ваше имя:")
	if mydb.get(player):
		playerInfo = mydb.get(player)
		break
	else:
		newPlayer = textinput("Данного игрока не существует", "Создать нового?(да/нет)")
		if newPlayer == "да":
			mydb.set(player , {"Games": 1, "Total Scores": 0})
			playerInfo = mydb.get(player)
			break

start_game()
onscreenclick(getletter)
mainloop()