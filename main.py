import os
import requests
import threading

from itertools import cycle
from colorama import Fore, init


init(convert=True)



class stats():
    sent = 0
    error = 0



def get_username(channel_name):

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


class Choose_Cookie():

    def get_token():
        with open('tokens.txt', 'r') as f:
            tokens = [line.strip('\n') for line in f]
        return tokens
    cookie = get_token()
    tokens_loop = cycle(cookie)




sem = threading.Semaphore(200)


channel_name = input("Enter channel name > ")

class Twitch():

    def follow():
        with sem:
            os.system(f'title Success: {stats.sent} ^| Error: {stats.error}')
            channel_ID = get_username(channel_name)

            token = next(Choose_Cookie.tokens_loop)

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
                stats.sent += 1
                print(f"{Fore.GREEN}[+] Followed {Fore.RESET}{channel_name}{Fore.RESET}\n")
            else:
                stats.error += 1
                print(F"{Fore.RED}Error{Fore.RESET}\n")

    def unfollow():
        with sem:
            os.system(f'title Success: {stats.sent} ^| Error: {stats.error}')
            channel_ID = get_username(channel_name)

            token = next(Choose_Cookie.tokens_loop)

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

            data = '[{"operationName":"FollowButton_UnfollowUser","variables":{"input":{"targetID":"'+channel_ID+'"}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"f7dae976ebf41c755ae2d758546bfd176b4eeb856656098bb40e0a672ca0d880"}}}]'
            r = requests.post('https://gql.twitch.tv/gql', headers=headers, data=data)
            if r.status_code == 200:
                stats.sent += 1
                print(f"{Fore.GREEN}[+] Unfollow {Fore.RESET}{channel_name}{Fore.RESET}\n")
            else:
                stats.error += 1
                print(F"{Fore.RED}Error{Fore.RESET}\n")



def menu():
    print("[1] Follow\n[2] Unfollow")

    choice = int(input(("Enter option > ")))

    if choice == 1:
        threads = input("Enter amount of follows > ")
        for i in range(int(threads)):
            threading.Thread(target=Twitch.follow).start()

    if choice == 2:
        threads = input("Enter amount of follows > ")
        for i in range(int(threads)):
            threading.Thread(target=Twitch.unfollow).start()





menu()
