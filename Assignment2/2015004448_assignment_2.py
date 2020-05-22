from konlpy.tag import Okt
import math
okt = Okt()

f = open('ratings_train.txt','r')
txt = f.readlines()

pos_m=0
neg_m=0
pos_num=0
pos_word = {}
neg_num=0
neg_word = {}
for i in txt:
    inp =  i[:-1].split('\t')
    word = okt.pos(inp[1])

    if inp[2] == '1':
        pos_m+=1
        for w in word:
            if w[1] == 'Josa':
                continue
            if w[0] in pos_word:
                pos_word[w[0]] += 1
            else:
                pos_word[w[0]] = 1
            pos_num+=1
            
    elif inp[2] == '0':
        neg_m+=1
        for w in word:
            if w[1] == 'Josa':
                continue
            if w[0] in neg_word:
                neg_word[w[0]] += 1
            else: 
                neg_word[w[0]] = 1
            neg_num+=1
            
f.close()
            
fi = open('ratings_test.txt','r')
fo = open('ratings_result.txt','w')
txt = fi.readlines()

word_list  = list(set(pos_word) | set(neg_word))
l = len(word_list)

for i in txt:
    inp = i[:-1].split('\t')
    if inp[0] == 'id' and inp[1] == 'document' and inp[2] == 'label':
        fo.write(i)
        continue

    word = okt.pos(inp[1])

    pos_P = math.log(float(pos_m)/(pos_m+neg_m))
    neg_P = math.log(float(neg_m)/(pos_m+neg_m))
            
    for w in word:
        if w[1] == 'Josa':
            continue
        if w[0] in pos_word:
            pos_P += math.log(float(pos_word[w[0]]+1)/(pos_num+l))
        else:
            pos_P += math.log(1/(pos_num+l))
        if w[0] in neg_word:
            neg_P += math.log(float(neg_word[w[0]]+1)/(neg_num+l))
        else:
            neg_P += math.log(1/(neg_num+l))

    i = i[:-1]
    fo.write(i)
    if pos_P > neg_P:
        fo.write('1')
    else:
        fo.write('0')
    fo.write('\n')
        
fi.close()
fo.close()

'''
fi = open('ratings_valid.txt','r')
txt = fi.readlines()
cnt=0
cnt1=0
for i in txt:
    inp = i[:-1].split('\t')
    if inp[0] == 'id' and inp[1] == 'document' and inp[2] == 'label':
        continue
    cnt+=1
    
    word = okt.pos(inp[1])

    pos_P = math.log(float(pos_m)/(pos_m+neg_m))
    neg_P = math.log(float(neg_m)/(pos_m+neg_m))
            
    for w in word:
        if w[1] == 'Josa':
            continue
        if w[0] in pos_word:
            pos_P += math.log(float(pos_word[w[0]]+1)/(pos_num+l))
        else:
            pos_P += math.log(1/(pos_num+l))
        if w[0] in neg_word:
            neg_P += math.log(float(neg_word[w[0]]+1)/(neg_num+l))
        else:
            neg_P += math.log(1/(neg_num+l))

    if pos_P > neg_P:
        if inp[2] == '1':
            cnt1+=1
    elif inp[2] == '0':
        cnt1+=1

print(float(cnt1)/cnt*100, "%\n")     
fi.close()
'''
