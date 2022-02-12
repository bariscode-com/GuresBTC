from asyncio import TimerHandle
from time import sleep
import requests
from bs4 import BeautifulSoup
import datetime

for x in range(3700,9999999999999999999999999999999999):
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


    
