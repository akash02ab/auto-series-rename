import os, re
from collections import defaultdict


count = defaultdict(list)
def fileFinder():

    # Getting the current work directory (cwd)
    thisdir = os.getcwd()

    # r=root, d=directories, f = files
    for r, d, f in os.walk(thisdir):
        for file in f:
            if file.endswith(".mkv") or file.endswith(".mp4"):
                # print(file)
                s = re.search(r's\d+|S\d+|Season\d+|season\d+', file).group()
                e = re.search(r'e\d+|E\d+|Episode\d+|episode\d+', file).group()
                if s and e:
                    if e not in count[s]:
                        count[s].append(e)