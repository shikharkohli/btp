import allimports
import urls

def insertfeeds():    
    y=allimports.yql.Public()
    TS=allimports.time.time()
    for i in range(0,1):
        for site in urls.url[i]:
            feed=allimports.feedparser.parse(site)
            news_category=urls.cat[i]
            for item in feed.entries:
                news_name=item.id
                news_title=item.title[:1000]
                news_summary=item.summary[:1000]
                str=news_summary.encode("ascii", "ignore")
                news_links=item.links
                news_TS=TS
                news_importance=1
                keys=[]               
                q='select * from search.termextract where context = @str'
                res=y.execute(q,{"str":str})
                for key in res.rows:
                    key_name=key
                    keys.append(key)
                    key_rank=1
                    key_attr={ news_name : [key_rank, news_category, news_TS]}
                    flag=allimports.dom_key.put_attributes(key_name,key_attr,False)
                    while(flag==False):
                        print "looping...\n"
                news_attr={'keys': keys, 'TS' : news_TS, 'category': news_category, 'link' : news_links, 'summary': news_summary, 'title':news_title, 'importance':news_importance}
                flag=allimports.dom_news.put_attributes(news_name,news_attr)
                while(flag==False):
                    print "looping..\n"
                print "news id:"
                print news_name
                print "keys:",
                print keys,
                print "category: " + news_category,
                print  "]..inserted\n",
          
insertfeeds();        
print "process slept"
#allimports.time.sleep(36000)
    
