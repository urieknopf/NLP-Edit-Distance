# NLP-Edit-Distance
Edit Distance assignment from Natural Language Processing class at ESU

Input two different words (or misspelling of words) to see the edit distance between them.
Edit distance is calculated using levenshtein distance with cost of 1 for insertions or deletions and 2 for substitutions.

Output shows the minumum edit distance, the distance matrix, pointer matrix, and alignment.

To run code, just run in any python ide or somewhere else that would run python.


Sample Output:
Enter target string: apple
Enter initial string: orange
------------------------------------------------
Words to compare:  orange apple
Min edit distance:  7

    #  a  p  p  l  e  
#  [0, 1, 2, 3, 4, 5]
o  [1, 2, 3, 4, 5, 6]
r  [2, 3, 4, 5, 6, 7]
a  [3, 2, 3, 4, 5, 6]
n  [4, 3, 4, 5, 6, 7]
g  [5, 4, 5, 6, 7, 8]
e  [6, 5, 6, 7, 8, 7]
 
     #    a    p    p    l    e  
#  [' ', 'L', 'L', 'L', 'L', 'L']
o  ['U', 'G', 'G', 'G', 'G', 'G']
r  ['U', 'G', 'G', 'G', 'G', 'G']
a  ['U', 'G', 'L', 'L', 'L', 'L']
n  ['U', 'U', 'G', 'G', 'G', 'G']
g  ['U', 'U', 'G', 'G', 'G', 'G']
e  ['U', 'U', 'G', 'G', 'G', 'G']
 
ora*nge 
||||||| 
**apple 
dd iss 
