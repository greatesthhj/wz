import urllib.request
import re
from bs4 import BeautifulSoup
response = urllib.request.urlopen("http://opinion.people.com.cn/GB/8213/49160/49179/")
shouye0 = response.read()
shouyehtml = BeautifulSoup(shouye0, "html.parser")
pattern = r'<li><a href="(.*?)" target="_blank">'
lianjie = re.findall(pattern, str(shouyehtml))
for i in lianjie:
    wenzhang = urllib.request.urlopen("http://opinion.people.com.cn/"+i)
    wenzhang0 = wenzhang.read()
    wenzhanghtml = BeautifulSoup(wenzhang0, "html.parser")
    pattern_title = r'<title>(.*?)</title>'
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
        print(f"已保存文章：{title}.txt")