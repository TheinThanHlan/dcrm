import os
import sys


def openFile(name):
	print(os.popen("alacritty --title "+name+ " -e nvim "+name));


name=sys.argv[1]
openFile(name)
