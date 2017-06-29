import nltk
from nltk.corpus import stopwords
stopwords = stopwords.words('english')

lemmatizer = nltk.WordNetLemmatizer()
stemmer = nltk.stem.porter.PorterStemmer()


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

sentence_re = r'''(?x)      # set flag to allow verbose regexps
      ([A-Z])(\.[A-Z])+\.?  # abbreviations, e.g. U.S.A.
    | \w+(-\w+)*            # words with optional internal hyphens
    | \$?\d+(\.\d+)?%?      # currency and percentages, e.g. $12.40, 82%
    | \.\.\.                # ellipsis
    | [][.,;"'?():-_`]      # these are separate tokens
'''


grammar = "NP: {<DT>?<JJ>*<NN>}"
chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""

def normilized(word):
    """Normalises words to lowercase and stems and lemmatizes it."""
    word = word.lower()
    word = stemmer.stem(word)
    word = lemmatizer.lemmatize(word)
    return word


def acceptable_word(word):
    """Checks conditions for acceptable word: length, stopword."""
    accepted = bool(2 <= len(word) <= 40
        and word.lower() not in stopwords)
    return accepted




def leaves(tree):
    #Finds NP (nounphrase) leaf nodes of a chunk tree.
    for subtree in tree.subtrees(filter = lambda t: t.label() == 'NP'):
        yield subtree.leaves()


def make_chunk(text):
    tokens = nltk.tokenize.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    cp = nltk.RegexpParser(chunkGram)
    chunk_parser = nltk.RegexpParser(chunkGram)
    chunged = chunk_parser.parse(pos)

    return chunged
    #print(chunged)
    # chunged.draw()



def get_terms(tree):
    chk = make_chunk(tree)
    #print(chk)
    for leaf in leaves(chk):
        term = [normilized(w) for w, t in leaf if acceptable_word(w)]

    yield term
    #return term




text = """The Buddha, the Godhead, resides quite as comfortably in the circuits of a digital
computer or the gears of a cycle transmission as he does at the top of a mountain
or in the petals of a flower. To think otherwise is to demean the Buddha...which is
to demean oneself."""









"""
def leaves(tree):
    #Finds NP (nounphrase) leaf nodes of a chunk tree.
    for subtree in tree.subtrees(filter = lambda t: t.label()=='NP'):
        yield subtree.leaves()

def normalise(word):
    #Normalises words to lowercase and stems and lemmatizes it.
    word = word.lower()
    word = stemmer.stem_word(word)
    word = lemmatizer.lemmatize(word)
    return word

def acceptable_word(word):
    #Checks conditions for acceptable word: length, stopword.
    accepted = bool(2 <= len(word) <= 40
        and word.lower() not in stopwords)
    return accepted


def get_terms(tree):
    for leaf in leaves(tree):
        term = [normalise(w) for w, t in leaf if acceptable_word(w) ]
        yield term

"""
terms = get_terms(text)
for t in terms:
    for word in t:
        print(word)


print(t)
print("")
#text = make_chunk(text)
#print(text)
##print(acceptable_word("if"))
