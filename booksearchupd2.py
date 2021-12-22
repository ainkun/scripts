import bs4
import urllib.request
import csv
from datetime import datetime
import os

def htmltotext(htmlfile):
    raw = bs4.BeautifulSoup(html, 'html.parser')
    text = str(raw)
    return text

def curtime():
    now = datetime.now()
    time = now.strftime("%d/%m/%Y %H:%M:%S")
    return time

def headcheck(header):
        if header[2]=='TITLE':
            return False 
        else:
            return True




location = os.path.expanduser('~')+'\\Desktop\\test.csv'
fileexist = os.path.isfile(location)


apilink1 = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
apilink2 = "https://www.goodreads.com/search/index.xml?key=<input_api_key>&q="

titlearray=[]
authorarray=[]
isbnarray=[]
bookcount = 0


while True:

    while True:
        isbninput = str(input("Enter the ISBN number of the book: ")).strip()
        try:
            if type(int(isbninput))==int:
                if len(str(isbninput))==13:
                    break
        except:
            print("Invalid Input! Try again.")
            continue
    count=0      
    if fileexist == True:
        with open(location, 'r') as f:
            read = csv.reader(f)
            for i in read:
                if count==0:
                    header=i[:]

                if i[1] == isbninput+'"':
                    isbncheck=True
                    break
                else:
                    isbncheck = False
                count += 1

    if isbncheck==True or isbninput in isbnarray:
        print('This book is already available in the datasheet!')
        continue

    html = urllib.request.urlopen(apilink1+isbninput).read()

    if len(html) < 60:
        html = urllib.request.urlopen(apilink2+isbninput).read()
        if len(html) < 600:
            while True:
                tryagain = str(input("This book is not available! Do you want to try again?(Y/N): ")).upper()
                if tryagain == 'Y' or tryagain == 'N':
                    break

            if tryagain == 'Y':
                continue
            else:
                break

        text = htmltotext(html)
        apigoogle = False
    else:
        text = htmltotext(html)
        apigoogle = True

    if apigoogle == True:
        title = text[text.find('"title": "')+len('"title": "'):text.find('",', text.find('"title": "'))]
        author = text[text.find('"authors": [\n     "')+len('"authors": [\n     "'):text.find('"\n', text.find('"authors": [\n     "'))]
    else:
        title = text[text.find('<title>')+len('<title>'):text.find('</title>')]
        author = text[text.find('<name>')+len('<name>'):text.find('</name>')]
    
    bookcount +=1  
    titlearray.append(title)
    authorarray.append(author)
    isbnarray.append(isbninput)

    while True:
        choice = str(input("Do you want to Enter another book?(Y/N): ").upper())
        if choice == 'Y' or choice == 'N':
            break
    if choice == 'N':
        break

for i in range(bookcount):
    print(i+1, isbnarray[i], titlearray[i], authorarray[i])

with open(location, 'a', newline='') as fp:
    write = csv.writer(fp, delimiter=',')
    heading = [['TIME', 'ISBN-No.', 'TITLE', 'AUTHOR']]
    if fileexist == False:
        write.writerows(heading)
    elif headcheck(header) == True:
        write.writerows(heading)

    for i in range(bookcount):
        data = [[curtime(), str(isbnarray[i]+'"'), titlearray[i],authorarray[i]]]
        write.writerows(data)
