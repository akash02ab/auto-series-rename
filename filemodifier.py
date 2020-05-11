import os, csv, re, shutil
from filefinder import isMatch

def modifyFile(name, thisdir, moveDir):
    '''
    The dictionary "D" contains the data in format:
    D = {'S01' : ['E01' : 'title1', 'E02' : 'title2', ....], 'S02' : [....], ....}
    This data is extracted from csv files that was created earlier
    '''
    D = {}
    # r=root, dir=directories, f = files
    for r, dir, f in os.walk(thisdir):
        for file in f:
            d = {}
            if file.endswith(".csv"):
                with open(f'{thisdir}/{file}', "r") as csv_file:
                    csv_reader = csv.DictReader(csv_file, delimiter=',')
                    for column in csv_reader:
                        s = column['season']
                        e = column['episode']
                        t = column['title']
                        d[e] = t
                D[s] = d
                csv_file.close()
    
    '''
    Again, look for all videos files and extract season number "s" and episode number "e".
    Use this index to access "title" from dictionary "D" as D[s][e] 
    '''
    for r, dir, f in os.walk(thisdir):
        for file in f:
            if file.endswith(".mkv") or file.endswith(".mp4"):
                if isMatch(file, name):
                    try:
                        s = re.search(r's\d+|S\d+|Season\d+|season\d+', file).group().upper()
                    except:
                        pass
                    try:
                        e = re.search(r'e\d+|E\d+|Episode\d+|episode\d+', file).group().upper()
                    except:
                        pass
                    if s and e:
                        #check if index already exists in the dictionary "D"
                        if s in D.keys() and e in D[s].keys():
                            title = D[s][e]
                            newFile = f'{name} {s}{e} {title}.mkv'
                            #rename the file
                            os.rename(os.path.join(r, file), os.path.join(r, newFile))
                        
                        #create new folder "Season [n]" and move episodes of that season
                        if moveDir:
                            n = re.findall(r'\d+', s)
                            folderName = 'Season ' + n[0]
                            newDir = moveDir + '/' + folderName
                            #if "folderName does not exists already, create it"
                            if not os.path.exists(newDir):
                                os.mkdir(newDir)
                            shutil.move(os.path.join(r, file), os.path.join(newDir, file))