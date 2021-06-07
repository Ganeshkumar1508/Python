def check(s1, s2):
     
    # the sorted strings are checked
    if(sorted(s1)== sorted(s2)):
        print("The strings {0} and {1} are anagrams.".format(s1,s2))
    else:
        print("The strings {0} and {1} aren't anagrams.".format(s1,s2))        
         
# driver code 
s1 = input("Enter String One: ")
s2 = input("Enter String Two: ")
check(s1, s2)