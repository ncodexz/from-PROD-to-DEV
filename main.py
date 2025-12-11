def hello_world(name: str) -> str:
	print(f'Hello World! Mr./Mrs {name}')


if __name__ == '__main__':
	name = input('What is your name? ')
	hello_world(name)
