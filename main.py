from bs4 import BeautifulSoup
import requests

#-------------------------------------------------- << FUNCTIONS >> --------------------------------------------------#

def where_is_my_bus(bus_stop_no):
    
    url = f'https://atus.konya.bel.tr/atus/otobusum-nerede?durakNo={bus_stop_no}'
    
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }
    
    response = requests.get(url = url, headers = headers)
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    table = soup.find('tbody', {'id' : 'searchBody'})
    
    rows = table.find_all('tr')
    
    data = []
    
    for row in rows:
        
        route_no = row.find('td', class_='tdHatno').text # Hat No
        name = row.find('td', class_='tdAdi').text # Adı
        direction = row.find('td', class_='tdYon').text # Yön
        duration = row.find('td', class_='tdSure').text # Süre
        
        if duration != '':
            
            duration = duration[:-3] if duration != 'DURAKTA' else 0
            
            data.append({'route_no': route_no, 'name': name, 'direction': direction, 'duration': int(duration)})
    
    data.sort(key = lambda item: item['duration']) # Sorting data based on duration
    
    return data

#-------------------------------------------------- << MAIN FUNCTION >> --------------------------------------------------#              

def main():
    
    bus_stop_no = 26 # "Anıt" Bus Stop
    
    data = where_is_my_bus(bus_stop_no)

    for bus in data:
        
        print(bus)
        
#-------------------------------------------------- << RUN >> --------------------------------------------------#

if __name__ == '__main__':
    
    main()
