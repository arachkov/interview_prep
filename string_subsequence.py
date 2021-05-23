'''
    Given two strings, determine if the first string is a subsequence of the second string. 
    Note that relative positioning matters. For example, if the inputs are "abcd" and "xyazbcd" 
    then return true, but if the inputs are "abcd" and "xyazbdc" then return false.
'''

def subsequence_stack(s1,s2):
# solution using a stack

    s1_list = []
    for c in s1:
        s1_list.append(c)
    s1_list.reverse()

    for c in s2:
        if c == s1_list[-1]:
            s1_list.pop()
        if len(s1_list)==0:
            return True

    if len(s1_list)>0:
        return False

def subsequence_pointers(s1,s2):
# solution using pointers 

    p1,p2= 0,0 #pointers
    sub = ""

    while p1<len(s1) and p2<len(s2):
        
        if s1[p1]==s2[p2]:
            sub += s1[p1]
            p1+=1
            p2+=1
        else:
            p2+=1
    
    return sub==s1