#this algorithm takes too much time for huge number so I need to redesign better algorithm
#s=input string to be repeated
#n=the length of string upto how much it should be repeated

def repeatedString(s, n):
    x=0
    mycount=0
    while x<n:
        y=0
        for y in range(len(s)):
            x=x+1
            if x>n:
                continue
            if s[y]=='a':
                mycount=mycount+1
    return mycount
##This is the second version applicable for all types and length of strings
##I used mathematics to solve it
###s=input string to be repeated
###n=the length of string upto how much it should be repeated


def repeatedString(s, n):
    len_str=len(s)

    num_of_a=s.count('a')

    amt_def_str_pos_in_n = int(n/len_str)

    def_str_len = len_str * amt_def_str_pos_in_n

    amt_of_a_in_def = amt_def_str_pos_in_n * num_of_a
    
    if def_str_len!=n:
        diff= n - def_str_len
        for x in range(diff):
            if s[x]=='a':
                amt_of_a_in_def=amt_of_a_in_def+1
        return amt_of_a_in_def
    else:
        return amt_of_a_in_def
