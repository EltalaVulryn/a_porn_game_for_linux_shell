configeration = {
	'silent_imprengations': False,
}

import subprocess

import os

import random

fert = random.randint(1, 100)

y = 'y'

n = 'n'

option1 = '1'

option2 = '2'

option3 = '3'

bed = 20

cum = 30

while True:
	subprocess.run('clear')
	print("Eltala presents you Erotic Night~")
	print()
	print("Main menu: type your option")
	print()
	print("play?")
	print()
	print("README")
	print()
	print("exit")
	print()
	menu = input()	
	if menu == 'cheats':
		while True:
			subprocess.run('clear')
			print("what kind of cheats do you want on? please type it exactly how it says minus the '?'")
			print()
			print("always get pregnant? $self explantory, sets fert to 100")
			print()
			print("change fertility? higher the number more likely to get pregnant")
			print()
			cheats_menu = input("select cheats then type back to go back: ")
			if cheats_menu == 'always get pregnant':
				fert = 100
			if cheats_menu == 'change fertility':
				fert_modifer = input('what would be the fertility? 0-100: ')
			fert_modifer = fert
			if cheats_menu == 'back':
				break
	if menu == 'README':
		subprocess.run('clear')
		subprocess.run(['cat', '/Games/eroticnight~/README.md'])
		input("press enter to exit read me")
	if menu == 'exit':
		subprocess.run('clear')
		quit()
	if menu == 'play':
		while True:
			print("which chapter?")
			print()
			print("chapter 1")
			print()
			print("chapter 2 (not avalible right now)")
			print()
			print("chapter 3 (not avalible right now)")
			print()
			print("type back to go back")
			print()
			chapter = input("which option? ")
			menu = chapter
			if chapter == '1':
				break
			else:
				input("sorry that aint an opion... press enter to go back")
				subprocess.run('clear')
		if menu == '1':
			break
		
pregnant = False

subprocess.run('clear')

player = input('name here: ')

women = input('name the female actrist: ')

