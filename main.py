import filefinder as f
import searchbot as s
import filemodifier as m
from pathlib import Path

if __name__ == "__main__":

    '''
    The name of TV-Series.
    Please enter it wisely with cases and spaces formatted correctly.
    As, it'll be reflected in the video file.
    '''
    series_name = 'Young Sheldon'

    '''
    The directory where all the video files are present.
    Please make sure to enter closest parent directory.
    eg: Consider the directory construct :-
        Tv-Series
            |
            |
      -----------------------------
      |                           |
      Young Sheldon               The Big Bang Theory
            |                              |
    -------------------------          -----------
    |          |            |          |         |
    Season 1   Season 2    Season 3   ...       ...

    Suppose you want to rename all files of Young Sheldon,
    then select the Young Sheldon directory.
    It will make the program run faster.
    '''
    dir = Path('C:/Users/91883/Downloads/Tv-Series/Young Sheldon')

    '''
    If your files are not present in organised fashion, then
    enter the directory where you want to store all the file.
    Note :- If your file are already organised than leave this field empty,
    otherwise if you choose to organise enter the directory in following manner:-
                    "syspath/series_name/"
    You need not require to make Season directory separately as it will create it
    automatically and move the corresponding file of that season in that newly created folder.
    '''
    changeDir = Path('') 

    #find the files in given directory
    f.fileFinder(series_name, dir)

    #search the details like title, episode description and store it in csv file season wise
    s.searchBot(series_name, dir)

    #finally rename the files in specific format [series name sno. eno. title] and organise it, if not already
    m.modifyFile(series_name, dir, changeDir)   