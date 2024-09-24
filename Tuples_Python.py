# Tuples In Python

.Tuples are used to store multiple items in a single varibles.
.Tuples is one of the buit-in data types in python used to store collections of data.
.Tuples is a collection of objects separated by commas.
.Tuples is similar a python List in terms of Indexing,Nested objects , and repetition but the difference between
 the two is that cannot change the elements of a tuple once it is assigned

.Tuple items are indexed, the first item has index, [0] and the second items as index [1] etc.
.Tuple are unchangeable, meaning that we cannot change, add or remove items .
.Since tuples are indexed , they can have items with the same value.

.And tuples is used to   (  ) this brackets paranthesis And separates by the Commas ( , , , , ,) ,, And Store the Character and Numerics Values and Complex numbers
("Vedant", "is" , 1,2,3 , 50+5j )


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                                            Tuples ->
                                                          1 =>  a =(1,2,3,4,5)
                                                                  print(a)
                                                                  print(type(a)

                                                ==> Mixed Tuples
                                                                           
                                                         2 => b =("vedant",70,50+5j)
                                                                   print(a)

                                                ==> Empty Tuples
                                                                        
                                                        3 => c = ()
                                                             print(c)
                                                                        
                                                ==> Nested Tuples
                                                            
                                                        4 => d = ("coder",(70,52,86),[1,2,3],50+5j)
                                                                        print(d)

                                                ==> Single Tuples  Making

                                                        5 => e = ("vedant)
                                                                  print(e)                  
                                                                  print(type(e) -> make a string because cannot be used Commas ,

                                                                   ^^^^^^^^^^^^^^^
                                                                   e = ("vedant",)
                                                                      print(e)   -> then this is called a tuple because this value assign a { Comma , }

                                                ==> Tuple Constructor

                                                            6 => a = tuple(("a","b","c"))          ---> change the data types of the tuple() 
                                                                        print(a)

===========================================================================================================================================================================

                                                                        Indexing In Tuples ->
                                                                        
                                                        Positive Indexing -> Left - Right ( 0 -- 5)
                                                        Negative Indexing -> Right - Left (-1 -- -5)

                                                                  1 ->      a=(47,50,55)
                                                                             print(a[5])

                                                                  2 ->     b=([47,50,55])
                                                                             print(a[-5])

                                                                  3 ->    c=(47,50,55,"python","codes")
                                                                             print(a[5])
                                                                        
                                                                  4 ->     d=(47,50,55"python","coders")
                                                                             print(a[-5])

========================================================================================================================================================================

                                                                        Slicing In Tuples ->
                                                                        
                      (  Slicing => slicing means slice the any items and products any things to slice cut this is called is slicing  )

                                                                [ Start :  End ]  -> [ 0 : 5]
                                                                [ Start : End : Step ]  -> { 0: 5: 2 ]

                                                                Examples ->
                                                                      1 ->  a=(10,20,55,66,14)
                                                                             print (a[0:5])
                                                                        
                                                                       2 -> b=(10,20,55,66,96)
                                                                            print (b[:])

                                                                       3 -> c=[10,85,69,32,15)
                                                                            print (c[0:])

                                                                        4 -> d=[1,5,8,9,10]
                                                                              print (d[0:5:2])
                                                                        
=====================================================================================================================================================================

                                                        ==> How to ADD and REMOVE tuple items ,,because tuple as NO option to ADD and REMOVE..
                                                        ==> only LIST Allows and ADD and REMOVES the items..
                                                        ==> And DELETE the items in TUPLES but show the erros because tuples is DELETED 

                                                                        => using this funciton -> .append() -> To ADD Itmes
                                                                                                  .remove() -> To REMOVE Itmes
                                                                                                   del  -> To DELETE Itmes


                                                        EXAMPLES =>
                                                                   1=>     a = (20,40,60,80)
                                                                           y = list(a)
                                                                           y.append(100)
                                                                           a=tuple(y)
                                                                           print(a)


                                                                    2=>    a=(20,40,60,80,100)
                                                                           y=list(a)
                                                                           y.remove(100)
                                                                           a=tuple(y)
                                                                           print(a)


                                                                     3=>   a=(10,20,30,40,50)
                                                                           del a
                                                                            print(a)
         ===============================================================================================================================================================
                                                                         Join Two Tuples AND Multiple (*) Two Tuples->

                                                                        Examples=>
                                                                               1-> tuple1 = ("a","b","c")
                                                                                   tuple2 = (1,2,3)
                                                                                   tuple3 = tuple1 + tuple2
                                                                                   print(tuple3)

                                                                              2->  a = ("computer","system",70,50)
                                                                                   b = ("vedant","ritesh",50,60)
                                                                                    print(a+b)
                                                                        
                                                                        
                                                                              3-> a=("apple","data","python)
                                                                                  b=a*2
                                                                                  print(b)

                                                                             4-> a=("vadant","coder",70,52,86)
                                                                                b=a*3
                                                                                print(b)


    ====================================================================================================================================================================
                                                                        @->  Write a program, to take 5 Input from the user and store it in a Tuple  :-
                                        T=()
                                        i=0
                                        while i<=5:
                                                num=int(input("Enter the values Please :-"))
                                                T  = T +(num,)
                                                i = i+1
                                                print(T)

    ----------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                     
                                                                    

        

                    




                                                                        















































 
