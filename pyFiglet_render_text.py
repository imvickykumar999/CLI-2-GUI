
# pip install pyfiglet

from pyfiglet import Figlet
f = Figlet(font='slant')

inp = input('Enter text to render : ')
print (f.renderText(inp))
