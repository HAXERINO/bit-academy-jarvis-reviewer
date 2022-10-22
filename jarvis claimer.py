import requests, re, time, json
from time import sleep

s = requests.Session()


# Je moet je eigen cookies pakken van jarvis site, ga naar https://roc-utrecht.jarvis.bit-academy.nl/a/code/reviews?state=OPEN en doe ctrl + shift + i klik dan rechtsboven op de 2 pijlen en klik op application.
# Ga dan naar Cookies -> https://roc-utrecht.jarvis.bit... en dan moet je alle waardes van de cookies pakken en hier beneden vervangen met X

cookies = {'MMUSERID': 'X', 'MMAUTHTOKEN': 'X', 'j_refresh_token': 'X',
 'userLastLocation': 'X', 'Authorization': 'X',
 'JSESSIONID': 'X', 'XSRF-TOKEN': 'X'}


headers = {'x-xsrf-token': 'X', 'Content-type': 'application/json', 'referer': 'https://roc-utrecht.jarvis.bit-academy.nl/a/code/reviews?state=OPEN', 
'origin': 'https://roc-utrecht.jarvis.bit-academy.nl'} # x-xrsrf-token is et zelfde als XSRF-TOKEN hierboven
doubl = "doubl"

while True:
    time.sleep(1)
    r = s.get(
        'https://roc-utrecht.jarvis.bit-academy.nl/api/v1/reviews?state=OPEN', cookies=cookies)

    if 'name' in r.text:
        print("Nieuwe review gevonden!")
        review_id = r.json()[0]['id']
        r = s.post('https://roc-utrecht.jarvis.bit-academy.nl/api/v1/reviews/' +
                   # EIGEN ID HIER TOEVOEGEN # EIGEN ID HIER TOEVOEGEN # EIGEN ID HIER TOEVOEGEN # EIGEN ID HIER TOEVOEGEN # EIGEN ID HIER TOEVOEGEN
                   review_id + '/assign', cookies=cookies, json={"id":"EIGEN ID HIER"}, headers=headers) # EIGEN ID HIER TOEVOEGEN
        print(r.text)
        if doubl == "doubl":
            print("Review geclaimed")
        else:
            print(r.text)
            print("Review kon niet worden geclaimed :(")
        time.sleep(5)
        payload = "{}"

        r = s.post('https://roc-utrecht.jarvis.bit-academy.nl/api/v1/reviews/' +
                   review_id + '/accept', cookies=cookies, data="{}", headers=headers)
        if doubl == "doubl":
            print(r.text)
            print("Review geaccepteerd")
        else:
            print(r.text)
            print("Review kon niet worden geaccepteerd :(")

    elif r.text == "[]":
        print("Geen nieuwe review gevonden!")

    else:
        print("Onbekende error tijdens het checken voor reviews")
