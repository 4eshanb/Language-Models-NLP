import re, nltk, argparse
from nltk.util import ngrams
import os

def get_score(review):
    return int(re.search(r'Overall = ([1-5])', review).group(1))

def get_text(review):
    return re.search(r'Text = "(.*)"', review).group(1)

def read_reviews(file_name):
    """
    Dont change this function.

    :param file_name:
    :return:
    """
    file = open(file_name, "rb")
    raw_data = file.read().decode("latin1")
    file.close()

    positive_texts = []
    negative_texts = []
    first_sent = None
    for review in re.split(r'\.\n', raw_data):
        overall_score = get_score(review)
        review_text = get_text(review)
        if overall_score > 3:
            positive_texts.append(review_text)
        elif overall_score < 3:
            negative_texts.append(review_text)
        if first_sent == None:
            sent = nltk.sent_tokenize(review_text)
            if (len(sent) > 0):
                first_sent = sent[0]
    return positive_texts, negative_texts, first_sent


########################################################################
## Dont change the code above here
######################################################################



def process_reviews(file_name):
    positive_texts, negative_texts, first_sent = read_reviews(file_name)

    # There are 150 positive reviews and 150 negative reviews.
    # print(len(positive_texts))
    # print(len(negative_texts))

    # Your code goes here

    ### TOKENIZE THE WORDS
    tokens_pos_texts = []
    for review in positive_texts:
        tokens_pos_texts.append(nltk.word_tokenize(review))

    tokens_neg_texts = []
    for review in negative_texts:
        tokens_neg_texts.append(nltk.word_tokenize(review))
   
    ### LOWER THE WORDS
    lower_neg_texts = [word.lower() for sent in tokens_neg_texts for word in sent]
    lower_pos_texts = [word.lower() for sent in tokens_pos_texts for word in sent]

    ### REMOVE THE STOP WORDS
    stop_words = nltk.corpus.stopwords.words('english')
    tokens_no_sw_pos = [word for word in lower_pos_texts if word not in stop_words]
    tokens_no_sw_neg =[word for word in lower_neg_texts if word not in stop_words]

    ### REMOVE THE WORDS WITH LESS THAN 1 WC
    #print(re.findall(r'[\w]', ".b.ubba9"))
    #print(re.findall(r'[\w]', "....;;"))
    tokens_final_pos = [word for word in tokens_no_sw_pos if re.findall(r'[\w]+', word) != []]
    tokens_final_neg = [word for word in tokens_no_sw_neg if re.findall(r'[\w]', word) != []]
    print(len(tokens_final_pos))
    print(len(tokens_final_neg))
    
    ### CREATE UNIGRAM FREQDIST
    create_unigram_freqdist(tokens_final_pos,'positive')
    create_unigram_freqdist(tokens_final_neg,'negative')

    ### CREATE BIGRAM CFD
    create_bigram_cfd(tokens_final_pos, 'positive')
    create_bigram_cfd(tokens_final_neg, 'negative')

    ### COLLOCATIONS
    text_neg = nltk.Text(tokens_final_neg)
    print("Collocations in negative reviews: ")
    print()
    print(text_neg.collocation_list())
    print()

    text_pos = nltk.Text(tokens_final_pos)
    print("Collocations in positive reviews: ")
    print()
    print(text_pos.collocation_list())
    print()

    ### 3.3 Questions
    #part3_3(tokens_final_pos, tokens_final_neg)
    
def calculate_five_ngrams(tokens, ngrams_count, category):
    n_grams = ngrams(tokens, ngrams_count)
    fdist_ngrams = nltk.FreqDist(n_grams)
    print("5 most frequent "+ str(ngrams_count)+ "-grams " + "in "+ category+ " text: \n")
    print(fdist_ngrams.most_common(5))
    print()

def part3_3(tokens_pos, tokens_neg):
    calculate_five_ngrams(tokens_pos, 1, 'positive')
    calculate_five_ngrams(tokens_neg, 1, 'negative')
    calculate_five_ngrams(tokens_pos, 2, 'positive')
    calculate_five_ngrams(tokens_neg, 2, 'negative')
    calculate_five_ngrams(tokens_pos, 3, 'positive')
    calculate_five_ngrams(tokens_neg, 3, 'negative')
    calculate_five_ngrams(tokens_pos, 4, 'positive')
    calculate_five_ngrams(tokens_neg, 4, 'negative')
    calculate_five_ngrams(tokens_pos, 5, 'positive')
    calculate_five_ngrams(tokens_neg, 5, 'negative')

def create_unigram_freqdist(tokens, category):
    unigrams = ngrams(tokens, 1)
    fdist_ugrams = nltk.FreqDist(unigrams)
    #print(fdist_ugrams.most_common(10))
    most_common_ugrams =  fdist_ugrams.most_common()
    mc_format = '\n'.join([str(tup[0][0]) + "\t" + str(tup[1]) for tup in most_common_ugrams])
    write_file(category + '-unigram-freq.txt', str(mc_format))

def create_bigram_cfd(tokens, category):
    bigrams_t = nltk.bigrams(tokens)
    bigrams_cfdist = nltk.ConditionalFreqDist(bigrams_t)
    bigram_dict = {}
    keys_bigrams = [(condition,word) for condition in bigrams_cfdist.conditions() for word in bigrams_cfdist[condition]]
    for key in keys_bigrams: 
        bigram_dict[key] = bigrams_cfdist[key[0]][key[1]]

    sorted_bigrams_alpha = sorted(bigram_dict.items(), key = lambda x:x[0])
    sorted_bigrams_num = sorted(sorted_bigrams_alpha, key = lambda x:x[1], reverse = True)
    bgc_format = '\n'.join([ str(tup[0][0]) + "\t" + str(tup[0][1]) + "\t" + str(tup[1]) for tup in sorted_bigrams_num])
    write_file(category + "-bigram-freq.txt", str(bgc_format))

# Write to File, this function is just for reference, because the encoding matters.
def write_file(file_name, data):
    file = open(file_name, 'w', encoding="utf-8")    # or you can say encoding="latin1"
    file.write(data)
    file.close()


def write_unigram_freq(category, unigrams):
    """
    A function to write the unigrams and their frequencies to file.

    :param category: [string]
    :param unigrams: list of (word, frequency) tuples
    :return:
    """
    uni_file = open("{0}-unigram-freq-n.txt".format(category), 'w', encoding="utf-8")
    for word, count in unigrams:
        uni_file.write("{0:<20s}{1:<d}\n".format(word, count))
    uni_file.close()


if __name__ == '__main__':
    if os.path.exists("test.txt"):  
        word_net_file = open("test.txt","w")
        word_net_file.write("")
        word_net_file.close()
    parser = argparse.ArgumentParser(description='Assignment 2')
    parser.add_argument('-f', dest="fname", default="restaurant-training.data",  help='File name.')
    args = parser.parse_args()
    fname = args.fname

    process_reviews(fname)
