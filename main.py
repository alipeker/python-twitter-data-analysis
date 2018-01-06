import os, inspect
from operator import itemgetter
import json
import string
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import collections
from matplotlib.dates import DateFormatter

f=open("tweet_data.json","r")
a=open("tweet_data.json","r")
b=a.readlines()
punctuation = list(string.punctuation)
stop=punctuation+[u'a',u'|',u".",u"-",u'an',u'the',u'rt', u'via',u'to',u'of',u'for',u'and',u'or',u'i',u'in',u'at',u'on',u'out',u'with',u'by',u'de',u' ',u'is',u'am',u'are',u'my',u'your',u'our',u'us',u'me',u'you',u'it',u'',u'the',u'no',u'have',u'has',u'we',u'her',u'his',u'them',u'when',u'who',u'where',u'which',u'how',u'that',u'not',u'this',u'&amp;',u'from',u'new',u'la',u'but',u"https://t.co/fezvw2bj9e"]
time=[]
denemelist=[]
mylist=[]
mylist2=[]
enddict={}
mydict={}
hour=[]

for d in range(len(b)-1):
    line =f.readline() # read only the first tweet/line
    tweet = json.loads(line) # load it as Python dict
    created_at_format = '%a %b %d %H:%M:%S +0000 %Y'
    str=tweet['text']#tweet
    str=str.lower()
    L=str.split(" ");
    mylist2.append(L)
    denemelist.append(L)
    date=tweet["created_at"];#date-time in ISO format
    dt=datetime.strptime(date, "%a %b %d %H:%M:%S +0000 %Y") #reading date in ISO format
    dt_without_sec = dt.replace(second=0,microsecond=0)
    hour.append(dt.hour+dt.minute)
    time.append(dt_without_sec )
    for word in L:
        if not word in stop:
            if word in enddict:
                enddict[word]+=1
            else:
                enddict[word]=1
a.close()
f.close()

key2=[]
value2=[]

sort=sorted(enddict.items(),key=itemgetter(1),reverse=True)

for a in range(20):
    key2.append(sort[a][0])
    value2.append(sort[a][1])

   
n_groups = 20
means_tweet = (value2)
std_tweet = (0)
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.4
error_config = {'ecolor': '0.3'}
rects1 = plt.bar(index, means_tweet, bar_width,
                 alpha=opacity,
                 color='b',
                 yerr=std_tweet,
                 error_kw=error_config,
                 label='Tweet')
plt.xlabel('Words')
plt.ylabel('Term Frequencies')
plt.title('Tweet Miner')
fig.autofmt_xdate(bottom=0.2, rotation=45, ha='right')
plt.xticks(index + bar_width, (key2))    
plt.savefig("term_frequencies.png")
plt.legend()
plt.tight_layout()
plt.show()





w=open("term_frequencies.txt","w")
for i in range(20):
    w.write(unicode(key2[i])+":"+unicode(value2[i])+"\n")
w.close()

for a in range(len(mylist2)):
    for aa in range(len(mylist2[a])):
        if mylist2[a][aa] in stop:
            mylist2[a][aa]="x"
for b in range(len(mylist2)):
    for bb in range(len(mylist2[b])):
        if "x" in mylist2[b]:
            mylist2[b].remove("x")

#figure2
first=[]
second=[]
third=[]
fourth=[]
fiveth=[]
time2=[]
endtime=[]
endkey=[]
for t in range(5):
    endkey.append(key2[t])
    
for a in time:
    endtime.append(a)

maxtime=[]   
for d in range(len(mylist2)):
    for dd in range(len(mylist2[d])):
        if mylist2[d][dd]==endkey[0]:
            first.append(unicode(mylist2[d][dd])+":"+unicode(endtime[d]))
        if mylist2[d][dd]==endkey[1]:
            second.append(unicode(mylist2[d][dd])+":"+unicode(endtime[d]))
        if mylist2[d][dd]==endkey[2]:
            third.append(unicode(mylist2[d][dd])+":"+unicode(endtime[d]))
        if mylist2[d][dd]==endkey[3]:
            fourth.append(unicode(mylist2[d][dd])+":"+unicode(endtime[d]))
        if mylist2[d][dd]==endkey[4]:
            fiveth.append(unicode(mylist2[d][dd])+":"+unicode(endtime[d]))
        if not endtime[d] in maxtime:
            maxtime.append(endtime[d])
