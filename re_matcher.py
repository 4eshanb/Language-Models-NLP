import argparse, re, nltk

# https://docs.python.org/3/howto/regex.html
# https://docs.python.org/3/library/re.html
# https://www.debuggex.com/


def get_words(pos_sent):
    """
    Given a part-of-speech tagged sentence, return a sentence
    including each token separated by whitespace.

    As an interim step you need to fill word_list with the
    words of the sentence.

    :param pos_sent: [string] The POS tagged stentence
    :return:
    """
    word_list = []
    # add the words of the sentence to this list in sequential order.
    # Your code goes here

    # Write a regular expression that matches only the
    # words of each word/pos-tag in the sentence.

    
    #pattern_words = re.compile(r'\w+[^/\s.(){};\'\?\!$*\"A-Z]')
    pattern_words = re.compile(r'(\w+)\/(\w+)')
    #matches_words = pattern_words.findall(pos_sent)
    #matches_words = pattern_words.group(1)
    matches_words = pattern_words.finditer(pos_sent)
    word_list = [match.group(1) for match in matches_words]
    #print(word_list)

    # END OF YOUR CODE
    retval = " ".join(word_list) if len(word_list) > 0 else None
    return retval


def get_pos_tags(pos_sent):
    # Your code goes here

    tags_list = []
    #pattern_tags = re.compile(r'[^a-z+][^/][A-Z]+[^\s]')
    #pattern_tags = re.compile(r'[^\/\s][A-Z]+')
    pattern_tags = re.compile(r"(\w+)\/([A-Z$]+)")
    #matches_tags = pattern_tags.findall(pos_sent)
    matches_tags = pattern_tags.finditer(pos_sent)
    tags_list = [tag.group(2) for tag in matches_tags]
    #print(tags_list)

    return tags_list
    pass


def get_noun_phrases(pos_sent):
    """
    Find all simple noun phrases in pos_sent.

    A simple noun phrase is a single optional determiner followed by zero
    or more adjectives ending in one or more nouns.

    This function should return a list of noun phrases without tags.

    :param pos_sent: [string]
    :return: noun_phrases: [list]
    """
    noun_phrases = []

    # Your code goes here
    #pattern_noun_phrases = re.compile(r'([a-zA-Z]+/DT[\s]+)*([a-zA-Z]+/JJ[\s]+)*([a-zA-Z]+/NNS)')
    #pattern_noun_phrases = re.compile(r'([a-zA-Z]+/DT[\s])*([a-zA-Z]+/JJ[\s])*([a-zA-Z]+/NNS)')
    #pattern_noun_phrases = re.compile(r"((\S+\/DT )?(\S+\/JJ )*(\S+\/NNS)+)")
 #   pattern_noun_phrases = re.compile(r"((\w+\/DT )?(\w+\/JJ )*(\w+\/NNS)+)")

    #pattern_noun_phrases = re.compile(r"((\w+\/DT )?(\w+\/JJ )*(\w+\/NNS)+)")
    #pattern_noun_phrases = re.compile(r"(?:(?:\w+\/DT )?(?:\w+\/JJ )*)?\w+(?:\/NNS|\/NN|\/NNP|\/NNPS)")
    #pattern_noun_phrases = re.compile(r"(?:(?:\w+\/DT )?(?:\w+\/JJ )*)?\w+ (?:N[NP]|PRN)")
    pattern_noun_phrases = re.compile(r"(?:\S+\/DT )?(?:\S+\/JJ )*(?:\S+(?:\/NNPS |NNP |NNS |NN ))*(?:\S+\/(?:NNPS|NNP|NNS|NN))")
    
    #pattern_noun_phrases = re.compile(r"(?:(?:\w+\/DT )?(?:\w+\/JJ )*)(\w+(\/NN|\/NNS|\/NNP|\/NNPS)+)?(?=(( \w+(\/NNPS|\/NNP|\/NNS|\/NN))+))( \w+(\/NNPS|\/NNP|\/NNS|\/NN))+|$")
    #pattern_noun_phrases = re.compile(r"(?:(?:\w+\/DT )?(?:\w+\/JJ )*)(\w+(\/NN|\/NNS|\/NNP|\/NNPS))+(?=(( \w+(\/NNPS|\/NNP|\/NNS|\/NN))+)|$|\s)")

    #pattern_noun_phrases = re.compile(r'(?:(?:\w+\/DT )?(?:\w+\/JJ )*)(\w+(\/NN|\/NNS|\/NNP|\/NNPS))+(?=(( \w+(\/NNPS|\/NNP|\/NNS|\/NN))+)|$|\s)')
    matches_noun_phrases = pattern_noun_phrases.findall(pos_sent)
    #matches_noun_phrases = re.findall(r"(?:(?:\w+\/DT )?(?:\w+\/JJ )*)(\w+(\/NN|\/NNS|\/NNP|\/NNPS))+(?=(( \w+(\/NN|\/NNS|\/NNP|\/NNPS))+)|$|\s)", pos_sent)
    #matches_noun_phrases = pattern_noun_phrases.sub(r'\4',pos_sent)
    #re.search(matches_noun_phrases, pos_sent)
    
    #print(matches_noun_phrases)
    noun_phrases = [get_words(match) for match in matches_noun_phrases]
 
    # END OF YOUR CODE

    return noun_phrases


