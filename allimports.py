import boto
import feedparser
import yql
import time
from datetime import date

conn = boto.connect_sdb('AKIAJQGNH4CPXPMONQMQ','vcvskvwMNjujVUtP73OssCJmYXs9eUuNOGiGJn4V')
conn.create_domain('users')

dom_user=conn.get_domain('users')
dom_news=conn.get_domain('faltu_news')
dom_key=conn.get_domain('keywords2')
dom_likes=conn.get_domain('likes')

def imports():
    import boto
    import feedparser
    import yql
    import time
    from datetime import date

    conn = boto.connect_sdb('AKIAJQGNH4CPXPMONQMQ','vcvskvwMNjujVUtP73OssCJmYXs9eUuNOGiGJn4V')
    conn.create_domain('users')

    dom_user=conn.get_domain('users')
    dom_news=conn.get_domain('faltu_news')
    dom_key=conn.get_domain('keywords2')
    dom_likes=conn.get_domain('likes')

