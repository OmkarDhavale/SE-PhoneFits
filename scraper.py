import csv 
from bs4 import BeautifulSoup
import requests

csv_file = open('data.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Phone name','Rating','Number of ratings','RAM','Storage','Display','Camera','Battery','Processor'])

url = 'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&page=1'
page = requests.get(url)
        
# Creating a soup object to retrieve the HTML text and using the default HTML parser to parse the HTML
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('a',{'class':"_1fQZEK"})
print(len(results))
for phone in results:
    try :
        name = phone.find('div',class_='_4rR01T').text
        rating = phone.find('div',class_='_3LWZlK').text
        no_of_ratings = phone.find('span',class_='_2_R_DZ').text.replace('\xa0&\xa0'," ; ")[0:phone.find('span',{'class':"_2_R_DZ"}).text.replace('\xa0&\xa0'," ; ").find(';')].strip()
        ram = phone.find('li',class_='rgWa7D').text[0:phone.find('li',class_='rgWa7D').text.find('|')]
        storage = phone.find('li',{'class':"rgWa7D"}).text[phone.find('li',{'class':"rgWa7D"}).text.find('|')+1:][0:11].strip()
        display = phone.find_all('li')[1].text
        cam = phone.find_all('li')[2].text
        battery = phone.find_all('li')[3].text
        processor = phone.find_all('li')[4].text
        csv_writer.writerow([name,rating,no_of_ratings,ram,storage,display,cam,battery,processor])

    except Exception as e : 
        print(e)
        