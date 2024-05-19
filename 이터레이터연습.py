
def 이터():
    l = [1,2,3,4,5]
    for i in l :
        yield i

def 이터2():
    with open('이터') as f:
        for line in f:
            yield int(line)

myiter = 이터()
myiter2 = 이터2()

def 노말(nums):
    total = sum(nums)
    result = []
    print(total)
    for i in nums:
        print(i)
        percent = 100*i / total
        result.append((percent))
    return result

print(노말(myiter))
print(노말(myiter2))
