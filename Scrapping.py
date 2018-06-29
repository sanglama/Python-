import urllib
import urllib.request as u
import re
from bs4 import BeautifulSoup
import csv
filename = "Scrapping.csv"
with open(filename, 'w+') as f:
    writer = csv.writer(f)
    for i in list(range(1,12)):
        url="http://www.aiovision.org/members-list/page/"+str(i)+"/"
        page= u.urlopen(url)
        soup=BeautifulSoup(page,"html.parser")
        containers=soup.findAll("div",{"class":"one_half"})
        for container in containers:
            gmail=''
            website=''
            telephone=''
            zipcode=''
            address=''
            title=(str(container.div.h2.a["title"]))
            details=list((container.div.div.div.text.split("\n")))
            for detail in details[::-1]:
                if "@" in detail:
                    s=details.index(detail)
                    gmail=(detail)
                    del details[s:-1]
                elif "co.uk" in detail or "www." in detail:
                    website=(detail)
                    s = details.index(detail)
                    del details[s:-1]
                elif "Tel" in detail  or 'TEL' in detail:
                    telephone=detail[4:-1]
                    s = details.index(detail)
                    del details[s:-1]
            for detail in details[::-1]:
                if str(re.findall("[0-9]{5,}",detail)) in detail or "02" in detail or "01" in detail :
                    telephone=detail
                    s = details.index(telephone)
                    del details[s:-1]
            try:
                zipcode=details[-2]
                details.__delitem__(-2)
            except:
                print("")
            address=" ".join(details)
            row=[title,address,zipcode,telephone,website,gmail]
            writer.writerow(row)

