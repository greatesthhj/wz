import urllib.request
from bs4 import BeautifulSoup
import re
response = urllib.request.urlopen("http://opinion.people.com.cn/")
shouye0 = response.read()
shouyehtml = BeautifulSoup(shouye0, "html.parser")
pattern = r'<strong><a href="(.*?)" target="_blank">'
lianjie = re.findall(pattern, str(shouyehtml))
for i in lianjie:
    wenzhang = urllib.request.urlopen("http://opinion.people.com.cn/"+i)
    wenzhang0 = wenzhang.read()
    wenzhanghtml = BeautifulSoup(wenzhang0, "html.parser")
    pattern_title = r'<h1>(.*?)</h1>'
    title0 = re.search(pattern_title, str(wenzhanghtml))
    title = str(title0.group(1)).replace(" ", "").replace("\n", "")
    pattern_content = r'>(.*?)</p>'
    content0 = re.findall(pattern_content, str(wenzhanghtml))
    content1 = title.join(content0).replace(" ", "").replace("\n", "")
    content2 = re.sub(r'<.*?>', '', content1)  
    content = re.sub(r'《人民日报》.*?京公网安备11000002000008号', '', content2)
    wenzhang.close()
    with open(title+".txt",'w',encoding="utf-8") as f:
        f.write(content)