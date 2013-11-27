# -*- coding: UTF-8 -*-
from .base import algo

INF = float("inf")

def greedy_wrap(words,count,cols,breaks):
    i = j = line = 0
    while(1):
        if i == count :
            breaks[j] = i
            j+=1
            break
        if line == 0 :
            line = len(words[i])
            i+=1
            continue
        if (line + len(words[i])) < cols:
            line += len(words[i])+1
            i+=1
            continue
        breaks[j] = i
        j+=1
        line = 0
        print(i,j)
    breaks[j] = 0
    print("fin greedy_wrap")
    print(breaks)
    return breaks

def show_wrap(words, len_w, breaks):
    lines = []
    i = j = 0
    while ((i < len_w) and (breaks[i] == 0)):
        line = []
        while(j < breaks[i]):
            line.append(words[j])
            j+=1
        lines = lines + [line]
    return lines


@algo("test other knuth algorithm")
def o_knuth(words,width):
    words = list(words)
    len_words = len(words)
    if (len_words == 0):
        return [[]]
    l = [0] * (len_words + 1)
    breaks = greedy_wrap(words,len_words,width,l)
    return show_wrap(words,len_words,breaks)

def retsoluce(words, lines, n): # TODO rename
    if lines[n] == 1:
        line = []
        for i in range(lines[n], n+1):
            line.append(words[i-1])
        return [line]

    p = retsoluce(words, lines, lines[n]-1)
    p.append([words[i-1] for i in range(lines[n], n+1)])
    return p

# TODO rename the function, 'words_wrap' is too vague
def words_wrap(len_word, n, width, exp=2):
    exp = max(1, exp)
    # lc[i][j] will have cost of a line which has words from i to j
    lc = [[0]*(n+1) for _ in range(n+1)]
    # c[i] will have total cost of optimal arrangement of words 
    # from 1 to i
    c = [0]*(n+1)
    # line is used to return the solution
    line = [0]*(n+1)
    # calculate extra space in a single line and line cost
    for i in range(1, n+1):
        # calculate extra spaces in a single line.
        # The value lc[i][j] indicates extra spaces 
        #    if words from word number i to j are
        #    placed in a single line
        lc[i][i] = width - len_word[i-1]
        for j in range(i+1, n+1):
            lc[i][j] = lc[i][j-1] - len_word[j-1] - 1
        # Calculate line cost corresponding to the above calculated extra spaces.
        # The value lc[i][j] indicates cost of putting words 
        #    from word number i to j in a single line
        for j in range(i, n+1):
            if lc[i][j] < 0:
                lc[i][j] = INF
            else:
                lc[i][j] = pow(lc[i][j], exp)

    # Calculate minimum cost and find minimum cost arrangement.
    # The value c[j] indicates optimized cost to arrange words
    #    from word number 1 to j.
    for j in range(1, n+1):
        c[j] = INF
        for i in range(1, j+1):
            if c[i-1] != INF and lc[i][j] != INF and c[i-1] + lc[i][j] < c[j]:
                c[j] = c[i-1] + lc[i][j]
                line[j] = i
    return line

def knuth(words, width, exp):
    words = list(words)
    len_words = len(words)
    if (len_words == 0):
        return [[]]
    l = [len(w) for w in words]
    lines = words_wrap(l, len_words, width, exp)
    para = retsoluce(words, lines, len_words)
    return para

@algo("A Knuth-like dynamic programming algorithm using the square function")
def dynamic_2(words, width):
    return knuth(words, width, 2)

@algo("A Knuth-like dynamic programming algorithm using the cube function")
def dynamic_3(words, width):
    return knuth(words, width, 3)
