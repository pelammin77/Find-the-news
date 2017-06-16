"""
file: file_ent.py
author: Petri Lamminaho 
"""
import nltk


"""
# You can use these tags  
###########################################
ORGANIZATION 	Georgia-Pacific Corp., WHO
PERSON 	        Eddy Bonte, President Obama
LOCATION 	    Murray River, Mount Everest
DATE 	        June, 2008-06-29
TIME 	        two fifty a m, 1:30 p.m.
MONEY 	        175 million Canadian Dollars, GBP 10.40
PERCENT 	    twenty pct, 18.75 %
FACILITY 	    Washington Monument, Stonehenge
GPE 	       South East Asia, Midlothian
############################################
"""


def find_ent(text, tag='PERSON'):
    tokens = nltk.tokenize.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    sentt = nltk.ne_chunk(pos, binary=False)
    #print(sentt)
    array = []
    for subtree in sentt.subtrees(filter = lambda t: t.label() == tag):
        array.append(" ".join([a for (a, b) in subtree.leaves()]))
    return array
