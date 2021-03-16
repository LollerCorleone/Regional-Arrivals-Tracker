# -*- coding: utf-8 -*-
"""
Regional Arrivals Tracker, originally built for usage in Caer Sidi.

@author: Loller Corleone (https://www.nationstates.net/nation=lollerland)


"""

import json
import re
import nationstates
from nationstates import Shard

file = open("arrivals.txt","r+")
file.truncate(0)
file.close()

log = open("arrivals.txt", 'a')
def oprint(message):
    print(message)
    global log
    log.write(message)
    return()
useragent = input("Enter a descriptive user agent: ")
nsr = input("Enter your region's name: ")
nsr1 = re.sub(r"\s+", '-', nsr)
api = nationstates.Nationstates(useragent)
resp = api.world().get_shards(Shard("happenings", view="region."+nsr, filter='move'))
data = json.dumps(resp.happenings)
datadict = json.loads(data)
b = []
for key in datadict['event']:
    filtertxt = 'to %%caer_sidi%%'
    a = key['text']
    if filtertxt in a:
        b.append(a)
d=[]
e=[]
for c in b:
    d = re.split(r'\s',c)
    e.append(d[0])
for nation in e:
    line = re.sub('@@', '', nation)
    oprint("[nation]"+line+"[/nation]"+" ")
    
log.close()