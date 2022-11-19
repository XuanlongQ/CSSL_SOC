# python3
import jsonlines
import sys
import matplotlib.pyplot as plt
from datetime import datetime
import time

filePath = 'post_process/output.jsonl'


def get_graph(date_dic):
    print(date_dic)
    neg = []
    neu = []
    pos = []
    datestrs = []
    for k,v in date_dic.items():
        
        datestrs.append(k)
        neg.append(v["负面"])
        neu.append(v["正面"])
        # pos.append(v["中性"])

    print(datestrs)
    x = [datetime.strptime(i,'%Y-%m-%d') for i in datestrs]
   
    plt.plot(x, neg)
    plt.show()
    

def get_date_sentiment(item):
    try:
        sentiment = item['addition']['sentiment']
        # print(type(sentiment))
        created_at = item['created_at'].split(' ')[0]

        if isinstance(sentiment,str):
            s = eval(sentiment)
            return created_at,s
        else:
            if not sentiment:
                print("sentiment is {}".format(sentiment),type(sentiment))
            else:
                return None,None
    except KeyError:
        #print("no such attributes")
        return None,None    
    
if __name__ == "__main__":
    with open(filePath,'r+',encoding='utf-8') as file:
        date_dic = {}
     
        for item in jsonlines.Reader(file):
            #print(item)
            date,sentiment = get_date_sentiment(item)
            print(date,sentiment)
            if date in date_dic.keys():
                if str(sentiment) in date_dic[date].keys():
                    if str(sentiment) == '负面':
                        date_dic[date]['负面'] += 1
                    if str(sentiment) == '中性':
                        date_dic[date]['中性'] += 1
                    if str(sentiment) == '正面':
                        date_dic[date]['正面'] += 1
                else:
                    if str(sentiment) == '负面':
                        date_dic[date]['负面'] = 1
                    if str(sentiment) == '中性':
                        date_dic[date]['中性'] = 1
                    if str(sentiment) == '正面':
                        date_dic[date]['正面'] = 1
            else:
                date_dic[date] = {}
                if str(sentiment) == '负面':
                    date_dic[date]['负面'] = 1
                if str(sentiment) == '中性':
                    date_dic[date]['中性'] = 1
                if str(sentiment) == '正面':
                        date_dic[date]['正面'] = 1
                    
                
        print(date_dic)           
        get_graph(date_dic)
        
        
