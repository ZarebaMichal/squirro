import heapq

import nltk

stopwords = nltk.corpus.stopwords.words("english")


def make_summary(text: str) -> str:
    """Create summary in 7 sentences from given text"""
    word_frequencies = {}
    sentence_list = nltk.sent_tokenize(text)
    words = nltk.word_tokenize(text)

    for word in words:
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

    maximum_frequency = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word] / maximum_frequency

    sentence_scores = {}
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]

    summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
    summary = " ".join(summary_sentences)

    return summary
