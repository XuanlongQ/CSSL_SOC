
import sys
import jsonlines

with open('post_process/predict_label_list.txt','r',encoding='utf-8') as f:
    a= f.read()
    new_list_relative = a.replace("["," ").replace("]", " ").split(",")
    #print(new_list_relative,len(new_list_relative))
    print(new_list_relative)
    
with open('post_process/predict_label_list_original.txt','r',encoding='utf-8') as f:
    b= f.read()
    new_list_sentiment = b.replace("["," ").replace("]", " ").split(",")
    #print(new_list_sentiment,len(new_list_sentiment))
    


with open('post_process/new_hongk.jl','r', encoding= 'utf-8') as f:
    c = 0
    dic = {}
    for item in jsonlines.Reader(f):
        print(type(item))
        addition = {}
        print(new_list_relative[c],new_list_sentiment[c])
        addition['relarive'] = new_list_relative[c]
        addition['sentiment'] = new_list_sentiment[c]
        item['addition'] = addition
        c += 1
        
        print(item)
        with jsonlines.open('output.jsonl',mode='a') as writer:
            writer.write(item)