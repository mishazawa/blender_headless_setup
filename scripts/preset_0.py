from easybpy import *
import sys

FRAME_START = 1
FRAME_END = 240

# read command line args
argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"

# set output dir
get_scene().render.filepath = './output/'

# set frame range
frame_start(FRAME_START)
frame_end(FRAME_END)

# show specified weapon
weapon = get_object(argv[0])
unhide(weapon)
unhide_in_render(weapon)

