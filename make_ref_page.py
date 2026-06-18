import zlib
import argparse
import os
from pathlib import Path

def gfwe(s: str): return Path(s).stem

parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str)
parser.add_argument("-s", "--section", type=str)
args = parser.parse_args()

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
with open(args.filename, "r") as F:
    data = F.read()

compressed_data = zlib.compress(data.encode("utf-8"))

if not os.path.isdir(Path(path).parent):
    os.mkdir(Path(path).parent)
with open(path, "wb") as F:
    F.write(compressed_data)

print("Done!")
