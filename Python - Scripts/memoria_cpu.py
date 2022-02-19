import psutil

if __namme__ == '__main__':
	perc_cpu = psutil.cpu_percent(interval = 1, percpu = True)
	mem_virt = int(psutil.virtual_memory().used/(1024 ** 2))
	avail_mem = int(psutil.virtual_memory().available * 100/psutil.virtual_memory().total)
	print(f''' El estado actual del PC es:
	La CPU esta al {perc_cpu}%
	Usando {mem_virt} MB de memoria
	Memoria libre de {avail_mem}% ''')
