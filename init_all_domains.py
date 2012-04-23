"""
RUN THIS SCRIPT ONCE TO INITIALIZE ALL DOMAINS IN AWS.

"""

import boto
import feedparser
import yql
import time
from datetime import date
conn = boto.connect_sdb('AKIAJQGNH4CPXPMONQMQ','vcvskvwMNjujVUtP73OssCJmYXs9eUuNOGiGJn4V')
conn.create_domain('keywords')
conn.create_domain('news')
conn.create_domain('users')
conn.create_domain('likes')
dom_key=conn.get_domain('keywords')
dom_news=conn.get_domain('news')
dom_user=conn.get_domain('users')
dom_like=conn.get_domain('likes')

