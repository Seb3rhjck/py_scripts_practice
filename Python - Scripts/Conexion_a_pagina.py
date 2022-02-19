from request import get, exceptions

def check_la_conexion_internet():
	try:
		get('https://binance.com/', timeout = 3)
		print('Conectado')
	except exceptions.ConnectionError:
		print('No hay conexion')
		
check_la_conexion_internet()
