import requests, re, time, json
from time import sleep

s = requests.Session()


# Je moet je eigen cookies pakken van jarvis site, ga naar https://roc-utrecht.jarvis.bit-academy.nl/a/code/reviews?state=OPEN en doe ctrl + shift + i klik dan rechtsboven op de 2 pijlen en klik op application.
# Ga dan naar Cookies -> https://roc-utrecht.jarvis.bit... en dan moet je alle waardes van de cookies pakken en hier beneden vervangen met X

cookies = {'MMUSERID': 'X', 'MMAUTHTOKEN': 'X', 'j_refresh_token': 'X',
 'userLastLocation': 'X', 'Authorization': 'X',
 'JSESSIONID': 'X', 'XSRF-TOKEN': 'X'}

headers = {'x-xsrf-token': 'XSRF TOKEN HIER', 'Content-type': 'application/json'} # Het zelfde als XSRF-TOKEN hierboven

while True:
    time.sleep(1)
    r = s.get(
        'https://roc-utrecht.jarvis.bit-academy.nl/api/v1/reviews?state=OPEN', cookies=cookies)

    if 'name' in r.text:
        print("Nieuwe review gevonden!")
        review_id = r.json()[0]['id']
        print("Review ID gepakt + " + review_id)
        reviewer_id = r.json()[0]['reviewer']['id'] 
        print("Reviewer ID gepakt + " + reviewer_id)
        r = s.post('https://roc-utrecht.jarvis.bit-academy.nl/api/v1/reviews/' +
                   review_id + '/assign', cookies=cookies, data={'reviewer': reviewer_id}, headers=headers)

        # r = s.post('https://roc-utrecht.jarvis.bit-academy.nl/api/v1/reviews/' + deid + '/assign', cookies=cookies, json={"id": "value"})

        print(r.text)
        if "20" in r.status_code:
            print("Review geclaimed")
        else:
            print(r.text)
            print("Review kon niet worden geclaimed :(")
        time.sleep(5)
        payload = "{}"

        r = s.post('https://roc-utrecht.jarvis.bit-academy.nl/api/v1/reviews/' +
                   review_id + '/accept', cookies=cookies, data=payload, headers=headers)
        if "20" in r.status_code:
            print("Review geaccepteerd")
        else:
            print(r.text)
            print("Review kon niet worden geaccepteerd :(")

    elif r.text == "[]":
        print("Geen nieuwe review gevonden!")

    else:
        print("Onbekende error tijdens het checken voor reviews")