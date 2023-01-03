from selenium import webdriver
from bs4 import BeautifulSoup
import csv




# Use the Chrome webdriver to open the page
driver = webdriver.Chrome()
driver.get('https://seanprashad.com/leetcode-patterns/')

# Wait for the table to be rendered
driver.implicitly_wait(10)

# Get the HTML source of the page
html = driver.page_source

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find the table with the desired class name
table = soup.find('table', class_='table table-borderless table-striped table-hover')

# Find all rows in the table with a role attribute equal to row
rows = table.find_all('tr', attrs={'role': 'row'})


all_data = [ ]
# Extract the data from each row
for row in rows:
    cells = row.find_all('td')
    data = []
    if len(cells) > 0:
        imgs = cells[5].find_all('img')
        for img in imgs:
            data_tip = img.get('data-tip')
            cells[5].append(data_tip[9:-5])
        a = cells[2].find_all('a')
        href = a[0].get('href')
        cells[2] = href
        for i,cell in enumerate(cells):
            if i == 0:
                continue
            elif i == 2:
                 data.append(cell)
            else:
                data.append(cell.text)
        all_data.append(data)
        print(data)

with open('data.csv', 'w') as csvfile:
    fieldnames = ['Problem Name', 'Link', 'Topic', 'Difficulty', 'Competency']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for data in all_data:
        writer.writerow({'Problem Name': data[0], 'Link': data[1] ,'Topic': data[2], 'Difficulty':data[3], 'Competency':data[4] })
    

# Close the webdriver
driver.close()
