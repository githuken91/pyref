import os
import sys
import argparse
from pypager.pager import Pager
from pypager.source import StringSource
import traceback
import zlib

# Get page & section
parser = argparse.ArgumentParser()

parser.add_argument("-s", "--section", type=str)
parser.add_argument("page", type=str)
args = parser.parse_args()
path = ""

# Create path
try:
    path = os.environ["PYREF_MANUAL_DIR"] + "/" # I should probably have a default instead of a "yeet everything" if there is no MANUAL_DIR env variable.
except KeyError:
    print("Could not find manuals directory. Please verify the installation of pyref.")
    sys.exit(1)

if args.section:
    path += args.section + "/"

path += args.page + ".cprp" # cprp - compressed pyref reference page

o_page_content = bytes() # why do i initialize these like this???
page_content = ""

try:
    F = open(path, "rb") # who even does it like this anymore?? why did i feel the need to do it like this? im too lazy to fix it though xd
    o_page_content = F.read()
    F.close()
except Exception as e:
    print("An error occured while trying to find / read the reference page. Please double check your command.")
    print("Error Details:")
    print(repr(e))
    sys.exit(1)

try:
    page_content = zlib.decompress(o_page_content).decode() # decode the compressed page from ZLIB compression.
except Exception as e:
    print("An error occured decompressing the reference page. Please report this to the pyref dev or the developer of the reference page.")

if __name__ == '__main__':
    try:
        p = Pager() # some oses dont have less/more
        p.add_source(StringSource(page_content))
        p.run()
    except Exception as e:
        traceback.print_exc()
        print("An error occured loading the reference page into the pager. This is likely a bug. Please report it on the Github issues tracker.")