timefirst=[]
timesecond=[]
timethird=[]
timefourth=[]
timefiveth=[]

timefirst=sorted(collections.Counter(first).items(),key=itemgetter(0),reverse=False)
timesecond=sorted(collections.Counter(second).items(),key=itemgetter(0),reverse=False)
timethird=sorted(collections.Counter(third).items(),key=itemgetter(0),reverse=False)
timefourth=sorted(collections.Counter(fourth).items(),key=itemgetter(0),reverse=False)
timefiveth=sorted(collections.Counter(fiveth).items(),key=itemgetter(0),reverse=False)



wri=open("term_frequencies_overtime.txt","w")
for i in range(len(timefirst)):
    wri.write(unicode(timefirst[i][0])+" "+unicode(timefirst[i][1])+"\n")
for i in range(len(timesecond)):
    wri.write(unicode(timesecond[i][0])+" "+unicode(timesecond[i][1])+"\n")
for i in range(len(timethird)):
    wri.write(unicode(timethird[i][0])+" "+unicode(timethird[i][1])+"\n")
for i in range(len(timefourth)):
    wri.write(unicode(timefourth[i][0])+" "+unicode(timefourth[i][1])+"\n")
for i in range(len(timefiveth)):
    wri.write(unicode(timefiveth[i][0])+" "+unicode(timefiveth[i][1])+"\n")
wri.close()
a2=[]
xmax=[]


firstmax=[]
secondmax=[]
thirdmax=[]
fourthmax=[]
fivethmax=[]


for b in range(len(timefirst)):
    firstmax.append(timefirst[b][1])
        

for b in range(len(timesecond)):
    secondmax.append(timesecond[b][1])


for b in range(len(timethird)):
    thirdmax.append(timethird[b][1])
        

for b in range(len(timesecond)):
    fourthmax.append(timefourth[b][1])
        

for b in range(len(timesecond)):
    fivethmax.append(timefiveth[b][1])

fig=plt.figure() 
plt.xlabel('Time')
plt.ylabel('Frequenct of occurrence'+"\n")
plt.plot(maxtime,firstmax,label=endkey[0],linewidth=1)
plt.plot(maxtime,secondmax,label=endkey[1],linewidth=1)
plt.plot(maxtime,thirdmax,label=endkey[2],linewidth=1)
plt.plot(maxtime,fourthmax,label=endkey[3],linewidth=1)
plt.plot(maxtime,fivethmax,label=endkey[4],linewidth=1)
formatter = DateFormatter('%H:%M')
plt.gcf().axes[0].xaxis.set_major_formatter(formatter)
fig.autofmt_xdate(bottom=0.2, rotation=0, ha='right')
plt.legend()
plt.legend(loc=1,prop={'size':12})
plt.savefig("term_frequencies_overtime.png")
plt.show() 


#figure3
newlist=[]
testlist=[]
tlist=[]



t2list=[]
t3list=[]
for b in range(len(mylist2)):
    tlist.append(sorted(mylist2[b], reverse=True)) 
for d in tlist:
    t2list.append(collections.Counter(d))

for k in t2list:
    t3list.append(k.keys()) 


for d in range(len(t3list)):
    for a in range(len(t3list[d])-1):
        x=t3list[d][a]
        for b in range(a,len(t3list[d])-1):
            newlist.append(unicode(x)+"-"+unicode(t3list[d][b+1]))

sorted_dict=sorted(collections.Counter(newlist).items(),key=itemgetter(1),reverse=True)



dict1={}
ret=[]
ret2=[]
kay=[]
for d in range(11):
    x=key2[d]
    for b in range(d,11):
            ret.append(unicode(x)+"-"+unicode(key2[b]))  
             

for p in range(len(sorted_dict)):
    dict1[sorted_dict[p][0]]=sorted_dict[p][1]
rekey=[]
result=[]
result2=[]
end=[]
for i in range(len(ret)):
    if ret[i] in dict1.keys():
        result.append(dict1[ret[i]])
        rekey.append(ret[i])
    

for a in range(len(result)):
    end.append(unicode(rekey[a])+":"+unicode(result[a]))  

writ=open("term_cooccurrences.txt","w")
for i in end:
    writ.write(i+"\n")
writ.close()

#son
