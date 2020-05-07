import filefinder as f
import searchbot as s
import filemodifier as m

if __name__ == "__main__":
    series_name = 'The Big Bang Theory' 
    f.fileFinder()
    s.searchBot(series_name)
    m.modifyFile(series_name)   