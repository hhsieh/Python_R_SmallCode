#This python function generates ngrams (n >=1 ) from a list of strings
def ngrams(tokens, MIN_N, MAX_N):
    n_tokens = len(tokens)
    for i in xrange(n_tokens):
        for j in xrange(i+MIN_N, min(n_tokens, i+MAX_N)+1):
            yield tokens[i:j]
            
# Test the code
tokens = ["this", "is", "not", "so", "nice"]
N = ngrams(tokens, 1,2)
bigrams = [" ".join(i) for i in N]
print(bigrams)

#list comprehension to gather ngram frequencies
frq = [bigrams.count(y) for y in bigrams]
print(frq)
