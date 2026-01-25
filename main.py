def hello_world(name: str) -> str:
	"""
	Docstring for hello_world
	
	:param name: Description
	:type name: str
	:return: Description
	:rtype: str
	"""
	print(f'Hello World! Mr./Mrs {name}')


if __name__ == '__main__':
	name = input('What is your name? ')
	hello_world(name)
