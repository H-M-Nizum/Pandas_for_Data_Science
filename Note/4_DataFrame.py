1) Constructing a DataFrame object : 
        data = {'country': ['Italy','Spain','Greece','France','Portugal'],
                'popu': [61, 46, 11, 65, 10],
                'percent': [0.83,0.63,0.15,0.88,0.14]}
        df = pd.DataFrame(data, index=['ITA', 'ESP', 'GRC', 'FRA', 'PRT'])

2) DataFrame from 'nested' dictionary: 
        un_data = {'GRC':{'2013':25, '2014':26, '2015':24.5},
                   'ESP':{'2013':23, '2014':27, '2015':26.5}}
        df = pd.DataFrame(un_data)

3) Loading data from external file : 
      i. Import from xls, xlsx - 
                        df = pd.read_excel("../../data/sampledata.xls",sheetname="Data-8",\skiprows=3, header=0, index_col=0)
      ii. Import from csv - 
                        df = pd.read_csv("../../data/sampledata.csv",sep=',',skiprows=3, header=0, index_col=0)


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                              Data access in DataFrame
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Accessing data in a DataFrame object can be done in many ways. Below we present the most important of them, that enable accessing data:
1) By column   2) By row (.ix, .iloc, .loc)     3) By scalar values (.at, .iat)

1. Accessing data by column :- 
        Selecting columns can be done in two ways:
          a) Using the column names as indexes - 
                * Just provide the column name as index, the way you would do it in a dictionary ->  c = df['Country']
                * You may provide the column label as a list, in which case you get a new DataFrame  -> c = df[['Country']]
                * In case a column name is a single non-digit string, using the dot notation will work the same   ->  df.Country
                * For more columns privide a list of column names (note the double brackets)   -> df[['Country', '2007', '2015']]

          b) Using the position (integer index) of the columns - 
                * Provide a list of column position. Note the list (not simply an indeger index)  -> df[[1]]
                * For more columns privide a list of column positions (note the double brackets)  -> df[[1, 3, 5]]
                * List comprehensions can also be used to define a list of integer indices        -> df[[i for i in range(3)]]
