def my_flattern(l):
    out_lst = []
    
    for i in range(len(l)):
        if out_lst == []:
            print "%d,go" % i
            out_lst.append(l[i])
            continue

        for j in range(len(out_lst)):
            print "i,j,l,r are %d,%d,%d,%d,nogo" % (i,j,l[i],out_lst[j])
            if(l[i]!=out_lst[j]):
                out_lst.append(l[i])

    return out_lst

print "test: %s" % my_flattern([0,1,0,0])
