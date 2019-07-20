spam = ['apples', 'bananas', 'tofu', 'cats']

def comma(spam):
    for item in spam[0:len(spam)-2]:
        egg = []
        egg.append(item)
        for york in egg:
            print(york, end=', ')

    secLast = []
    secLast = spam[-2]
    print(secLast, end=' and ')
    
    last = []
    last = spam[-1]
    print(last, end='')
    
    
comma(spam)
