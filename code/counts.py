

import sys
import re
import time




def main():

    # load the data
    try:
        text_file = sys.argv[1]
        with open(text_file, 'r') as f:
            pass
    except Exception, e:
        print '\n\tusage: python %s <text_file>\n' % sys.argv[0]
        exit(1)


    # read the data
    with open(text_file, 'r') as f:
        #text = f.read(100000000)
        text = f.read()


    # which phrases to look up
    queries = ['pizza store', 'pizza shop', 'pizza place', 'pizza joint', 'pizzeria', 'pizza land', 'pizza park', " s pizzeria"]

    #for i in range(
    #print len(text)
    #exit()
    '''
    tokens = text.split()
    vocab  = set(tokens)

    print
    print 'tokens: %d' % len(tokens)
    print 'vocab:  %d' % len(vocab)
    print
    '''

    # count each number of queries
    for query in queries:
        starttime = time.time()
        matches = re.findall(query, text)
        endtime = time.time()
        difftime = endtime - starttime
        print '\t%-12s:%6d\t(%0.3f)' % (query,len(matches),difftime)



if __name__ == '__main__':
    main()



