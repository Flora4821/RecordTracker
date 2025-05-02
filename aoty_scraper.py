import requests
from bs4 import BeautifulSoup

def get_ratings(user, threshhold):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }   
    
    records_info = []
    url = f"https://www.albumoftheyear.org/user/{user}/ratings/"
    print(url)
    i = 1
    page_exists = True
    while page_exists == True:
        response = requests.get(url + f"{i}/", headers=headers)
        print(url)
        if response.status_code != 200:
            print(response.status_code)
            page_exists == False
            break
        
        
        soup = BeautifulSoup(response.text, "html.parser")
        records = soup.find_all("div", {"class": "albumBlock"})
        for r in records:
            rating = int(r.find("div", {"class": "rating"}))
            name = r.find("div", {"class": "albumTitle"})
            artist = r.find("div", {"class": "artistTitle"})
            
            if rating < threshhold:
                continue
            
            records_info.append({
                "Name": name,
                "Artist": artist
            })
    
    return records_info
        
def main():
    print(get_ratings("flora4821", 0))
    
if __name__ == "__main__":
    main()