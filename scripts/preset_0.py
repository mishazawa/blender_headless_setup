from easybpy import *
import sys

# read command line args
argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"

# set frame range
frame_start(int(argv[0]))
frame_end(int(argv[1]))

# get pivot object for camera rotation
pivot = get_object("Pivot")

# insert initial keyframe
start_frame = add_keyframe(pivot, "rotation_euler", frame_start())

# do rotation
rotate_around_z(int(argv[2]), pivot)

# insert last keyframe
end_frame = add_keyframe(pivot, "rotation_euler", frame_end())
