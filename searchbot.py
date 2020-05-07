from bs4 import BeautifulSoup
import urllib, requests, webbrowser, csv
from collections import defaultdict
from filefinder import count

def searchBot(name):
    for s in count:
        csv_file = open(f'{s}.csv', 'w')
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['season', 'episode', 'info', 'title', 'details'])
        for e in count[s]:
            
            query = f'{name} {s}{e}'

            query = urllib.parse.quote_plus(query)
            #query = query.replace(' ', '+')

            url = 'https://google.com/search?q=' + query

            response = requests.get(url)

            #webbrowser.open_new_tab(url)


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
            
            csv_writer.writerow([s, e, info, title, details])
        
        csv_file.close()
    
#print(soup.prettify())
# with open("output1.html", "w") as file:
#     file.write(str(soup.prettify()))

'''kno-ecr-pt PZPZlf gsmt i8lZMc sKbx2c
kno-ecr-pt PZPZlf gsmt i8lZMc hNKfZe
kno-ecr-pt PZPZlf gsmt i8lZMc'''