if chapter == '1':
	print("Backstory: you had met a girl in a strip club named " + women + ", and you and her talked a bit, and you sat down at a table by your self, then she walks upto you after 2 minutes")

	print(women + ": hello there " + player + "~ would you like to have some fun with me~?")
	print(player + ": y : are you suggesting something~?")
	print(player + ": n : no... go fuck someone else...")
	action = input("which option?: ")
	if  n == action: 
		print(women + ": aww... worth the shot...")
	else:
		action = input(women + ": would you like to follow me to my room~?	y/n:")
		if n == action:
			print(women + ": i understand you changed your mind...")
		else:
			print(women + ": *she giggles, and leads you to her room*")
			print(player + ": *you walk into her room*")
			print(women + ": closes the door,* would you like to help me remove my clothes~?")
			print(player + ": Y :sure~")
			print(player + ": n : no")
			action = input("which option?: ")
		
			if n == action:
				print(women + ": oh... so your one that will make us do all the work aren't you~?")
				print(player + ": y : heh~ you bet i am dear~")
				print("Or (just different words, no affect on gameplay)")
				print(player + ": n : what~? i only see this once~")
				action = input("which option?: ")
				if action == action:
					print(women + ": dirty bastured~")
					print(women + ": what do you want~? a lap dance~? is that why you had me remove them my self~?")
					print(player + ": y : i would like one~")
					print("Or")
					print(player + ": n : nah~ just making you do the work for me~ *you walk upto her, pulling her into a kiss*")
					action = input("which option?: ")
					if n == action:
						print(women + ": *her eyes widen in surprise, closing her eyes*")
						print(women + ": *you then begin to get erect*")
						print(player + ": 1 : *begin to lift one of her legs, putting your tip on her entrance*")
						print(player + ": 2 :*gently pushes her onto the bed*")
						print(player + ": 3 :*you gently guide her against the wall, with a smirk*")
						print("WARNING MAKE SURE YOU SELECT THE RIGHT ONE OR IF YOU DONT DO ONE OF THE OPTIONS BUT ANOTHER KEY IT WILL EXIT THE GAME!!!")
						action = input("which option?: ")
						if option1 == action:
							print(women + ": *her entrance was wet, and she lets out a soft moan, then pulls away* what are you gonna do~?")
							print(player + ": y : some teasing~ *you gently start probing her*")
							print("Or")
							print(player + ": n : *with out a word, you hold her other leg, and in response she wraps her arms around you, and you push her your penis deep into her*")
							action = input("which option?: ")
							if n == action:
								print(women + ": AHN~! *you grunt a little due to how tight she is*")
								subprocess.run(['bash', '/Games/eroticnight~/assets/repeatrbut.sh'])
								print("oh " + player + "!")
								action = input("do you want to cum in her? y/n")
								if action == n:
									print("*you pull out and cum onto her vagiia*")
								else:
									if fert >= 80:
										if configeration["silent_imprengations"] == False:
											subprocess.run(['bash', '/Games/eroticnight~/animations/rbutterp.sh'])
											print("you just imprenganted " + women + "!")
										else:
											subprocess.run(['bash', '/Games/eroticnight~/animations/rbuttercump.sh'])
										fert = 0
										pregnant = True	
									else:
										fert = random.randint(1, 100)
										subprocess.run(['bash', '/Games/eroticnight~/animations/rbuttercump.sh'])
								print(player + ": *after railing her a couple times in this postion, you put her into the bed*")
								bed = 78
						if option2 == action:
							
							bed = 78
						if option3 == action:
							print(women + ": oh my~ i never done it like this before~")
					else:
						print(women + ": you have to sit down first dear~")
						print(player + ": *you do so, on a chair*")
						print(women + ": *she walks upto you, and begins to do a lap dance*")
						print("what do you do?//")
						print(player + ": y : *reach up. and put your hand on her ass. starting to get hard*")
						print("Or, (different actions, no affect on what happens, but will affect what she says//)")
						print(player + ": n : *you just watch her, startiong to get hard*")
						action = input("which option?: ")
						if n == action:
							print(women + " turn on easily i see~ *giggles*")
						else:
							print(women + "oh~ hehe~ turn on easily i see~ *giggles*")
			else:
				print(women + ": *she starts to remove her panties, and she walks upto you, and begins to do a lap dance*")
				print(player + ": y : *once she takes off her panties you push her down gently onto her bed*")
				print("Or")
				print(player + ": n : *once she takes off her panties, you lick her neck lewdly*")
				action = input("which option?: ")
				if n == action:
					print(women + ": how lewd of you~")
					print(women + ": come on and fuck me already~")
					print("do you pin her to the wall? y")
					print("or")
					print("do you start to rub your penis on her vagina? n")
					action = input("which option?")
				else:
					bed = 78
		if bed == 78:
			print(women + ": *soft thud when she lands on the bed* rawr~ *spreads her legs out*")
			print("what do you do?")
			print(player + ": y : *walk upto her, and lifts her legs, putting her tip in*")
			print("Or")
			print(player + ": n : *you hover over her, leaning over, mounting her, then you put your tip into her")
			action = input("which option?: ")
			if n == action:
				print(women + ": *she gazes into your eye's, waiting for you take her, break her*")
				print("what do you do?")
				print(player + ": y : *you lean down and kiss her, making it deep and pasionet, closing your eyes*")
				print("or")
				print(player + ": n : *you start gently thrusting into her, grunting softly at how tight she is*")
				action = input("which option?:")
				if n == action:
					print("fuck me hard " + player + "~")
			else:
				print(women + ": *she huffs softly, and she looks down at the action*")
				print("what do you do?")
				print(player + ": y : *start to slowly speed up on her*")
				print("or (does not affect outcome at all)")
				print(player + ": n : you lean down a little, and start ramping up the speed, and push her legs down a little")
				action = input("which option?:")
				if action == action:
					print(women + ": *she starts to moan* oh " + player + " you feel so good~")
					print(player + ": y : *cum in " + women + "?*")
					print("or")
					print(player +": n : *keep going?*")
					action5BBA = input("which option?:")
					if action5BBA == n:
						print(player + "*: you keep going deep inside of her, as she moans*")
						print(women + ": oh " + player + " dont stop~ your doing so good~")
						action = input("cum in " + women + "? y/n")
						if action == n:
							print(player + ": *you procude to go harder on her*")
							print("what do you do?")
							print("y: cum in " + women)
							print("or")
							print("n: mute her moans by kissing her?")
							action = input("which option?")
							if action == n:
								print(women + ": *she embraces it, as you rail her, moaning underneath the kiss*")
								print(women + ": *pulls away* cum in me~")
								action = input("will you? y/n")
								if action == n:
									print(women + ": no~? fine~ have you fun sweatheart~")
									input("press enter to cum in " + women)
									cum = 40
								else:
									cum = 40
						else:
							cum = 40
					else:
						cum = 40
					if cum == 40:
						if fert >= 80:
							if configeration["silent_imprengations"] == False:
								subprocess.run(['bash', '/Games/eroticnight~/animations/cump.sh'])
								print("you just impregnanted " + women + "!")
							pregnant = True
							if configeration["silent_imprengations"] == True:
								subprocess.run(['bash', '/Games/eroticnight~/animations/cum.sh'])
						else:
							subprocess.run(['bash', '/Games/eroticnight~/animations/cum.sh'])
					print("mhp~!")
					print(women + ": *looks blistful* you might have a kid...")
					subprocess.run(['sleep', '2'])
	if pregnant == True:
		subprocess.run(['sleep', '5'])
		subprocess.run('clear')
		print("9 months later")
		print("*you would be in your home, on the couch, and you get a call from " + women + "*")
		print("*you pick it up and awnser it")
		print(player + ": hello?")
		print(women + ": Hey, it's me " + women + ". Remember some months back? Well you did end up getting me pregnant and I've had the baby just thought I'd let you know.")
	print("WARNING!!! INCOMPLETE!")
