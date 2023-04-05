from bs4 import BeautifulSoup
import requests
import csv

#create a csv to contain all the links of all the phones 
links_file = open('Phone links.csv','w',newline='')
links = csv.writer(links_file)
links.writerow(['Index','Link'])

#create a csv to store the date of all the phones
data_file = open('data.csv','w',newline='')
data_writer = csv.writer(data_file)
data_writer.writerow(['Brand','Model Name','Color','Display Size','Resolution','Operating System','Processor','Storage','RAM','Expandable Storage','Primary Camera','Secondary Camera','Connectivity','In Box'])

def get_links(i):
    '''
    This function fetches the URL of the item that you want to search
    '''
    URL = 'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&page=' + str(i)
    page = requests.get(URL)
    soup = BeautifulSoup(page.text,'html.parser')
    data = soup.find_all('div',class_ = '_2kHMtA')

    for temp in data:
        try :
            link = temp.a.get('href')
            links.writerow([i,link])
        except Exception as e :
            print('')

def get_phone_page(i):
    page_link = "https://www.flipkart.com" + str(i)
    return page_link

def extract_phone_info():
    with open('Phone links.csv', mode = 'r') as file :
        Links = csv.reader(file)
        for lines in Links :
            if lines[1] == "Link" :
                    continue
            webpage_link = get_phone_page(lines[1])
            phone_page = requests.get(webpage_link)
            soup = BeautifulSoup(phone_page.content,'html.parser')
            try :
                name = soup.find('h1',class_='yhB1nd').span.text.replace(" ",';').split(';')[0]
            except Exception as e :
                print()
            try :
                details = soup.find_all('div',class_='_3k-BhJ')
            except Exception as e :
                print()
            try :
                in_box = details[0].find_all('tr',class_='_1s_Smc row')[0].find('td',class_='URwL2w col col-9-12').ul.li.text
            except Exception as e :
                print()
            try :
                model_name = details[0].find_all('tr',class_='_1s_Smc row')[2].find('td',class_='URwL2w col col-9-12').ul.li.text
            except Exception as e :
                print()
            try :
                color = details[0].find_all('tr',class_='_1s_Smc row')[3].find('td',class_='URwL2w col col-9-12').ul.li.text
            except Exception as e :
                print()
            try :
                display_size = details[1].find_all('tr',class_='_1s_Smc row')[0].find('td',class_='URwL2w col col-9-12').ul.li.text
            except Exception as e :
                print()
            try :
                resolution = details[1].find_all('tr',class_='_1s_Smc row')[1].find('td',class_='URwL2w col col-9-12').ul.li.text
            except Exception as e :
                print()
            try :
                operating_system = details[2].find_all('tr',class_='_1s_Smc row')[0].find('td',class_='URwL2w col col-9-12').ul.li.text
            except Exception as e :
                print()
            try :
                processor = details[2].find_all('tr',class_='_1s_Smc row')[1].find('td',class_='URwL2w col col-9-12').ul.li.text
            except Exception as e :
                print()
            try :
                rom = details[3].find_all('tr',class_='_1s_Smc row')[0].find('td',class_='URwL2w col col-9-12').ul.li.text
            except Exception as e :
                print()
            try :
                ram = details[3].find_all('tr',class_='_1s_Smc row')[1].find('td',class_='URwL2w col col-9-12').ul.li.text
            except Exception as e :
                print()
            try :
                expandable_storage = details[3].find_all('tr',class_='_1s_Smc row')[3].find('td',class_='URwL2w col col-9-12').ul.li.text
            except Exception as e :
                print()
            try :
                primary_cameras = details[4].find_all('tr',class_='_1s_Smc row')[1].find('td',class_='URwL2w col col-9-12').ul.li.text
            except Exception as e :
                print()
            try :
                secondary_camera = details[4].find_all('tr',class_='_1s_Smc row')[5].find('td',class_='URwL2w col col-9-12').ul.li.text
            except Exception as e :
                print()
            try :
                connectivity = details[6].find_all('tr',class_='_1s_Smc row')[0].find('td',class_='URwL2w col col-9-12').ul.li.text
            except Exception as e :
                print()
            try :
                data_writer.writerow([name,model_name,color,display_size,resolution,operating_system,processor,rom,ram,expandable_storage,primary_cameras,secondary_camera,connectivity,in_box])
            except Exception as e :
                print()    
            

def main():
    #only 41 iterations because there were only 41 pages available to scrape 
    for i in range(1,41):
        url = get_links(i)
    extract_phone_info()
    
main()    
