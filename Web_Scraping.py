import requests
from bs4 import BeautifulSoup
def get_top_repo(s,n,m):
    url = f"https://github.com/topics/{s}?o=desc&s=forks"
    response= requests.get(url)
    r_code = response.status_code
    if r_code != 200:
        print("Unknown Error Occurred")
        return
    html_content = response.content
    dom = BeautifulSoup(html_content,'html.parser')
    fr = dom.select("h3")
    res = []
    count = 0
    for repo in fr:
        if count < n:    
            t = repo.find_all("a",{"class":"text-bold wb-break-word"})
            g = str(t)
            h = g.split('href')
            m = h[-1].split('">')
            if len(m) == 1:
                pass
                count -= 1
            else:
                res.append("github.com/"+m[0][3:])
        else:
            break
        count += 1
    return res
