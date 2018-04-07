#implement:
#can I cut any more data?
import datetime
import time
inputfromr = 0#set to one if the input file was generated in r, 0 otherwise
earliestdate = str(time.mktime(datetime.datetime.strptime("2016/10/01", "%Y/%m/%d").timetuple()))
filetoread = open("/Users/grayson/desktop/datafest/datafest2018.csv","r")
filetowrite = open("/Users/grayson/desktop/datafest/finalwritefile.csv","w")
header = filetoread.readline()
filetowrite.write(header)
jobids = range(0,1090000)
times = [[] for i in range(len(jobids))]
startdates = [[] for i in range(len(jobids))]
lines = ['']*len(jobids)
linestodo = 0
linesread = 0
for line in filetoread:
        linesread+=1
        if(linesread%10000 ==0):
                print('reading')
                print(linesread/17635296)
        linemod = line
        linemod = linemod.replace('"','')
        splitline = linemod.split(',')
        timesofar = splitline[-3]
        date = splitline[inputfromr]
        date = date.replace("-","/")
        date = str(time.mktime(datetime.datetime.strptime(date, "%Y/%m/%d").timetuple()))
        timesincestart = float(date) - float(earliestdate)
        if(timesincestart/(60*60*24) < float(timesofar)):
                continue
        startdate = float(date) - 60*60*24*float(timesofar)
        splitline[inputfromr] = date
        edrecs = splitline[-4]
        if(edrecs == 'None'):
                edrecs = 0
        if(edrecs == 'High school'):
                edrecs = 1
        if(edrecs == 'Higher education'):
                edrecs = 2
        splitline[-4] = str(edrecs)
        jobid = splitline[2+inputfromr]
        jobid = jobid.replace('job','')
        cid = splitline[1+inputfromr]
        cid = cid.replace('company','')
        jobid = int(jobid)
        timesofar = int(timesofar)
        cid = int(cid)
        splitline[2+inputfromr] = str(jobid)
        splitline[1+inputfromr] = str(cid)
        filetowrite.write(','.join(splitline))
        if (len(lines[jobid])==0):
                times[jobid].append(timesofar)
                lines[jobid]=splitline
                startdates[jobid] = startdate
                linestodo+=1
        else:
                times[jobid].append(timesofar)
linesdone = 0
for idx in range(len(jobids)):
        if (linesdone%1000==0):
                print('writing')
                print(linesdone/linestodo)
        linesdone+=1
        if(len(times[idx])>0):
                maxtime = max(times[idx])
                for i in range(maxtime):
                        if(not (i in times[idx])):
                                strtoedit = lines[idx]
                                startdate = startdates[idx]
                                currentdate = startdate + 60*60*24*i
                                strtoedit[-3] = str(i)
                                strtoedit[-2] = '0'
                                strtoedit[-1] = '0'
                                strtoedit[inputfromr] = str(currentdate)
                                writestr = ','.join(strtoedit)+'\n'
                                filetowrite.write(writestr)
filetoread.close()
filetowrite.close()
