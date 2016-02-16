import argparse # Makes it easy to write user-friendly command-line interfaces.
import subprocess # Allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.
import sys
import time

ap = argparse.ArgumentParser() # Define an Argument Parser
ap.add_argument("-v", "--video", help="path to the video file") # Add --video argument
ap.add_argument("-a", "--audio", help="path to the audio file") # Add --audio argument
args = vars(ap.parse_args()) # Parse the arguments

hearing_process = subprocess.Popen(["python", "hearing/perception.py", args["audio"]]) # Start hearing perception subprocess
vision_process = subprocess.Popen(["python", "vision/perception.py", "--video", args["video"]]) # Start vision perception subprocess