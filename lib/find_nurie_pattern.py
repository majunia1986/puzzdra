for i in range(0, BASIC_UNIT_NUM):
    if(flag[i]) == 1:
        for j in range(len(units[i])):
            indv_blng_units_lst[units[i][j]-1].append(i)
print "board status : %s" % indv_blng_units_lst

######################################################
#check if there are merginable units and then merge
# x x x *     x * * *     * * * *     x x x *
# * * * *  +  x * * *  +  * * * *  >  x * * *
# * * * *     x * * *     x x x *     x x x *
#
# merge lists which have the mutual elements
# [[0,6],[0],[0],[],[6],[],[],[],[4,6],[4],[4],[]] > [[0,4,6]]
######################################################
BOARD_NUM = 12 # in case of 3*4 board

#mergable_units_lst are likely to be [[G1,G3],[G4,G6],,,]
mergable_units_lst = []
for i in range(0, BOARD_NUM):
    print "start i=%d/12,mergable_units_lst:%s" % (i,mergable_units_lst)
    #in case of initial, add
    if mergable_units_lst == []:
        mergable_units_lst.append(indv_blng_units_lst[i])
        print "init : %s" % mergable_units_lst
        continue
    
    append_flag = -1
    for j in range(len(indv_blng_units_lst[i])):
        print "start j=%d" % j
        unit = indv_blng_units_lst[i][j]
        print "i,j,len(indv_blng_units_lst[i]), indv_blng_units_lst[i] are %d,%d,%d,%s" % (i,j,len(indv_blng_units_lst[i]),indv_blng_units_lst[i])
        #[0,6]
        for k in range(len(mergable_units_lst)):
            print "start k=%d" % k
            #start to jadge if this unit should be merged or not
            extend_flag = -1
            for l in range(len(mergable_units_lst[k])):
                if flag == 0:
                    continue
                print "i,j,k,l : %d,%d,%d,%d\t unit,check_lst,flag : %d,%s,%d" % (i,j,k,l,unit,mergable_units_lst[k],extend_flag)
                if mergable_units_lst[k][l] == unit :
                    #should be merged cause alreday exists in the list
                    print "flag is changed to 0"
                    extend_flag = 0
                else:
                    #should not be merged cause never exists in the list
                    print "flag is changed to 1"
                    extend_flag = 1
            
            if extend_flag == 0 :
                print "through merge: %s + %s" % (mergable_units_lst[k],indv_blng_units_lst[i])
                mergable_units_lst[k].extend(indv_blng_units_lst[i])
                tmp_uniq_lst =  list(set(mergable_units_lst[k]))
                mergable_units_lst[k] = tmp_uniq_lst
                print "new lst: %s" % mergable_units_lst


    # if
    # print "through append:%s, %s" % (mergable_units_lst,indv_blng_units_lst[i])
    # if(indv_blng_units_lst[i] != []):                    
    #                 mergable_units_lst.append(indv_blng_units_lst[i])


                        
print "%s" % mergable_units_lst
                        
#create mergable indvisuals from mergable_units_lst
mergable_indivisuals_lst = []
for i in range(len(mergable_units_lst)):
    mergable_indivisuals = []
    for j in range(len(mergable_units_lst[i])):
        unit = mergable_units_lst[i][j]
        mergable_indivisuals.append(units[unit])
    flatterned_mergable_indivisuals = [e2 for e1 in mergable_indivisuals for e2 in e1]
    mergable_indivisuals_lst.append(list(set(flatterned_mergable_indivisuals)))

print "%s" % mergable_indivisuals_lst

