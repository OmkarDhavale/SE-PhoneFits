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
data_writer.writerow(['Brand','Name','Rating','Price','RAM','ROM','Expandable Storage','Screen Size (inch)','Screen Size (cm)','Rear Cam','Selfie Cam','Battery','Processor'])

def get_links(i):
    '''
    This function fetches the URL of the item that you want to search
    '''
    URL = 'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&page=' + str(i)
    page = requests.get(URL)
    soup = BeautifulSoup(page.text,'html.parser')
    # Creating a soup object to retrieve the HTML text and using the default HTML parser to parse the HTML
    results = soup.find_all('div',class_='_1AtVbE col-12-12')
    print(len(results))
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
            price = phone.find('div',class_='_30jeq3 _1_WHN1').text
        except Exception as e :
            price = None
        try :
            ram = phone.find('li',class_='rgWa7D').text.replace(' ',';').split(';')[0]
        except Exception as e :
            ram = None
        try :
            storage = phone.find('li',class_='rgWa7D').text.replace(' ',';').split(';')[5]
        except Exception as e :
            storage = None
        try :
            exp = phone.find('li',class_='rgWa7D').text.replace(' ',';').split(';')[-2:]
            expandable = ' '.join(exp)
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
            rear_cam = phone.find_all('li')[2].text.split('|')[0].split(' ')[0]
        except Exception as e :
            rear_cam = None
        try :
            front_cam = phone.find_all('li')[2].text.split('|')[1].split(' ')[1]
        except Exception as e :
            front_cam = None
        try :
            battery = phone.find_all('li')[3].text
        except Exception as e :
            battery = None
        try :
            processor = phone.find_all('li')[4].text
        except Exception as e :
            processor = None
            # link = phone.a.get('href')
        print([brand,name,rating,price,ram,storage,expandable,display_inches,display_cm,rear_cam,front_cam,battery,processor])
        if brand != None :
            data_writer.writerow([brand,name,rating,price,ram,storage,expandable,display_inches,display_cm,rear_cam,front_cam,battery,processor])
            # link_writer.writerow([i,link])
            # print(link)
        # break

def get_phone_page(i):
    page_link = "https://www.flipkart.com" + str(i)
    return page_link


# def extract_phone_info():
#     with open('Phone links.csv', mode = 'r') as file :
#         Links = csv.reader(file)
#         for lines in Links :
#             if lines[1] == "Link" :
#                     continue
#             webpage_link = get_phone_page(lines[1])
#             phone_page = requests.get(webpage_link)
#             soup = BeautifulSoup(phone_page.content,'html.parser')
#             try :
#                 name = soup.find('h1',class_='yhB1nd').span.text.replace(" ",';').split(';')[0]
#             except Exception as e :
#                 print()
#             try :
#                 details = soup.find_all('div',class_='_3k-BhJ')
#             except Exception as e :
#                 print()
#             try :
#                 in_box = details[0].find_all('tr',class_='_1s_Smc row')[0].find('td',class_='URwL2w col col-9-12').ul.li.text
#             except Exception as e :
#                 print()
#             try :
#                 model_name = details[0].find_all('tr',class_='_1s_Smc row')[2].find('td',class_='URwL2w col col-9-12').ul.li.text
#             except Exception as e :
#                 print()
#             try :
#                 color = details[0].find_all('tr',class_='_1s_Smc row')[3].find('td',class_='URwL2w col col-9-12').ul.li.text
#             except Exception as e :
#                 print()
#             try :
#                 display_size = details[1].find_all('tr',class_='_1s_Smc row')[0].find('td',class_='URwL2w col col-9-12').ul.li.text
#             except Exception as e :
#                 print()
#             try :
#                 resolution = details[1].find_all('tr',class_='_1s_Smc row')[1].find('td',class_='URwL2w col col-9-12').ul.li.text
#             except Exception as e :
#                 print()
#             try :
#                 operating_system = details[2].find_all('tr',class_='_1s_Smc row')[0].find('td',class_='URwL2w col col-9-12').ul.li.text
#             except Exception as e :
#                 print()
#             try :
#                 processor = details[2].find_all('tr',class_='_1s_Smc row')[1].find('td',class_='URwL2w col col-9-12').ul.li.text
#             except Exception as e :
#                 print()
#             try :
#                 rom = details[3].find_all('tr',class_='_1s_Smc row')[0].find('td',class_='URwL2w col col-9-12').ul.li.text
#             except Exception as e :
#                 print()
#             try :
#                 ram = details[3].find_all('tr',class_='_1s_Smc row')[1].find('td',class_='URwL2w col col-9-12').ul.li.text
#             except Exception as e :
#                 print()
#             try :
#                 expandable_storage = details[3].find_all('tr',class_='_1s_Smc row')[3].find('td',class_='URwL2w col col-9-12').ul.li.text
#             except Exception as e :
#                 print()
#             try :
#                 primary_cameras = details[4].find_all('tr',class_='_1s_Smc row')[1].find('td',class_='URwL2w col col-9-12').ul.li.text
#             except Exception as e :
#                 print()
#             try :
#                 secondary_camera = details[4].find_all('tr',class_='_1s_Smc row')[5].find('td',class_='URwL2w col col-9-12').ul.li.text
#             except Exception as e :
#                 print()
#             try :
#                 connectivity = details[6].find_all('tr',class_='_1s_Smc row')[0].find('td',class_='URwL2w col col-9-12').ul.li.text
#             except Exception as e :
#                 print()
#             try :
#                 csv_writer.writerow([name,model_name,color,display_size,resolution,operating_system,processor,rom,ram,expandable_storage,primary_cameras,secondary_camera,connectivity,in_box])
#             except Exception as e :
#                 print()    
            

def main():
    #only 41 iterations because there were only 41 pages available to scrape 
    for i in range(1,42):
        url = get_links(i)
    # extract_phone_info()
    

main()