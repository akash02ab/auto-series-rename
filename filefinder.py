import os, re
from collections import defaultdict


def isMatch(file, name):
    #change file name and series name to lower case
    file = file.lower()
    name = name.lower()

    #seperate all words and store it in list
    l1 = re.findall(r"[\w']+", file)
    l2 = re.findall(r"[\w']+", name)

    #return True if series name is present in file name
    return ', '.join(map(str, l2)) in ', '.join(map(str, l1))

'''
dictionary that sore information in format:
count = {'Sno.' : ['Eno']}
'''
count = defaultdict(list)

def fileFinder(name, thisdir):

    '''
    walk through every folders and files in 'thisdir'
    '''
    # r=root, d=directories, f = files
    for r, d, f in os.walk(thisdir):
        for file in f:

            #if file is a video file
            if file.endswith(".mkv") or file.endswith(".mp4"):

                #verify id file belongs to given series
                if isMatch(file, name):
                    #retrieve season number from file name
                    try:
                        s = re.search(r's\d+|S\d+|Season\d+|season\d+', file).group().upper()
                    except:
                        continue
                    #retrieve episode number from file name
                    try:
                        e = re.search(r'e\d+|E\d+|Episode\d+|episode\d+', file).group().upper()
                    except:
                        continue

                    #if both season and episode number are present than store it into dictionary 'count'
                    if s and e:
                        if e not in count[s]:
                            count[s].append(e)
                            