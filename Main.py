from asyncio import TimerHandle
from time import sleep
import requests
from bs4 import BeautifulSoup
import datetime
import socket
# import telebot
# from telethon.sync import TelegramClient
# from telethon.tl.types import InputPeerUser, InputPeerChannel
# from telethon import TelegramClient, sync, events

# api_id = 'API_id'
# api_hash = 'API_hash'
# token = 'bot token'
# message = "Working..."
# phone = 'YOUR_PHONE_NUMBER_WTH_COUNTRY_CODE'
# client = TelegramClient('session', api_id, api_hash)
# client.connect()
# if not client.is_user_authorized():
  
#     client.send_code_request(phone)
     
#     # signing in the client
#     client.sign_in(phone, input('Enter the code: '))
  
  
# try:
#     # receiver user_id and access_hash, use
#     # my user_id and access_hash for reference
#     receiver = InputPeerUser('user_id', 'user_hash')
 
#     # sending message using telegram client
#     client.send_message(receiver, message, parse_mode='html')
# except Exception as e:
     
#     # there may be many error coming in while like peer
#     # error, wrong access_hash, flood_error, etc
#     print(e);
 
# # disconnecting the telegram session
# client.disconnect()

def internet(host="8.8.8.8", port=53, timeout=3):
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        sleep(1)
        return False

start = input("Start on page :")
intstart = int(start)
for x in range(intstart,4631683569492647816942839400347516314113502571162996175304206525660726459774):
    if (internet()):
        page = requests.get("https://www.bitcoinlist.io/"+str(x))
        if(page.status_code == 200):
            soup = BeautifulSoup(page.content, 'html.parser')
            for i in range(25):
                date = datetime.datetime.now()
                try:
                    main_table = soup.find_all('tr', class_="main_table")[i]
                    private_key = main_table.find_all('td')[0].text.strip()
                    address = main_table.find_all('td')[1].text.strip()
                    balance = main_table.find_all('td')[3].text.strip()
                    f_balance = float(balance)
                    if (f_balance > 0):
                        print("\n")
                        print(str(date)+" : Balance before verify blokchain: "+str(f_balance)+" BTC.")
                        print(str(date)+" : Request to https://blockchain.info/rawaddr/"+address)
                        r = requests.get("https://blockchain.info/rawaddr/"+address)
                        r.encoding
                        r.text
                        hasil = r.json()
                        blc = float(hasil.get('final_balance'))
                        print(str(date)+" : Balance after verify blokchain:"+ str(blc)+" BTC"+"\n")
                        if(blc > 0):
                            print(str(date)+" : Add data valid_balance_bitcoin.txt")
                            try:
                                text = str(date)+"\n"+"Balance: " + str(blc) + " BTC"+"\n"+"Private Key: " + private_key+"\n"+"Address: " + address+"\n"
                                obj_file = open('valid_balance_bitcoin.txt', 'a')
                                obj_file.write(text)
                                obj_file.close()
                            except IOError as err:
                                print(str(date)+" : Terjadi kesalahan: ".format(err))
                            sleep(1)
                        else:
                            print(str(date)+" : Add data in invalid_balance_bitcoin.txt")
                            try:
                                text_invalid = str(date)+"\n"+"Balance: " + str(f_balance) + " BTC"+"\n"+"Private Key: " + private_key+"\n"+"Address: " + address+"\n"
                                invalidfile = open('invalid_balance_bitcoin.txt', 'a')
                                invalidfile.write(text_invalid)
                                invalidfile.close()
                            except IOError as err:
                                print(str(date)+" : Terjadi kesalahan: ".format(err))
                            sleep(1)
                    else:
                        print(str(date)+" : No balance line "+str(i)+" in page "+str(x))
                        sleep(0.1)
                except:
                    print(str(date)+" : No balance line "+str(i)+" in page "+str(x))
                    sleep(0.1)
        else:
            print(str(date)+" : Error on page "+str(x))
        print("\n")
        print(str(date)+" : https://www.bitcoinlist.io/"+str(x))
        sleep(1)
    else:
        intstart -= 1
        print("Connecting to internet access in "+str(x))

    
