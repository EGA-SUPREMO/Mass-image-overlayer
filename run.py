import os
import sys
import subprocess

os.system("magick -background none inn1.jpeg int.png -layers flatten out.png")
