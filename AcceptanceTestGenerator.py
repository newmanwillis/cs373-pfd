import sys, random

lineCount = 0

while(lineCount <= 1000) :
    tasks = random.randrange(1, 101)
    rules = random.randrange(1, 101)
    seenRules = [0]*(rules + 1)
    seenTasks = [0]*(tasks + 1)

    lineCount += 1+rules
    ruleCount = 0
    taskCount = 0

    print tasks, rules
    
    while(ruleCount < rules) :
        seenRNum = random.randrange(1, rules+1)
        while(seenRules[seenRNum] != 0) :
            seenRNum = random.randrange(1, rules+1)
        seenRules[seenRNum] = 1
        curTaskCount = random.randrange(1, tasks+1)
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
    






