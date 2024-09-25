#List in Python

==> Lists are used to store multiple items in a single variable.
==> Lists are one of 4 buit-in data types in python used to store collections of data, the other 3 are [ TUPLES , SET , and DICTIONARY ] all with different qualities and usage

==> Lists are the simplest containers that are an integral part of the python language.
==> A single List may contains DataTypes Like -> Integers,Strings, as well as objects.
==> Lists are mutable, and hence, they can be altered even after their creation.

==> Store Multiples data in One variables with help of 4-data types => [ List,Tuples,Dictionary,Set ]
==> List is uses of  # SQUARE BRACKETS [ ] -> Brackets
==> List items is SEPARATE by COMMAS (,)

 # Functions of List
 ==> List items are Ordered, Changeable, and allow Duplicate values .

  # Ordered ->
              when we say that lists are ordered, it means that the items have a defined order, and that order will not change
               EX => a = [ a,b,c,1,8,9,10 ] -> 1,2,3,4,5,6,7   ( this is the order of list ) 

  # Changeable ->
              the list is changeable,meaning that we can change, add , and remove items in a list after it has been created.
  # Allow Duplicates ->
              since lists are Indexed, lists can have items with the same value.

  # LIST Are allows ALL Data types :-
                             [ string,float, complex,tuple,integers,booleans ] -> by separate the Commas (,)
                              
========================================================================================================================================================================

                                                                 Indexing in List ->

                                                                 Examples =>
                                                                                     a  b  c  d  e
                                                                  Positive index =>  0  1  2  3  4         -> Left to Right
                                                                  Negative index => -5 -4 -3 -2 -1         -> Right to Left

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                                      syntax of list =>          a = [ "apple","banana","cherry" ]
                                                                                 print(a)
                                                                                 print(type(a))

---------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                    Allow Duplicates  In LIST :-

                                                                    a = [ "apple","banana","apple","cherry","apple","banana" ]
                                                                    print(a)

------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                                                    LIST Allows All Data Types :-
                                                                                                [ string,float,complex,integers,booleans,tuple,set ]
                                                                        
                                                                    Examples  :-
                                                                            1-> list1 = ["apple","cherry","banana", ]
                                                                                list2 = [2,5,8,9,7]
                                                                                list3 = [7.8,8.5,9.5]
                                                                                list4 = [True,False,True]
                                                                                print(list1)
                                                                                print(list2)
                                                                                print(list3)
                                                                                print(list4)

                                                                            2-> a = [ 12,-85,20.5,3.6,-98,"students","hello",True,False]
                                                                                print(a)
                                                                                print(type(a))


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                                                            Allows Items In List  ->
                                                                                        Indexing Items in List :- Left TO Right => Start 0-5
                                                                                                                  Right To Left => Start -1-5
                                                                                                                    
                                                                                        Examples :-
                                                                                            1-> a=[50,"apple",50.6,5]
                                                                                                 print(a[2])
                                            
                                                                                            2-> b=[50,"banana",50.6]
                                                                                                print(a[-3])


-------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                                                                    Slicing In List :-
                                                           => Its means a biggest part of thing cut the [ Small parts of area ] this is called the slicing [ slicing ->cutting ] and its used to the
                                                           => [ Start:End:Step ] ->  [ 0:1:2]
                                                           => and End is work on the [ n+1 ] Decrement the value 1
                                                           => and Step is work on the by ( n+1 Increment of 1 value )
                                                                                   Examples ->
                                                                                           1-> a = [10,50,60,20,82,52]
                                                                                               print(a[0:6])       -> its work in by decrement of  1 number
                                                                                               
                                                                                           2-> a = [10,50,60,20,82,52]
                                                                                               print(a[0:6:2])     -> its use the step 2

                                                                                           3-> a = ["python",'java',"css",50,5.6,]
                                                                                               print(a[1:4])                                                                                        


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                                                    Slicing Change Items In Lists ->
                                                                    
                                                                           Examples-> 
                                                                                    1-> a = ["apple","banana","cherry"]
                                                                                        a[1] = "orange"
                                                                                        print(a)                ---> "apple","orange","cherry"


                                                                                    2-> b = ["orange","pineapple"20,580,58,99,100]
                                                                                        b[4] = "apple"
                                                                                        print(b)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                                                     Slicing Change a Range of items values :-

                                                                                      Examples :-
                                                                                             1->  a = [10,20,50,60,80,90]
                                                                                                  a[2:5] = ["books","copy","pen"]
                                                                                                  print(a)       -> 10,20,"books","copy","pen"

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                                                    .append,,.remove function in LIST :-
                                                                    
                                                                    => .append -> this function is used to (ADD) the items of the list
                                                                    => .remove -> and this function is used to (REMOVE) the items of the list
                                                                    => .reverse -> and this function is used to (REVERSE) the items of the list

                                                                    Examples =>
                                                                            1-> a=[10,20,30,40,50,60,70]
                                                                                a.append(100)
                                                                                print(a)
                                                                                
                                                                            2-> a=[10,20,30,40,50,60,70]
                                                                                a.remove(30)
                                                                                print(a)

                                                                            3-> a=["apple","banana","orange"]
                                                                                a.append("pineapple")
                                                                                print(a)

                                                                            4-> a=["apple","banana","orange"]
                                                                                a.remove("banana")
                                                                                print(a)

                                                                            5-> a=["apple","banana","orange",20,30,40,50,60]
                                                                                a.reverse()
                                                                                print(a)


===========================================================================================================================================================================

    #Write the program all list items to add this items in given the lists :-

    l = [10,20,30,40,50,60,70,80,90]
    print(len(l))
    a = 0
    for i in range(9):
    a = a + l[i]
    i = i + 1
    print("the sum of a list is :-",a)
    


                                                                                
                                                                                





                                                                                
















