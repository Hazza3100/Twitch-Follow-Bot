import requests
import threading
import random

from colorama import Fore, init

init(convert=True)


channel_name = input("Enter Channel: ")


def get_username():

    json = {"operationName": "ChannelShell",
            "variables": {
                "login": channel_name
            },
            "extensions": {
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": "580ab410bcd0c1ad194224957ae2241e5d252b2c5173d8e0cce9d32d5bb14efe"
                }
            }
        }

    headers = {
        'Client-ID': 'kimne78kx3ncx6brgo4mv6wki5h1ko'
    }
    r = requests.post('https://gql.twitch.tv/gql', json=json, headers=headers)
    return r.json()['data']['userOrError']['id']


channel_ID = get_username()




def follow():

    for i in range(7):
        tokens = open('tokens.txt', 'r').read().splitlines()
        token = random.choice(tokens)
        
        headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-GB',
        'Authorization': f'OAuth {token}',
        'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
        'Connection': 'keep-alive',
        'Content-Type': 'text/plain;charset=UTF-8',
        'Origin': 'https://www.twitch.tv',
        'Referer': 'https://www.twitch.tv/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = '[{"operationName":"FollowButton_FollowUser","variables":{"input":{"disableNotifications":false,"targetID":"'+channel_ID+'"}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"800e7346bdf7e5278a3c1d3f21b2b56e2639928f86815677a7126b093b2fdd08"}}}]'
    r = requests.post('https://gql.twitch.tv/gql', headers=headers, data=data)
    if r.status_code == 200:
        print(f"{Fore.GREEN}Followed {Fore.RESET}{channel_name}{Fore.RESET}\n")
    else:
        print(F"{Fore.RED}Error{Fore.RESET}\n")




def start():
    print("Sending followers")
    while True:
        threading.Thread(target=follow).start()




start()
