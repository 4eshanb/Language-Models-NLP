from nltk.corpus import wordnet as wn
import random
import os
def print_syn_lemmas_def(w1):
    word_net_file = open("wordnet.txt","a+")
    word_net_file.write("Word: "+w1 +'\n\n')
    word_net_file.write("1.Synsets and definitions:" +'\n\n')
    for synset in wn.synsets(w1):
         word_net_file.write(str(synset) + " ")
         word_net_file.write(str(synset.definition()) + '\n')
    word_net_file.write('\n')
    word_net_file.close()
    
    
def print_lexical_rel(syn):
    word_net_file = open("wordnet.txt","a+")
    word_net_file.write("2. Chosen synset: "+ str(syn) + '\n\n')
    word_net_file.write("Hyponyms: "+ str(syn.hyponyms())+ '\n\n')
    word_net_file.write("Root hypernyms:" + str(syn.root_hypernyms()) + '\n\n')

    word_net_file.write("3. Hypernym Path:\n\n")
    paths = syn.hypernym_paths()
    for i in range(len(paths)):
        word_net_file.write("Paths[{}]:".format(i) +'\n')
        [word_net_file.write(syn.name() + '\n') for syn in paths[i]]
    word_net_file.write('\n')
    word_net_file.close()

def print_path_similarity(syn1, syn2):
    word_net_file = open("wordnet.txt","a+")
    word_net_file.write("4. Path similarity: \n\n")
    word_net_file.write("Synset1: "+ str(syn1) +'\n')
    word_net_file.write("Synset2: " + str(syn2) +'\n')
    word_net_file.write("Path similarity :" + str(syn1.path_similarity(syn2)) +'\n')
    word_net_file.write('\n')
    word_net_file.close()
    

def print_highest_path_similarity(syn_list):
    word_net_file = open("wordnet.txt","a+")
    word_net_file.write("5. Highest path similarity: \n\n")
    dict_syn = {}
    keys = [(syn, syn2)for syn in syn_list for syn2 in syn_list]
    max_path_sim_pair = 0
    max_pairs = [] 
    for key in keys:
        if key[0] != key[1]:
            syn1 = wn.synset(key[0])
            syn2 = wn.synset(key[1])
            dict_syn[key] = syn1.path_similarity(syn2)
            #print(str(key) + ", "+str(dict_syn[key]))

    
    max_path_sim_pair = max(dict_syn, key = dict_syn.get)
    max_Val = dict_syn[max_path_sim_pair]
    #print(max_Val)
    for entry in dict_syn:
        if dict_syn[entry] >= max_Val and entry not in max_pairs:
            if [entry[0], entry[1]] not in max_pairs and [entry[1], entry[0]] not in max_pairs:
                word_net_file.write(str(entry) +'\n')
            max_pairs.append([entry[0], entry[1]])
            max_pairs.append([entry[1], entry[0]])
    word_net_file.close()
    #print(max_pairs)
    #print(max_path_sim, dict_syn[max_path_sim])
    #[print() for pair in max_pairs for tup in pair if tup[0][0]]
    #print(dict_syn)

if __name__ == '__main__':
    if os.path.exists("wordnet.txt"):  
        word_net_file = open("wordnet.txt","w")
        word_net_file.write("")
        word_net_file.close()
    
    print_syn_lemmas_def('fish')
    print_lexical_rel(wn.synset('fish.n.01'))
    #print_syn_lemmas_def('fox') #w2
    print_path_similarity(wn.synset('fish.n.01'),wn.synset('fox.n.01'))
    print_highest_path_similarity(['dog.n.01', 'man.n.01', 'whale.n.01','bark.n.01', 'cat.n.01'])

