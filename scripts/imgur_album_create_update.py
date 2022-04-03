from bs4 import BeautifulSoup
import requests
import sys
import time
from imgur_album_deets import client_id, client_secret, access_token, refresh_token

filename = sys.argv[1]

print(f'using client ID {client_id} and secret {client_secret}')

# info from https://apidocs.imgur.com/#authorization-and-oauth

# need to authorize with https://api.imgur.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&response_type=REQUESTED_RESPONSE_TYPE&state=APPLICATION_STATE

# https://api.imgur.com/oauth2/addclient
# https://api.imgur.com/oauth2/authorize
# https://api.imgur.com/oauth2/token
# You can also verify your OAuth 2.0 tokens by setting your header and visiting the page

# https://api.imgur.com/oauth2/secret

# you can run this script from the top level by going
#
# date; python3 scripts/imgur_album_create_update.py pkto_cockatrice.xml
#
# you have to set the client ID and secret of course

album_name = "Pokécube album"

album_id = 'Q6aqDwK'

last_updated_card = "Ditto"


def get_image_name_to_urls_dict():

    # set this if we get to the point
    should_skip_cards = True

    print(f'Loading file... {filename}')
    urls = dict()

    with open(filename, "r") as f:
        soup_obj = BeautifulSoup(f, "xml")

        # grab the list of cards out of the input cockatrice xml file
        all_cards = soup_obj.findAll("card")

        for index in range(len(all_cards)):

            cockatrice_card = all_cards[index]

            for name_tag in cockatrice_card:
                if name_tag.name == 'name':
                    card_name = name_tag.string

                    if should_skip_cards:
                        if card_name == last_updated_card:
                            should_skip_cards = False
                            continue
                        else:
                            continue

                    urls[card_name] = (cockatrice_card.set['picURL'])

    return urls


def create_image(card_name, accessToken, image_url, album_id):

    url = "https://api.imgur.com/3/image"

    payload = {'image': f'{image_url}',
               'type': 'url',
               'description': f'image for {card_name}',
               'title': card_name,
               'album': album_id}
    files = [

    ]
    headers = {
        'Authorization': f'Bearer {accessToken}'
    }

    response = requests.request(
        "POST", url, headers=headers, data=payload, files=files)

    print(response.text)
    return response


def create_album(accessToken, album_name):
    url = "https://api.imgur.com/3/album"

    payload = {'ids[]': '{{imageHash}}',
               'title': album_name,
               'description': 'Pokecube album',
               'cover': '{{imageHash}}'}
    files = [

    ]
    headers = {
        'Authorization': f'Bearer {accessToken}'
    }

    response = requests.request(
        "POST", url, headers=headers, data=payload, files=files)

    print(response.text)


def get_access_token(clientId, clientSecret, refresh_token):
    url = "https://api.imgur.com/oauth2/token"

    payload = {'refresh_token': refresh_token,
               'client_id': clientId,
               'client_secret': clientSecret,
               'grant_type': 'refresh_token'}
    files = [

    ]
    headers = {}

    response = requests.request(
        "POST", url, headers=headers, data=payload, files=files)
    print(f'response: {response}')


def get_credits(access_token):
    url = 'https://api.imgur.com/3/credits'

    payload = {}
    files = [

    ]
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.request(
        "GET", url, headers=headers, data=payload, files=files)
    return response.json()['data']['UserRemaining']


def upload_cards():
    cardList = get_image_name_to_urls_dict()
    index = 0
    for cardInfo in cardList.items():
        index += 1
        print(f'   {cardInfo[0]}: {cardInfo[1]}')
        response = create_image(
            cardInfo[0], access_token, cardInfo[1], album_id)
        if response.status_code != 200:
            print("stopping :(")
            break
        time.sleep(20)


upload_cards()
