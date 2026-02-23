def missing_number(a, n):
    #// is used for interger division
    expected=n*(n+1)//2
    actual=sum(a)
    print(expected-actual)

my_arr=[1,2,4,5]
missing_number(my_arr,5)    
