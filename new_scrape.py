from bs4 import BeautifulSoup
import requests
import csv

# #create a csv to contain all the links of all the phones 
# links_file = open('Phone links.csv','w',newline='')
# link_writer = csv.writer(links_file)
# link_writer.writerow(['Index','Link'])

# #create a csv to store the date of all the phones
data_file = open('Flipkart_data.csv','w',newline='',encoding='utf-8')
data_writer = csv.writer(data_file)
data_writer.writerow(['Brand','Name','Rating','Price','RAM','ROM','Expandable Storage','Screen Size (inch)','Screen Size (cm)','Rear Cam','Selfie Cam','Battery','Processor','Image Link'])

def get_links(i):
    '''
    This function fetches the URL of the item that you want to search
    '''
    URL = 'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&page=' + str(i)
    page = requests.get(URL)
    soup = BeautifulSoup(page.text,'html.parser')
    # Creating a soup object to retrieve the HTML text and using the default HTML parser to parse the HTML
    results = soup.find_all('div',class_='_1AtVbE col-12-12')
    for phone in results:
        try :
            brand = phone.find('div',class_='_4rR01T').text.replace(' ',';').split(';')[0]
        except Exception as e :
            brand = None
        try :
            name = phone.find('div',class_='_4rR01T').text.replace(' ',';').split(';')[1]
        except Exception as e :
            name = None    
        try :
            rating = phone.find('div',class_='_3LWZlK').text
        except Exception as e :
            rating = None
        try :
            price = phone.find('div',class_='_30jeq3 _1_WHN1').text.replace('₹','')
        except Exception as e :
            price = None
        try :
            ram = phone.find('li',class_='rgWa7D').text.replace(' ',';').split(';')[0]
        except Exception as e :
            ram = None
        try :
            storage = phone.find('li',class_='rgWa7D').text.replace(' ',';').split(';')[4]
        except Exception as e :
            storage = None
        try :
            expandable = phone.find('li',class_='rgWa7D').text.replace(' ',';').split(';')[-2]
            if expandable == 'MB' or expandable == 'GB' :
                expandable = None
        except Exception as e :
            expandable = None
        try :
            display_inches = phone.find_all('li')[1].text.replace('(',' ').replace(')',' ').split(' ')[3]
        except Exception as e :
            display_inches = None
        try :
            display_cm = phone.find_all('li')[1].text.replace('(',' ').replace(')',' ').split(' ')[0]
        except Exception as e :
            display_cm = None
        try :
            rear_cam = phone.find_all('li')[2].text.split('|')[0].split(' ')[0].replace('MP','')
        except Exception as e :
            rear_cam = None
        try :
            front_cam = phone.find_all('li')[2].text.split('|')[1].split(' ')[1].replace('MP','')
        except Exception as e :
            front_cam = None
        try :
            battery = phone.find_all('li')[3].text.split(' ')[0]
        except Exception as e :
            battery = None
        try :
            processor = phone.find_all('li')[4].text
        except Exception as e :
            processor = None
        try :
            image_link = phone.find('div',class_='CXW8mj').img.get('src')
        except Exception as e :
            image_link = None
            # link = phone.a.get('href')
        if brand != None :
            data_writer.writerow([brand,name,rating,price,ram,storage,expandable,display_inches,display_cm,rear_cam,front_cam,battery,processor,image_link])
            # link_writer.writerow([i,link])
            # print(link)
        # break

def get_phone_page(i):
    page_link = "https://www.flipkart.com" + str(i)
    return page_link

def main():
    #only 41 iterations because there were only 41 pages available to scrape 
    for i in range(1,42):
        url = get_links(i)
    # extract_phone_info()
    

main()