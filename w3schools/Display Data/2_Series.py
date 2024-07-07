1) What is a Series?
    A Pandas Series is like a column in a table. It is a one-dimensional array holding data of any type.

2) Create a simple Pandas Series from a list:
    import pandas as pd
    a = [1, 7, 2]
    myvar = pd.Series(a)
    print(myvar)

3) Labels : 
    This label can be used to access a specified value. Return the first value of the Series:
      print(myvar[0])

4) Create Labels :
    # With the index argument, you can name your own labels.
        import pandas as pd
        a = [1, 7, 2]
        myvar = pd.Series(a, index = ["x", "y", "z"])
        print(myvar)

    # When you have created labels, you can access an item by referring to the label.
        print(myvar["y"])

5) Objects as Series :
    # like a dictionary, when creating a Series.
    # Create a simple Pandas Series from a dictionary:
        import pandas as pd
        calories = {"day1": 420, "day2": 380, "day3": 390}
        myvar = pd.Series(calories)
        print(myvar)
