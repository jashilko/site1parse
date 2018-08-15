# import libraries
import requests
from bs4 import BeautifulSoup

class SearchPerson:
    Name = ''
    Location = ''
    Golg = False
    href = ''

spList = []
bd = requests.get('search/index.php?input_action=search&input_who1=2&input_who2=1&input_bdsm_position=1&input_age1=&input_age2=&input_country_id=3159&input_state_id=4312&input_city_id=0&input_online=on')
bds = BeautifulSoup(bd.text, "html.parser")
#print(bds)
#p3 = bds.select('.personal_user_name_vip0')
#p3 = bds.findAll("a", class_="search_user_name_vip1")
p3 = bds.findAll("span", {"class": "text_normal"})
#print(*p3)
for one in p3:
    sp = SearchPerson()
    sp.Name = one.p.a.text
    sp.Location = one.contents[3].text
    sp.href = one.p.a['href']
    spList.append(sp)
    