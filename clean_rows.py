def clean_rows(df,list1=[],drop=[]):
    a = df.select_dtypes(include='object')
    for i in a.columns:
        for x in a.index:
            try:
                c = list1.index(a[i].iloc[x:x+1][x])
                a[i].iloc[x:x+1][x] = c
            except:
                list1.append(a[i].iloc[x:x+1][x])
                a[i].iloc[x:x+1][x] = len(list1)-1
    a.fillna(len(list1))
    d = df.select_dtypes(exclude='object').fillna(0)
    try:
        return pd.concat([d,a],axis=1).fillna(0).drop([drop],axis=1)
    except:
        return pd.concat([d,a],axis=1).fillna(0)