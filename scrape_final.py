from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('data.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Phone name','Rating','Number of ratings','RAM','Storage','Display','Camera','Battery','Processor'])

#page = requests.get('https://www.flipkart.com/mobiles/pr?sid=tyy,4io&otracker=categorytree')
#soup = BeautifulSoup(page.text,'html.parser')
def get_url(i):
    '''
    This function fetches the URL of the item that you want to search
    '''
    URL = 'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&page={i}'
    return URL

def extract_phone_info(phone):
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

def main(search_item):#341
    for i in range(2):
        url = get_url(i)
        page = requests.get(url)
        soup = BeautifulSoup(page.text,'html.parser')
        list_of_phones = soup.find_all('div',class_='_13oc-S')
        for phone in list_of_phones:
            extract_phone_info(phone)

    