def read_stories(fname):
    stories = []
    with open(fname, 'r') as pos_file:
        story = []
        for line in pos_file:
            if line.strip():
                story.append(line)
            else:
                stories.append("".join(story))
                story = []
    return stories



def most_freq_noun_phrase(pos_sent_fname, verbose=True):
    """

    :param pos_sent_fname:
    :return:
    """
    story_phrases = {}
    story_id = 1
    for story in read_stories(pos_sent_fname):
        most_common = []
        # your code starts here
        np_list = get_noun_phrases(story)
        #print(np_list)
        #print(story)
        np_list_lower = [np.lower() for np in np_list if np != None]
        #print(np_list_lower)
       
        np_lower_dict = {}
        
        for np in np_list_lower:
            if np in np_lower_dict:
                np_lower_dict[np] += 1
            else:
                np_lower_dict[np] = 1
        
        #print(np_lower_dict)
        #np_tuples = list(np_lower_dict.items())

        #print(np_sorted_tuples)
        #np_vals = list(np_lower_dict.values())
        #np_vals.sort(reverse = True)
        #print(vals)

        np_sorted_tuples = sorted(np_lower_dict.items(), key=lambda x:x[1], reverse = True)
        most_common = [val for val in np_sorted_tuples[:3]]
        # do stuff with the story

        # end your code
        if verbose:
            print("The most freq NP in document[" + str(story_id) + "]: " + str(most_common))
        story_phrases[story_id] = most_common
        story_id += 1

    return story_phrases

def most_freq_pos_tags(pos_sent_fname, verbose=True):
    """

    :param pos_sent_fname:
    :return:
    """
    story_tags = {}
    story_id = 1
    for story in read_stories(pos_sent_fname):
        most_common = []
        # your code starts here
        
        # do stuff with the story
        pos_list = get_pos_tags(story)
        #print(pos_list)
        pos_dict = {}
        for pos in pos_list:
            if pos in pos_dict:
                pos_dict[pos] += 1
            else:
                pos_dict[pos] = 1
        pos_sorted_tups = sorted(pos_dict.items(), key = lambda x:x[1], reverse = True)
        
        #print(pos_sorted_tups)
        most_common = [tup for tup in pos_sorted_tups[:3]]
        #print(pos_dict)
        # end your code
        if verbose:
            print("The most freq pos tags in document[" + str(story_id) + "]: " + str(most_common))
        story_tags[story_id] = most_common
        story_id += 1

    return story_tags



