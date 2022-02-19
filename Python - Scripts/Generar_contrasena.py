import random, string

def generar_contrasena(n):
	
	todosCaract = list(string.ascii_letters) + 
	list(string.digits) +
	list(string.punctuation)
	contraFrase = []
	
	for i in range(n):
		tmp = random.choice(todosCaract)
		contraFrase.append(tmp)
	
	res = "".join(contraFrase)
	return res

n = input("Ingresa el ancho de la contraseña minimo 4 maximo 12: ")
test = generar_contrasena(n)

if n < 4 or n > 12:
	print("Ingresa de nuevo el ancho de la contraseña minimo 4 maximo 12: ")
else:
	print(test)
		
		
