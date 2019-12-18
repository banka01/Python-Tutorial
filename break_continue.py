## break and continue

## break is used to come out of the loop
## come out of the first immeditae for loop in which it is enoountered

### for a given  nos, break on some cond
for x in range(1,100):
    if x == 50:
        break
    print(x)

## continue
print('*'*100)
for x in range(1,100):
    if x % 5==0:
        continue
    ###
    #####
    print(x)

