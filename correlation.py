# Add the functions in this file
import json
def load_journal(file_name):
    jfile = open(file_name,)
    data = json.load(jfile)
    jfile.close()
    #print(data)
    return data


def compute_phi(file_name,event):
    data = load_journal(file_name)
    n11=0
    n00=0
    n10=0
    n01=0
    n1_=0
    n0_=0
    n_1=0
    n_0=0
    for i in data:
        if event in i['events']:
            if i['squirrel']:
                n11 += 1
            else : 
                n10 += 1
        else :
            if i['squirrel']:
                n01 += 1
            else:
                n00 += 1
    n1_ = n11 + n10
    n0_ = n01 + n00
    n_1 = n11 + n01
    n_0 = n10 + n00
    
    phi = (n11 * n00 - n10 * n01) / ((n1_ * n0_ * n_1 * n_0)**0.5)
    
    #print(phi)
    return phi

def compute_correlations(file_name):
    data = load_journal(file_name)
    d = {}
    for i in data:
        for j in i['events']:
            if j not in d:
                d[j]= compute_phi(file_name,j)
    
    #print(d)
    return d

def diagnose(file_name):
    d = compute_correlations(file_name)
    #print(max(d,key=d.get),min(d,key =d.get))
    return max(d,key=d.get),min(d,key =d.get)
    


