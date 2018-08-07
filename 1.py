# import libraries
import requests
from bs4 import BeautifulSoup



bd = requests.get('http://bdsmpeople.club/search/index.php?input_action=search&input_who1=2&input_who2=1&input_bdsm_position=1&input_age1=&input_age2=&input_country_id=3159&input_state_id=4312&input_city_id=0&input_online=on')
bds = BeautifulSoup(bd.text, "html.parser")
#print(bds)
#p3 = bds.select('.personal_user_name_vip0')
p3 = bds.findAll("a", class_="search_user_name_vip1")
p3 = bds.findAll("a", {"class": "search_user_name_vip1"})
print(*p3)
print(p3[0])