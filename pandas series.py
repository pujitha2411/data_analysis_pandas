import pandas as pd
s1 = pd.Series([1,2,3,4,5])
s2=pd.Series({'name':'pujitha','age':'20','city':'nyw'})
df1 = pd.DataFrame ({
    'name':['pujitha','anusri','punitha','navya','kavitha','pujitha'],

    'age':[20,19,20,23,21,20],

    'city':['nym','hbd','bang','nun','bav','nym',' ']
    })
print(s1)
print(s2)
print(df1)
df1.drop_duplicates()
print(df1)
