import sys
from compiler.ast import flatten

lower_bound = 3

#init
patterns = []

#add 3-5 cases
patterns.append([3])
patterns.append([4])
patterns.append([5])

#in case of 4*5, set 21 
#in case of 5*6, set 31
#in case of 6*7, set 43
for i in range(6,43,1):
    print "start %d" % i

    #add self
    tmp = [[i]]
    j = lower_bound

    while(i - j >= lower_bound) and (j <= i - j):
        l = j
        r = i-j
        
        l_list = patterns[l-3]
        r_list = patterns[r-3]

        for p in range(len(l_list)):
            for q in range(len(r_list)):
                tmp.append(flatten([l_list[p],r_list[q]]))
            
        j += 1
    
    patterns.append(tmp)
#    print "%s" % patterns[i-3]
    tmp = []
    print "end\t%d\t%d" % (i,len(patterns[i-3]))

#print "%s" % patterns[27][20000]
#print "%s" % patterns[39][20000]
print "%s" % patterns[39][20000]
