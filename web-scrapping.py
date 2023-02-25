

import requests
import pandas as pd
import time
list=['DHK121', 'SHK122', 'SHK123', 'SHK124', 'SHK125', 'SHK126',
       'SHK127', 'SHK128', 'SHK129', 'SHK130', 'SHK131', 'SHK132', 'SHK133',
       'SHK134', 'SHK135', 'SHK136', 'SHK137', 'SHK138', 'SHK140', 'SHK141',
       'SHK142', 'SHK143', 'SHK144', 'SHK145', 'SHK146', 'SHK147', 'SHK148',
       'SHK149', 'SHK150']

headers = {'Accept': 'application/json'}


def manulife_scrapping(name,begin=None,end=None):
    """
    name(Must, String): manulife MPF name, such as DHK121
    begin(Option, String): begin date of the data, format :"2011-05-25"
    end(Option, String):end date of the data, format : "2011-05-25"
    
    if you didn't specify the begin and ending date, it will return all the data from the website (recent history # 2956 )
    but sometime the fund data would not update, such as DHK121
    
    it will return as dataframe format
    """

    r = requests.get(f"https://www.manulife.com.hk/bin/funds/fundhistory?id={name}&productLine=mpf&overrideLocale=en_HK",headers=headers)
    resjson=r.json()
    len(resjson['priceHistory'])
    df=pd.DataFrame(resjson['priceHistory'])
    df['name']=name
    first_column = df.pop('name')
    df.insert(0, 'name', first_column)
    df['asOfDate']=pd.to_datetime(df['asOfDate'])

    if begin==None and end==None:
        df=df
    elif (begin !=None and end==None):
        df = df[(df['asOfDate'] >= begin)]
    elif (begin ==None, end!=None):
        df = df[(df['asOfDate'] <= begin)]
    else:
        df = df[(df['asOfDate'] >= begin) & (df['asOfDate'] <= end)]
    

    return df


def main():
    for i in list:
        time.sleep(2)
        a=manulife_scrapping(i)
        print(a)
main()