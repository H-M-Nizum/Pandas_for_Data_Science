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


2. Accessing data by row :- 
        Selecting rows can be done in three ways:
                a) Using the .loc indexer for selection by label -
                        # Note that a row is now constructed as a new DataFrame
                                gr = df.loc[['GRC']]
                        # You can provide a single label as an single index (not in a list). In this case the row is now constructed as a new Series object
                                gr = df.loc['GRC']
                        # More rows: provide the list of labels
                                df.loc[['GRC','ESP','PRT']]
                        # Slicing rows is also possible (note that single brackets are used)
                                df.loc['ESP':'GRC']

                b) Using the .iloc indexer for selection by position -
                        # Provide the list of row positions
                                gr = df.iloc[[2]]
                        # You can provide a single label as an single index (not in a list). In this case the row is now constructed as a new Series object
                                esp = df.iloc[0]
                        #More rows: provide the list of integer position indexes
                                df.iloc[[2,4,6]]
                        # Slicing rows is also possible (note that single brackets are used)
                                df.iloc[2:5]

                c) Using the .ix indexer -
                        # ix is the most general indexer and supports bot inputs in label and integer format. Before using it however it is advisable to read the pandas documentation on .ix (here)
                        # .ix with row label
                                df.ix[['PRT']]
                        # .ix with list of row positions
                                df.ix[[0,2,4]]
                        # Slicing with labels
                                df.ix['ESP':'GRC']
                        # Slicing with positions
                                df.ix[3:5]


3. Accessing scalars (single data items)
        Selecting scalars can be done in two major ways:
                a) Using the [ ] notation to provide column & row indexes - 
                                ita = df['Country']['ITA']
                        # Also works without brackets for non-digit string indices
                                esp = df.Country.ESP

                b) Using the .at and .iat indexers - 
                        # Using the .at indexer
                        # Provide first the row label and then the column name (remember: .at is a non-integer indexer)
                                d = df.at['FRA','Country'] 
                                d = df.at['FRA','2015'] 
                        
                        # Using the .iat indexer
                                d = df.iat[0,0] 
                                d = df.iat[7,9] 








