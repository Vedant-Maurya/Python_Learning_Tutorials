#string in python
(A string is a data structure in python that represents a sequences of characters.) it is an immutable data type , meaning that once you have created a string,you cannot
change it. strings are used widely in many diffrent  applications such as stroring and manipulating text data representing names , addresses, and others types of data
that can be represented as text.
                            {python string is the collection of the character surrounded by single quote,double quote and triple quotes. the compute does not understand the
                             character : internally it stores the character form of the combination the [0 and 1] format},,
    pEach character is encoded in the (ASCII) or (Unicode) character string can be created by enclosing the character or the sequences of character in the quotes
                             {python allows us to use single quotes, double quotes, and triple quotes create in the string}
                             EXAMPLES =>
                             a = "use in double quotes string"
                             b = 'use in single quotes string'
                             c = """ use in triple quotes string"""
                             print(a,b,c)


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                             Indexing in string ->

                                                                              H   E   L   L   L
                            -> Right Indexing                                 0   1   2   3   4
                            -> Left Indexing                                  -5  -4  -3  -2  -1
                             NOTE ==> and space is also counting in string

            ===================================================================================================================================================
            Examples =>
                        a = "Vedant is coder"
                        print(a[5])
                        print(a[4])
                        print(a[3])

                        b = "Vedant is coder "
                        print(a[-4])
                        print(a[-5])
                        print(a[-3])
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                            Slicing of string ->

                                                    [Start:End]  ->[0:5]
                                                    [Start:End:Step] ->[1:18]
                                                    
                            Note => Spaces is also count in slicing of string...

                            Examples =>
                                        a = "hello students what are doing ? "
                                        print(a[0:5])
                                        print(a[10:18])     --->start to end slicing
                                        print(a[0:18:2])    --->step in slicing  ,,and step is using the Alternate number [ 1+1 ] value 

         =========================================================================================================================================================
                                                     lenght in string  ->

                                                     a = "vedant how are doing "
                                                     print(len(a))
                                                     
                                Notes => Length is not count the ( blanck space )
                                
------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                    .upper() , .lower() , .replace() , .find() functions  ->

                                                a="vedant"
                                                print(a.upper())

                                                b="vedant"
                                                print(a.lower())

                                                c"vedant is a coder"
                                                print(a.replace("vedant","sameer")      -> .replace( give the replace syntax "", "") replace any character and a single word replace this -:

                                                d="vedant is a coder"
                                                print(a.replace("V","S")

                                                e="vedant is a located in GKP
                                                print(a.find("v"))
                                                print(a.find("GKP")
                                                      






















                                    





















                                                             

                    
