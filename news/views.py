from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse


toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html5lib')

toi_headings = toi_soup.find_all('h2')

toi_headings = toi_headings[2:16]

toi_news = []

for th in toi_headings:
    toi_news.append(th.text)



categ_sp= requests.get("https://timesofindia.indiatimes.com/briefs/sports")
toi_sp = BeautifulSoup(categ_sp.content, 'html5lib')
toi_hgs = toi_sp.findAll('h2')
toi_hgs = toi_hgs[3:14] 
toi_newsp = []

for toi_sp in toi_hgs:
    toi_newsp.append(toi_sp.text)



categ_spx= requests.get("https://www.outlookindia.com/sports")
ot_sp = BeautifulSoup(categ_spx.content, 'html5lib')
ot_hgs = ot_sp.findAll('h4')
ot_hgs = ot_hgs[2:13]
ot_newsp = []

for ot_sp in ot_hgs:
    ot_newsp.append(ot_sp.text)


categ_pox= requests.get("https://www.outlookindia.com/topic/politics/101551/2")
ot_po = BeautifulSoup(categ_pox.content, 'html5lib')
ot_hgpo = ot_po.findAll('h4')
ot_hgpo=ot_hgpo[2:15]
ot_newspo=[]


for ot_po in ot_hgpo:
    ot_newspo.append(ot_po.text)



categ_po= requests.get("https://timesofindia.indiatimes.com/politics/news")
toi_po = BeautifulSoup(categ_po.content, 'html5lib')
toi_hgpo = toi_po.findAll("span", {"class": "w_tle"})
toi_hgpo=toi_hgpo[2:15]
toi_newspo=[]


for toi_po in toi_hgpo:
    toi_newspo.append(toi_po.text)


categ_edu= requests.get("https://indianexpress.com/section/education/")
ixe_edu = BeautifulSoup(categ_edu.content, 'html5lib')
ixe_hgedu = ixe_edu.findAll('h2')
ixe_hgedu=ixe_hgedu[2:17]
ixe_newsedu=[]


for ixe_edu in ixe_hgedu:
    ixe_newsedu.append(ixe_edu.text)

categ_tec= requests.get("https://www.gadgetsnow.com/tech-news")
toi_tec = BeautifulSoup(categ_tec.content, 'html5lib')
toi_hgtec = toi_tec.findAll("span", {"class": "w_tle"})
toi_hgtec=toi_hgtec[2:15]
toi_newstec=[]


for toi_tec in toi_hgtec:
    toi_newstec.append(toi_tec.text)

categ_tecx= requests.get("https://www.outlookindia.com/topic/science-technology")
ot_tec = BeautifulSoup(categ_tecx.content, 'html5lib')
ot_hgtec = ot_tec.findAll('h4')
ot_hgtec=ot_hgtec[2:15]
ot_newstec=[]


for ot_tec in ot_hgtec:
    ot_newstec.append(ot_tec.text)


ot_r = requests.get("https://www.outlookindia.com/national")
ot_soup = BeautifulSoup(ot_r.content, 'html5lib')
ot_headings = ot_soup.findAll('p')
ot_headings = ot_headings[2:12]
ot_news = []

for oth in ot_headings:
    ot_news.append(oth.text)

categ_wea= requests.get("https://indianexpress.com/section/weather/")
ixe_wea = BeautifulSoup(categ_wea.content, 'html5lib')
ixe_hgwea = ixe_wea.findAll('h2')
ixe_hgwea=ixe_hgwea[2:17]
ixe_newswea=[]


for ixe_wea in ixe_hgwea:
    ixe_newswea.append(ixe_wea.text)


def home(req):
    return render(req, 'index.html')
def main(req):
    return render(req, 'PblProject.html', {'toi_news':toi_news, 'ot_news': ot_news})

def aboutx(req):
    return render(req, 'about.html')

def categories_sp(req):
    return render(req, 'PblProject_sp.html',{'toi_newsp':toi_newsp ,'ot_newsp':ot_newsp})

def categories_po(req):
    return render(req, 'PblProject_po.html',{'toi_newspo':toi_newspo ,'ot_newspo':ot_newspo})

def categories_edu(req):
    return render(req, 'PblProject_edu.html',{'ixe_newsedu':ixe_newsedu})

def categories_tec(req):
    return render(req, 'PblProject_tec.html',{'toi_newstec':toi_newstec ,'ot_newstec':ot_newstec})

def categories_wea(req):
    return render(req, 'PblProject_wea.html',{'ixe_newswea':ixe_newswea})










