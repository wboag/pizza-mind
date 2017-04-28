

import numpy as np
import os




def main():

    # which phrases to look up
    #queries = ['pizza store', 'pizza shop', 'pizza place', 'pizza joint', 'pizzeria', 'pizza land', 'pizza park']
    queries = ['pizza store', 'pizza shop', 'pizza place', 'pizzeria', 'pizza land', 'pizza park']
    tok_queries = [ q.split() for q in queries ]


    # load word vectors
    vocab = set(sum(tok_queries, []))
    w2v_file = '/data1/nlp-data/GoogleNews-vectors-negative300.bin'
    vectors = read_bin_vectors(w2v_file, vocab=vocab)

    query_embeddings = [centroid([vectors[w] for w in q]) for q in tok_queries]

    # count each number of queries
    n = len(queries)
    scores = np.zeros( (n,n) )
    for i in range(n):
        for j in range(n):
            scores[i,j] = cosine(query_embeddings[i],query_embeddings[j])

    '''
    scores = scores - scores.min(axis=0)
    ranges = scores.max(axis=0) - scores.min(axis=0)
    scores = scores / ranges
    '''

    print ' '*15,
    for query in queries:
        print '%-10s' % query.split()[-1],
    print

    for i in range(n):
        print '%10s' % queries[i].split()[-1],
        for j in range(n):
            score = scores[i,j]
            print '%10.3f' % score,
        print



def centroid(vecs):
    val = np.zeros(vecs[0].size)
    return sum(vecs, val)


def cosine(u, v):
    return np.dot(u,v) / ((np.dot(u,u) * np.dot(v,v))**0.5)



def read_bin_vectors(fname, verbose=0, dev=False, vocab=[]):
    """
    Loads 300x1 word vecs from Google (Mikolov) word2vec
    """

    if not os.path.exists(fname):
        print '\n\tERROR: word embeddings file %s does not exist.'
        print           '\tPlease download the standard w2v GoogleNews embedding, change the pathname, and try again\n'
        exit(1)

    #dev = True
    verbose = 0
    word_vecs = {}
    if verbose:
        print 'loading word2vec'
    with open(fname, "rb") as f:
        header = f.readline()
        vocab_size, layer1_size = map(int, header.split())
        binary_len = np.dtype('float32').itemsize * layer1_size
        for line in xrange(vocab_size):
            # short circuit (when we just care about pipeline, not actually using this for tests)
            if dev:
                if line >= 500:
                    break
            # display how long it takes?
            if verbose:
                if line % (vocab_size/40) == 0:
                    print '%6.2f %%' % (100*float(line)/vocab_size)
            word = []
            while True:
                ch = f.read(1)
                if ch == ' ':
                    word = ''.join(word)
                    break
                if ch != '\n':
                    word.append(ch)

            # read through file
            text = f.read(binary_len)

            if vocab and (word not in vocab):
                continue

            word_vecs[word] = np.fromstring(text, dtype='float32')

            # early stopping (if you have everythign from the vocab)
            do_more = False
            for w in vocab:
                if w not in word_vecs:
                    do_more = True
            if not do_more:
                break

    if vocab:
        for w in vocab:
            if w not in word_vecs:
                print 'OOV: ', w

    return word_vecs





if __name__ == '__main__':
    main()



