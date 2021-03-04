def dropCol(dataframe, col):
    newdf = dataframe
    if not isinstance(col, list):
        col = [col]
    for c in col:
        try:
            newdf = newdf.drop(c, axis=1)
        except:
            print("couldn't drop", c)
    return newdf
