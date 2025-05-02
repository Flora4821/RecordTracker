import requests
import json
import time

headers = {
    "User-Agent": "RecordTracker/1.0 +https://github.com/Flora4821/RecordTracker",
    "Authorization": "Discogs token=ZavweCFfwrHvWXtjJYZPemwOYVUIuLeDxjrlThUP"
}

def get_wishlist(user):
    wantlist = []
    max = False
    page = 1
    max_page = requests.get(f"https://api.discogs.com//users/{user}/wants", headers=headers).json()["pagination"]["urls"]["last"]
    while max == False:
        print(f"get page {page}")
        time.sleep(1)
        url = f"https://api.discogs.com/users/{user}/wants?page={page}&per_page=50&sort=label&sort_order=asc"
        if url == max_page:
            max == True
            break
        response = requests.get(url, headers=headers)
        print(response.status_code)
        response = response.json()
        for album in response["wants"]:
            master = album["basic_information"]["master_id"]
            
            if master in wantlist:
                continue
            
            wantlist.append(master)
        page += 1
        
    with open("wantlist.json", "w", encoding="utf-8") as file:
        json.dump(sorted(wantlist), file, indent=4)
    
    
    

def main():
    get_wishlist("Flora4821")
    
if __name__ == "__main__":
    main()