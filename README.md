## Regular expression matcher

Given a part of speech tagged sentence:
> All/DT animals/NNS are/VBP equal/JJ ,/,but/CC some/DT animals/NNS are/VBP more/RBR equal/JJ than/IN others/NNS ./. 


A regular  expression  is used to  match  only  the  words  of  each  word/pos-tag(pos = Part of Speech)  in  the  sentence, excluding all the punctuation marks.
Consider the variable pos_sent is equal to the sentence above. A python function named get_words that takes the pos_sent as input and uses regular expression in to find a list of words. This function returns a sentence including each token separated by whitespace.  
The correct  output  of  the pos_sent is:
> All animals are equal but some animals are more equal than others

Consider the variable pos_sent is equal to the sentence above. A python function named
get_pos_tags that takes the pos_sent as input and uses a regular expression to find a list of pos
tags, excluding punctuation marks. This function returns a list including each tag in their
original order. 
The correct output of the pos_sent is : 
> [’DT’, ’NNS’, ’VBP’, ’JJ’, ’CC’, ’DT’, ’NNS’, ’VBP’, ’RBR’, ’JJ’, ’IN’, ’NNS’]

Given a part-of-speech tagged sentence like the one above, a regular expression is used to match simple noun phrases. A simple noun phrase is a single optional determiner followed by zero or more adjectives ending in one or more nouns.
A python function named get_noun_phrases, which also takes a variable pos_sent as input, searches for noun phrases in pos_sent using the regular expression above. This function returns a list of noun phrases without tags. 
The correct output of the previous sentence is :
> [’All animals’, ’some animals’, ’others’]


Given the pos-tag files CORPUSNAME-pos.txt, where the CORPUSNAME is fables or blogs: 
A python function named print_most_freq_noun_phrase, which takes the file name as input, 
prints out (to the stout) the top 3 noun phrases and their counts for each document.  
Then  find  the  most common lowercas enoun phrases are found. 
A correct output would look like this: 
> The most freq NP indocument[7]:  [(’the donkey’, 6), (’the mule’, 3), (’load’, 2)]

A python function named print_most_freq_pos_tags, which takes the file name as input, prints out (to the stout) the top 3 pos tags and their counts for each document. 
A correct output would look like this:
> The most freq pos tags in document[7]:  [(’NNS’,3), (’DT’, 2), (’JJ’, 2)]

Corpus = collection of texts

## WordNet

WordNet is imported from NLTK like other corpus. You can browse WordNet online at http://wordnetweb.princeton.edu/perl/webwn 
or you can use the NLTK WordNet browser by opening a command prompt
(or terminal) window and typing python (or python3 depending on your computer) to enter the Python
environment. Type import nltk and nltk.app.wordnet(), and NLTK should open a WordNet browse
page in your default browser.

### Synsets and Lemmas

Although WordNet is usually used to investigate words, its unit of analysis is called a synset, representing
one sense of a word. For an arbitrary word, i.e. dog, it may have different senses, and we can find its synsets.
Note that each synset is given an identifier that includes one of the actual words in the synset, whether it is
a noun, verb, adjective or adverb, and a number, which is relative to all the synsets listed for the particular
actual word.

Once you have a synset, there are functions to find information about that synset. We will start with
lemma words, lemmas, definitions, and examples.

WordNet contains many relations between synsets. In particular, we quite often explore the hierarchy of
WordNet synsets induced by the hypernym and hyponym relations. These relations are sometimes called
\is-a" because they represent abstract levels of what things are. 

Picked a word w1 and showed all the synsets of that word and their definitions.
Picked one synset of w1 and show all of its hyponyms and root hypernyms.
Showed the hypernym path from w1 to the top of the hierarchy.
Chose another word w2 and picked one synset for it. Showed path similarity between the synsets for w1 and w2.
Found the two words that have the highest path similarity from this list [’dog.n.01’, ’man.n.01’, ’whale.n.01’, ’bark.n.01’, ’cat.n.01’]. 
Output all pairs if there is a tie.
Found the paths between two random given synsets. For example ’dog.n.01’ and ’cat.n.01’.

## Language Models

When working with text we usually want to categorize it in some way. 
This is a basic form of semantics and allows us to generalize our knowledge about what the document is about. 
We will look at user generated restaurant reviews from the site we8there2. Given the text of a restaurant
review, we’d like to know whether it is expressing a positive opinion about a restaurant or a negative opinion.
Usually, text classification requires multiple experts to assign a category from a predefined set of categories
to each document we are interested in. This can be very time consuming and expensive. Fortunately, many
review sites, like this one, provide a star rating along with the text. We can use this star rating as our
annotation without requiring any additional manual labeling.
We can use this annotated data in many different ways. For example, we can:
> • learn a classification model to predict the opinion of a new review that has not been given a star rating
(for example on another website).

>• use it to identify words or phrases that are most associated with positive and negative opinions.

>• estimate whether we trust the star rating of an existing review.

In this case, we will model the reviews using a language model. There are 150 restaurant
reviews that have been given a positive rating (an overall score > 3 out of 5) and 150 that have been
given a negative rating (an overall score < 3), for a total of 300 reviews. These are stored in a file called
restaurant-training.data
The file contains a list of user reviews. Each review has the following format:
> Review: INTEGER
FACET_NAME_1 = VALUE_1
FACET_NAME_2 = VALUE_2
...
FACET_NAME_N = VALUE_N 

Normalized the data.
• Lowercased all the words
• Removed stop words.
• Removed all tokens that do not have at least one word character. A word character is an alpha
([a-zA-Z]) or numeric ([0-9]) character that may also include an underscore ( ). This class of
characters is defined as nw in Python regular expressions.

Created a frequency distribution of the unigrams for each category. Wrote these frequencies in descending
order to a file named CATEGORY-unigram-freq.txt, where CATEGORY is either positive or negative.
Each line of the file contains a word and its frequency separated by whitespace.

Created a conditional frequency distribution from the bigrams for each category. Wrote these frequencies
in descending order to a file named CATEGORY-bigram-freq.txt. Each line of the file contains
the condition word, the word, and the frequency, all separated by whitespace.

Foundnd the collocations for each category using the collocations() function. 

Check language-model-answers for analysis.

This was for an assignment in CSE 143 at UCSC with Professor Dilek Hakkani-Tür.

