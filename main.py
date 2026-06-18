import os
import sys
import argparse
from pypager.pager import Pager
from pypager.source import StringSource
import traceback
import zlib

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--section", type=str)
parser.add_argument("page", type=str)
args = parser.parse_args()
path = ""

try:
    path = os.environ["PYREF_MANUAL_DIR"] + "/"
except KeyError:
    print("Could not find manuals directory. Please verify the installation of pyref.")
    sys.exit(1)

if args.section:
    path += args.section + "/"

path += args.page + ".cprp"

o_page_content = bytes()
page_content = ""

try:
    F = open(path, "rb")
    o_page_content = F.read()
    F.close()
except Exception as e:
    print("An error occured while trying to find / read the reference page. Please double check your command.")
    print("Error Details:")
    print(repr(e))
    sys.exit(1)

try:
    page_content = zlib.decompress(o_page_content).decode()
except Exception as e:
    print("An error occured decompressing the reference page. Please report this to the pyref dev or the developer of the reference page.")

if __name__ == '__main__':
    try:
        p = Pager()
        p.add_source(StringSource(page_content))
        p.run()
    except Exception as e:
        traceback.print_exc()
        print("An error occured loading the reference page into the pager. This is likely a bug. Please report it on the Github issues tracker.")
