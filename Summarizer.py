from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from collections import defaultdict
from string import punctuation
from heapq import nlargest



class Summarizer:
    def __init__(self, min_sum=0.1, max_sum=0.9):
        self._min_sum = min_sum
        self._max_sum = max_sum
        self._stopwords = set(stopwords.words('english') + list(punctuation))



    def _find_common_words(self):
        pass

    def _compute_words(self, words_sen):
        freq = defaultdict(int)

        for sen in words_sen:
            for word in sen:
                if word not in self._stopwords:
                    freq[word] += 1
        m = float(max(freq.values()))
        for w in freq.copy().keys():
            freq[w] = freq[w] / m
            if freq[w] >= self._max_sum or freq[w] <= self._min_sum:
                del freq[w]
        return freq

    def _summarize(self, text, n):
        text = text.strip()
        sents = sent_tokenize(text)
        assert n <= len(sents)
        self.count_of_sens = len(sents)
        self.first_sen = sents[0]
       # print(len(sents))
       # print(sents)
        word_sent = [word_tokenize(s.lower()) for s in sents]
        #print(word_sent.most_common(15))
        self._freq = self._compute_words(word_sent)
        ranking = defaultdict(int)
        for i, sent in enumerate(word_sent):
            for w in sent:
                if w in self._freq:
                    ranking[i] += self._freq[w]
        sents_idx = self._rank(ranking, n)
        return [sents[j] for j in sents_idx]

    def _rank(self, ranking, n):
        r = nlargest(n, ranking, key=ranking.get)
        # print(r)
        return r
