import sys, random

def checkNotAvailable(arr, size, num):
    a = 0
    for x in range(1,size + 1) :
        if(a == 1 and arr[x] == 0) :
            return False
        if(arr[x] == 0) :
            a = 1
    return True

lineCount = 0

while(lineCount <= 1000) :
    tasks = random.randrange(1, 101)
    rules = random.randrange(1, 101)
    seenRules = [0]*(101)
    seenTasks = [0]*(101)

    lineCount += 1+rules
    ruleCount = 0
    taskCount = 0

    print tasks, rules
    
    while(ruleCount < rules) :
        seenRNum = random.randrange(1, 101)
        while(seenRules[seenRNum] != 0 and checkNotAvailable(seenRules, rules, seenRNum)) :
            seenRNum = random.randrange(1, 101)
        seenRules[seenRNum] = 1
        curTaskCount = random.randrange(1, 101)
        print seenRNum, curTaskCount,
        while(taskCount < curTaskCount) :
            seenTNum = random.randrange(1, tasks+1)
            while(seenTasks[seenTNum] != 0) :
                seenTNum = random.randrange(1, tasks+1)
            seenTasks[seenTNum] = 1
            print seenTNum,
            taskCount += 1
        print
        taskCount = 0
        seenTasks = [0]*(tasks + 1)
        ruleCount += 1

print "line count is", lineCount
    






