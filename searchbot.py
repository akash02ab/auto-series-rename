from bs4 import BeautifulSoup
import urllib, requests, webbrowser, csv, re
from collections import defaultdict
from filefinder import count

def searchBot(name, thisdir):
    '''
    dictionary "count" is imported from "filefinder.py"
    itterate through all seasons and theough all episodes inside that season
    '''
    for s in count:
        
        '''
        create a csv file containng the columns :- ['season', 'episode', 'info', 'title', 'details']
        in the same directory
        '''
        csv_file = open(f'{thisdir}/{s}.csv', 'w')
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['season', 'episode', 'info', 'title', 'details'])

        for e in count[s]:
            '''
            for each episode google search the query
            '''
            query = f'{name} {s}{e}'

            query = urllib.parse.quote_plus(query)
            #query = query.replace(' ', '+')

            url = 'https://google.com/search?q=' + query

            response = requests.get(url)

            #webbrowser.open_new_tab(url)

            '''
            Retrieve the information from google pages.
            It turns out that google pages (html pages) contains a specific template.
            The data of similar type comes and sits at same div tag for every search.
            As long as this div tags (class attribute) does not changes this program will work. 
            '''
            soup = BeautifulSoup(response.text, 'lxml')
            try:
                info = soup.find('div', class_='BNeawe tAd8D AP7Wnd').text
            except:
                info = None
            try:
                title = soup.find('div', class_='BNeawe deIvCb AP7Wnd').text
            except:
                title = None
            try:
                details = soup.find('div', class_='BNeawe s3v9rd AP7Wnd').text
            except:
                details = None

            '''
            if info field in none, it means that there is nothing found in search result.
            this can be due to two reasons:
            1.Google page has not been created yet.
            2.There does not exists any combination of such season and episode number. 
            '''
            if info:
                verify = re.findall(r"[\w']+", info)
                if 'Season' in verify and 'Episode' in verify:
                    csv_writer.writerow([s, e, info, title, details])
                else:
                    print(f'Error!, this page has not created yet')
            else:
                print(f'Error!, {name} does not have {s} {e}')
        
        csv_file.close()