import os
import csv
from bs4 import BeautifulSoup
import initialize


#create a basic html file
def createTemplate(src):
    #add these contents
    contents = '''
    <html>
    <head>
    <style>
    h1 {color: #ffffff; background-color: #224c43; font-family: Verdana; font-size: xx-large; height: 80px; text-align: center; vertical-align: middle; padding-top: 30px;}
    body {padding: 20px; background-color: #50756d;}
    li {background-color: wheat; padding-left: 15px; padding-top: 20px; padding-bottom: 20px; list-style-type: none;}
    a:link {color: #50756d; text-decoration: none; font-weight: bold; font-family: Verdana; font-size: x-large; vertical-align: middle; padding-left: 25px;}
    input {color: #224c43; height:40px; width: 40px; vertical-align: middle;}
    input[type=search] {padding-left: 15px; height: 40px; width: 500px; vertical-align: middle; font-size: large; font-family: Verdana; font-weight: bold; color: #224c43;}
    button {color: #224c43; height: 40px; width: auto; vertical-align: middle; font-size: large; font-family: Verdana; font-weight: bold;}
    h3 { padding-left: 35px;}
    </style>
    <meta charset="utf-8" />
    <title>Links to print numbers</title>
    <h1>Click each link and send message.</h1>
    </head>
    <body>
    <h3 id="search-bar">
    <form role="search" id="form">
    <input type="search" id="query" placeholder="Search for phone number...">
    <button type="submit">Search</button>
    </form>
    </h3>
    <ul>

    </ul>
    <script>
    const form = document.getElementById('form');
    const query = document.getElementById('query');
    function searchNumber(event) {
    event.preventDefault();
    let phone = query.value;
    let target = document.getElementById(phone)
    console.log(target)
    target.scrollIntoView(true)
    }
    form.addEventListener('submit', searchNumber)
    </script>
    </body>
    </html>
    '''
    #idempotence statement
    if 'text_list.html' not in os.listdir(src):
        #create new html file
        htmlFile = open(f'{src}/text_list.html', 'w')
        htmlFile.write(contents)
    else:
        #quit if file already exists
        print('HTML file already exists. Delete your current version of HTML file.')
        quit

def makeLinks(src, csvFile):
    #open csv
    with open(f'{src}/{csvFile}') as data:
        #extract csv data
        csvreader = csv.reader(data)
        #iterate through rows in the csv file
        for row, column in enumerate(csvreader):
            #open html file
            htmlFile = open(f'{src}/text_list.html')
            htmlRead = htmlFile.read()
            #extract html
            soup = BeautifulSoup(htmlRead, 'html.parser')
            #get rid of title row
            if row != 0:
                #establish variables
                #if both numbers are empty skip this iteration
                if len(column[2]) == 0 and len(column[3]) == 0:
                    last = column[0]
                    first = column[1]
                    print(f'There are no phone numbers for {first} {last}')
                    continue
                #if mobile number is empty use phone number
                elif len(column[3]) == 0:
                    last = column[0]
                    first = column[1]
                    phone = column[2]
                    formHTML(src, row, soup, first, last, phone)
                #if both numbers are filled in default to mobile number
                else: 
                    last = column[0]
                    first = column[1]
                    phone = column[3]
                    formHTML(src, row, soup, first, last, phone)
                
#make and append HTML elements
def formHTML(src, row, soup, first, last, phone):
    excelRow = row + 1
    message = initialize.prompt_for_message()
    #format text message for link
    textMessage = message.replace(' ', '%20')
    #creat new lime break item
    lnBrk = soup.new_tag('br')
    #create new list item
    newLs = soup.new_tag('li', id = f'{phone}')
    #create new link
    newLink = soup.new_tag('a', href = f'sms:{phone}&body={textMessage}')
    newLink.string = f'{first} {last} | {phone} | Row {excelRow} in Excel.'
    #create a checkbox next to link
    box = soup.new_tag('input', type = 'checkbox')
    #append list item into unordered list
    soup.ul.append(newLs)
    #append checkbox into list item
    newLs.append(box)
    #append link into list item
    newLs.append(newLink)
    #append line break into unordered list
    soup.ul.append(lnBrk)
    #organize new html contents
    newSoup = soup.prettify()
    #save new html contents
    with open(f'{src}/text_list.html', 'w') as file:
        file.write(newSoup)