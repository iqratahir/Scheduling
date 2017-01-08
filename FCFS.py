burst_time = []
arrival_time =[]
average_wait_time = 0
average_turn_around = 0
finished_time = 0
wait = []
print "Enter the number of processes:"

number = input()

print 'Enter arrival time for processes:'

for x in range(number):
    print 'for P [',(x+1),']:'
    arrival_time.append(input())

print 'Enter burst time for processes:'

for x in range(number):
    print 'for P [',(x+1),']:'
    burst_time.append(input())

print '\n Process\t|Turnaround_time\t|Waiting_time\n\n'

for x in range(number):
    finished_time+=burst_time[x]
    average_wait_time+=finished_time-arrival_time[x]-burst_time[x]
    average_turn_around+=finished_time-arrival_time[x]
    print "\nP[",(x+1),"]\t\t","\t\t",finished_time-arrival_time[x],"\t\t",finished_time-arrival_time[x]-burst_time[x]

print "\n Average Waiting Time : " , average_wait_time*1.0/number
print "\n Average Turn Around Time : " , average_turn_around*1.0/number    
    
    
