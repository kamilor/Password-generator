import random, string

l = "grass brick testy chivalrous incompetent rais steel care productive vagabond playground existence coil mountainous wink saw jellyfish gentle spark wide measly concerned weigh team potato unbecoming example third fax live jolly rejoice macho sound base gate kittens coil bump stomach blot subdued hook tough descriptive proud art pause include"
z = l.split()
things = "!@#$%^&*()_-+:,."
things1 = "123456789"

def what_pass():
	a = input("What password do you like, strong, medium or weak?(s,m,w): ")
	while a != "w" or "m" or "s":
		if a == "w":
			return password_weak()
		elif a == "m":
			return password_medium()
		elif a == "s":
			return password_strong()
		a = input("Something went wrong, choose between (s - strong, m - medium, w - weak): ")
	
def password_weak():
	global z 
	global things1
	return random.choice(z) + random.choice(things1)

def password_medium():
	global z
	global things1
	return random.choice(z) + random.choice(things1) + random.choice(z)

def password_strong(lenght = 30):
	global things1
	letters = string.ascii_lowercase + things1 + string.ascii_uppercase + things
	return ''.join(random.choice(letters) for i in range(lenght))



p = what_pass()
print(p)