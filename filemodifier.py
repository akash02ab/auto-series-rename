import os, csv, re

def modifyFile(name):
    # Getting the current work directory (cwd)
    thisdir = os.getcwd()
    D = {}
    # r=root, dir=directories, f = files
    for r, dir, f in os.walk(thisdir):
        for file in f:
            d = {}
            if file.endswith(".csv"):
                with open(file, "r") as csv_file:
                    csv_reader = csv.DictReader(csv_file, delimiter=',')
                    for column in csv_reader:
                        s = column['season']
                        e = column['episode']
                        t = column['title']
                        d[e] = t
                D[s] = d
                csv_file.close()

    for r, dir, f in os.walk(thisdir):
        for file in f:
            if file.endswith(".mkv") or file.endswith(".mp4"):
                s = re.search(r's\d+|S\d+|Season\d+|season\d+', file).group()
                e = re.search(r'e\d+|E\d+|Episode\d+|episode\d+', file).group()
                if s and e:
                    title = D[s][e]
                    newFile = f'{name} {s.upper()}{e.upper()} {title}.mkv'
                    os.rename(os.path.join(r, file), os.path.join(r, newFile))