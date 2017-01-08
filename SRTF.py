arrival_time=[]
burst_time=[]
run_time=[]
sum_wait=0
sum_turnaround=0
time=0
remain=0
number=int(input("Enter number of Process : "))
i=0
while i<number:
        print "For process[",(i+1),"]:"
        arrival_time.append(int(input("Enter arrival time of process :")))
        burst_time.append(int(input("Enter burst time of process :")))
        run_time.append(burst_time[i])
        i+=1

print "\n\nProcess\t|Turnaround Time| Waiting Time\n"
run_time.append(99999)
j=i   	
while remain!=number:
        smallest=j
        i=0
        while (i<number):
                if arrival_time[i]<=time and run_time[i]<run_time[smallest] and run_time[i]>0:
                        smallest=i
                i+=1       
        run_time[smallest]-=1
        if run_time[smallest]==0:
                remain+=1
                end_time=time+1
                print smallest+1,"\t\t",end_time-arrival_time[smallest],"\t\t",end_time-burst_time[smallest]-arrival_time[smallest]
                sum_wait+=end_time-burst_time[smallest]-arrival_time[smallest]
                sum_turnaround+=end_time-arrival_time[smallest]
        time+=1
print "\nAverage waiting time = ",sum_wait*1.0/number
print "Average Turnaround time = ",sum_turnaround*1.0/number
