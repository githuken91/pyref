import zlib
import argparse
import os
from pathlib import Path

def gfwe(s: str): return Path(s).stem # get filename without extension

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str)
parser.add_argument("-s", "--section", type=str)
args = parser.parse_args()

# create save path
path = ""
try:
    if args.section:
        path = "{}/{}/{}".format(os.environ["PYREF_MANUAL_DIR"], args.section, gfwe(args.filename)+".cprp")
    else:
        path = "{}/{}".format(os.environ["PYREF_MANUAL_DIR"], gfwe(args.filename)+".cprp")
except:
    print("No environment variable set for PYREF_MANUAL_DIR.")

print("Saving to: " + path)
data = ""
with open(args.filename, "r") as F: # read original content
    data = F.read()

compressed_data = zlib.compress(data.encode("utf-8")) # gzip compression would probably be better? but zlib is easier

if not os.path.isdir(Path(path).parent): # i hate that oses dont just create a directory when you're tryna create a file
    os.mkdir(Path(path).parent)
with open(path, "wb") as F:
    F.write(compressed_data)

print("Done!")
