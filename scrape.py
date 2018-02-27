import pandas as pd
import json
import requests
from bs4 import BeautifulSoup


# scrap website and add it to pandas dataframe
res = requests.get("https://www.fangraphs.com/leaders.aspx?pos=all&stats=bat&lg=all&qual=y&type=8&season=2017&month=0&season1=2017&ind=0&team=0&rost=0&age=0&filter=&players=0&page=1_50")
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table', id="LeaderBoard1_dg1_ctl00")
df = pd.read_html(str(table))
df = df[0]

df.columns = ['#', 'Name', 'Team','G', 'PA','HR','R','RBI','SB','BB%','K%','ISO','BABIP','AVG','OBP','SLG','wOBA','wRC+','BsR','Off','Def','WAR']

df.drop(df.tail(1).index,inplace=True) #remove blank entry at end
print(df)

# print(df)
#write to file
# fh = open("stats.json", "w")
# fh.writelines(df[0].to_json(orient='values'))
# fh.close()