def test_get_words():
    """
    Tests get_words().
    Do not modify this function.
    :return:
    """
    print("\nTesting get_words() ...")
    pos_sent = 'All/DT animals/NNS are/VBP equal/JJ ,/, but/CC some/DT ' \
               'animals/NNS are/VBP more/RBR equal/JJ than/IN others/NNS ./.'
    print(pos_sent)
    retval = str(get_words(pos_sent))
    print("retval:", retval)

    gold = "All animals are equal but some animals are more equal than others"
    assert retval == gold, "test Fail:\n {} != {}".format(retval, gold)

    print("Pass")


def test_get_pos_tags():
    """
    Tests get_pos_tags().
    Do not modify this function.
    :return:
    """
    print("\nTesting get_pos_tags() ...")
    pos_sent = 'All/DT animals/NNS are/VBP equal/JJ ,/, but/CC some/DT ' \
               'animals/NNS are/VBP more/RBR equal/JJ than/IN others/NNS ./.'
    print(pos_sent)
    retval = str(get_pos_tags(pos_sent))
    print("retval:", retval)

    gold = str(['DT', 'NNS', 'VBP', 'JJ', 'CC', 'DT', 'NNS', 'VBP', 'RBR', 'JJ', 'IN', 'NNS'])
    assert retval == gold, "test Fail:\n {} != {}".format(retval, gold)

    print("Pass")



def test_get_noun_phrases():
    """
    Tests get_noun_phrases().
    Do not modify this function.
    :return:
    """
    print("\nTesting get_noun_phrases() ...")

    pos_sent = 'All/DT animals/NNS are/VBP equal/JJ ,/, but/CC some/DT ' \
               'animals/NNS are/VBP more/RBR equal/JJ than/IN others/NNS ./.'
    print("input:", pos_sent)
    retval = str(get_noun_phrases(pos_sent))
    print("retval:", retval)

    gold = "['All animals', 'some animals', 'others']"
    assert retval == gold, "test Fail:\n {} != {}".format(retval, gold)

    print("Pass")


def test_most_freq_noun_phrase(infile="fables-pos.txt"):
    """
    Tests get_noun_phrases().
    Do not modify this function.
    :return:
    """
    print("\nTesting most_freq_noun_phrase() ...")

    import os
    if os.path.exists(infile):
        noun_phrase = most_freq_noun_phrase(infile, False)
        gold1 = "[('the donkey', 6), ('the mule', 3), ('load', 2)]"
        gold2 = "[('the donkey', 6), ('the mule', 3), ('burden', 2)]"
        retval = str(noun_phrase[7])

        print("gold:\t", gold1)
        print("OR:\t", gold2)
        print("retval:\t", retval)

        assert retval == gold1 or retval == gold2, "test Fail:\n {} != {} OR {}".format(noun_phrase[7], gold1, gold2)
        print("Pass")
    else:
        print("Test fail: path does not exist;", infile)

def test_most_freq_pos_tags(infile="fables-pos.txt"):
    """
    Tests most_freq_pos_tags().
    Do not modify this function.
    :return:
    """
    print("\nTesting most_freq_pos_tags() ...")

    import os
    if os.path.exists(infile):
        pos_tags = most_freq_pos_tags(infile, False)
        gold = "[('DT', 28), ('NN', 24), ('IN', 21)]"
        retval = str(pos_tags[7])

        print("gold:\t", gold)
        print("retval:\t", retval)

        assert retval == gold, "test Fail:\n {} != {}".format(pos_tags[7], gold)
        print("Pass")
    else:
        print("Test fail: path does not exist;", infile)


def run_tests():
    test_get_words()
    test_get_pos_tags()
    test_get_noun_phrases()
    test_most_freq_noun_phrase()
    test_most_freq_pos_tags()


if __name__ == '__main__':

    # comment this out if you dont want to run the tests
    run_tests()

    parser = argparse.ArgumentParser(description='Assignment 2')
    parser.add_argument('-i', dest="pos_sent_fname", default="blogs-pos.txt",  help='File name that contant the POS.')

    args = parser.parse_args()
    pos_sent_fname = args.pos_sent_fname

    most_freq_noun_phrase(pos_sent_fname)

