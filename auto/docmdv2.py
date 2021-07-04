import click
import random
@click.command()
@click.option('--monty', default=False, help='Show a Monty Python quote.')
@click.option('--veg', default=False, help='Show a random vegetable.')
def do_work(monty, veg):
	""" Basic Click example will follow your commands"""
	if monty:
		print('What\'s this, then? "Romanes eunt domus"? People called Romanes, they go, the house?')
	if veg:
		print(random.choice(['Carrot', 'Potato', 'Turnip']))
if __name__ == '__main__':
	do_work()