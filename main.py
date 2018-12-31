from bs4 import BeautifulSoup as bs
import urllib
import os

def parseUrl(url):
    url_new = ""
    for ele in url:
        if ele==" ":
            url_new = url_new + "%20"
        else:
            url_new = url_new + str(ele)
    return url_new

def getData(url,ele):
    try:
        try:
            os.makedirs(str(str(url[url.find("http://")+7:])))
        except Exception as e:
            # Ignore this error, error due to mkdir calls for existing dirs
            print("Exception at getData osmakedirs url : "+str(url+ele)+" \nType : "+str(e))
        urllib.request.urlretrieve(str(url+ele), str(str(url[url.find("http://")+7:])+ele) )  
    except Exception as e:
        print("Exception at getData url : "+str(url+ele)+" \nType : "+str(e))

def getContent(url):
    content = []
    try:
        page = urllib.request.urlopen(url).read()
        soup = bs(page,features="html5lib")
        soup.prettify()
        for ele in soup.find_all('a'):
            content.append(str(ele['href']))
        return content
    except Exception as e:
        print("Exception at getContent url : "+str(url)+" \nType : "+str(e))
        return content

def getMitfiles(url):
    try:
        content = getContent(url)
        for ele in content:
            if ele[-1]=='/':
                getMitfiles(parseUrl(url+ele))
            else:
                getData(parseUrl(url),ele)
    except Exception as e:
        print("Exception at getMitfiles url : "+str(url)+" \nType : "+str(e))

getMitfiles('http://resource.mitfiles.com/')