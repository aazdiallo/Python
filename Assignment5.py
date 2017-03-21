largest = None
smallest = None

while True:
    num = raw_input("Enter a number: ")
    if num == "done" :
        break
        
    else :
        try :
            num = int(num)
            if largest is None or smallest is None :
                largest = num
                smallest = num
            
            else :
                if largest < num :
                    largest = num
                
                if smallest > num :
                    smallest = num

        except :
            print "Invalid input"

print "Maximum is", largest
print "Minimum is", smallest
x = 'Ghadhakanka'
i = len(x)
print i
while i > 0 :
    print x[i-1], 'index', i
    i = i-1

z = x[0:6]
y = x[6:11]

print z, y
print x[:] # contains the whole string.