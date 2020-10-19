import mechanize,time,os,sys
from bs4 import BeautifulSoup as BS


m = '\033[1;31m' # merah
b = '\033[1;36m' # biru
k = '\033[1;33m' # kuning
h = '\033[1;32m' # hijau
u = '\033[1;35m' # ungu
p = '\033[1;37m' # putih
ut = '\033[1;34m' # ungu tua

def wr(l):
	for kon in l + "\n":
		sys.stdout.write(kon);sys.stdout.flush();time.sleep(1./1000)
class sms:
	def __init__(self):
		#install browser
		self.br = mechanize.Browser()
		self.br.set_handle_equiv(True)
		self.br.set_handle_gzip(True)
		self.br.set_handle_redirect(True)
		self.br.set_handle_referer(True)
		self.br.set_handle_robots(False)
		self.br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
		self.br.addheaders =[('Connection','keep-alive'),
		('Pragma','no-cache'),
		('Cache-Control','no-cache'),
		('Origin','http://sms.payuterus.biz'),
		('Upgrade-Insecure-Requests','1'),
		('Content-Type','application/x-www-form-urlencoded'),
		('User-Agent','Opera/9.80 (Android; Opera Mini/8.0.1807/36.1609; U; en) Presto/2.12.423 Version/12.16'),
		('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'),
		('Referer','http://sms.payuterus.biz/alpha/'),
		('Accept-Encoding','gzip, deflate'),
		('Accept-Language','id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'),
		('Cookie','_ga=GA1.2.131924726.1560439960; PHPSESSID=jjrqqaakmfcgfgbtjt8tve5595; _gid=GA1.2.1969561921.1561024035; _gat=1')
		]
		self.u='http://sms.payuterus.biz/alpha/'
		self.banner()

	def banner(self):
		os.system('clear')
		time.sleep(2);
		wr(f"""{m} _____              ____
|  ___| __ ___  ___/ ___| _ __ ___  ___  
| |_ | '__/ _ \/ _ \___ \| '_ ` _ \/ __| 
{p}|  _|| | |  __/  __/___) | | | | | \__ \ 
|_|  |_|  \___|\___|____/|_| |_| |_|___/ 
{k}══════════════════════════════════════
{p}[{h}+{p}]{b}Author  : {p} MRROBO28
{p}[{h}+{p}]{b}Github  : {p} github.com/MRROBO28
{p}[{h}+{p}]{b}Youtube : {p} TEKTRIKBOT CN
{k}══════════════════════════════════════
		""")
		no=input(f'{h}Ex : 08xxxxx\n{p}[{h}?{p}] {b}Nomor Target {p}> ')
		psn=input(f'{k}[Note]{p} ketik {h}(\\n) {p}untuk garis baru pada pesan\n{p}[{h}?{p}] {b}Masukkan Pesan {p}> ')
		self.main(no,psn)

	def main(self,no,msg):
		o=[]
		bs=BS(self.br.open(self.u),features="html.parser")
		for x in bs.find_all("span"):
			o.append(x.text)
		capt=int(str(o)[2])+int(str(o)[6])
		self.br.select_form(nr=0)
		self.br.form['nohp']=no
		self.br.form['pesan']=msg
		self.br.form['captcha']=str(capt)
		sub=self.br.submit().read()
		if 'SMS Gratis Telah Dikirim' in str(sub):
			print('{p}[{b}+{p}] {h}Sukses mengirim sms ke',no)
		elif 'Mohon Tunggu' in str(sub):
			print('{m}[{k}!{m}] {k}Tunggu beberapa saat untuk mengirim sms yang sama')
		else:
			print('{k}[!] {m}Gagal mengirim sms ke',no)

try:
	sms()
	while True:
		plh=input(f"{k}\n[{m}?{k}] {h}coba lagi {p}(y/n) : ")
		if plh.lower() == 'y':
			sms()
		elif plh.lower() == 'n':
			print(f"{h}Thanks For used My script");time.sleep(1);
			print(f"{m}Exit")
			sys.exit()
except KeyboardInterrupt:
	print('\nErr: KeyboardInterrupt')
except Exception as E:
	print(f'Err: {E}')
