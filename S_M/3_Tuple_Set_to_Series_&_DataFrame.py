import pandas as pd

print("--------------------- Set to convert Series and DataFrame --------------------")
st = {1,2,3,4,5,6}
# s = pd.Series(st) # TypeError: 'set' type is unordered
# print(s) # Series is Ordered

s = pd.Series(list(st))
# OR s = pd.Series(tuple(st))
print(s)
df = pd.DataFrame(st)
print(df)


print("--------------------- Tuple to convert Series and DataFrame --------------------")
tp = (1,2,3,4,5,6)
s1 = pd.Series(tp)
print(s1)
df1 = pd.DataFrame(tp)
print(df1)
