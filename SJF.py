burst_time = []
arrival_time =[]
average_wait_time = 0
average_turn_around = 0
turn_around_time = 0
wait = []
temp = 0
process = []
total = 0
print "Enter the number of processes:"

number = input()

for x in range(number):
    process.append([])
    print'Enter process number:'
    process[x].append(input())

print 'Enter burst time for processes:'

for x in range(number):
    print 'for P [',(x+1),']:'
    burst_time.append(input())

print '\n Process\t|Burst_time\t|Waiting_time\n\n'

for x in range(number):
    smallest = x
    for y in range(x+1,number):
        if (burst_time[y]<burst_time[smallest]):
            smallest=y
    temp=burst_time[x]
    burst_time[x]=burst_time[smallest]
    burst_time[smallest]=temp

    temp=process[x]
    process[x]=process[smallest]
    process[smallest]=temp
wait.append(0)

for x in range(1,number):
    wait.append(0)
    for y in range(x):
        wait[x]+=burst_time[y]
    total+=wait[x]
average_wait_time= total*1.0/number
for x in range(number):
    print"\nP[",(x+1),"]\t\t","\t\t",burst_time[x],"\t\t",wait[x]
print"\n\Total Waiting Time=",total
print"\n\Average Waiting Time=",average_wait_time

