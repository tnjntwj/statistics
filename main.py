def avg(*data):
    avg = sum(data)/len(data)
    return avg

def var(*data):
    for i in range(len(data)):
        var = (avg(*data)-data[i])**2/len(data)
    return var

def mdn(*data):
    if len(data) % 2 == 0:
        mdn = (data[int(len(data)/2 -1)] + data[int(len(data)/2)]) /2
    else:
        mdn = data[len(data)/2]

    return mdn
 
a = [1,2,3,4,5,6,7,8,9,10]
print(avg(*a))
print(var(*a))
print(mdn(*a))