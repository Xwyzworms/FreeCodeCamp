import math
def add_time(start, duration,dayparams=None):
    
    start = start.split(":")
    theHourStart = int(start[0])
    theMinuteStart= int(start[1].split(" ")[0])
    DayOrNight=start[1].split(" ")[1]
    
    moreHour = 0
    moreDays = 0
    dayparamsidx = 0
    message = ""

    duration = duration.split(':') 
    durationHour = int(duration[0])
    durationMinutes = int(duration[1])
    theMinuteStart +=  durationMinutes
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday' ,'Thursday' ,'Friday' ,'Saturday']

    if(dayparams != None):
        for dayidx in range(len(days)):
            if(days[dayidx] == dayparams.lower().capitalize()):
                dayparamsidx = dayidx
    if(theMinuteStart > 59):
        theMinuteStart -= 60
        moreHour+=1
    if(moreHour != 0):
        theHourStart += moreHour
    if(theHourStart <= 12):
       moduloDurationHour = durationHour % 24
       durationHour -= moduloDurationHour
       theHourStart += moduloDurationHour

    if(durationHour >12 ):
        moreDays = math.ceil(durationHour // 24) + 1
        if(durationHour == 24 and durationMinutes == 0 ):
          moreDays = math.ceil(durationHour//24)
    else:
        theHourStart += durationHour
    
    if theHourStart > 11:
        if(theHourStart  > 12):
            if DayOrNight == "AM":
                DayOrNight = "PM"
            else:
                DayOrNight = "AM"
                message ="(next day)"
            theHourStart = theHourStart - 12
            
        elif theHourStart == 12:
             if DayOrNight == "AM":
                DayOrNight = "PM"
             else:
                DayOrNight = "AM"
    if moreDays == 1:
        if(dayparams != None):
            dayparamsidx = (dayparamsidx + 1) % len(days) 
            message = days[dayparamsidx] + ' (next day)'
        else:    
          message = "(next day)"
    elif moreDays > 1:
        if(dayparams != None):
            dayparamsidx = (dayparamsidx + moreDays) % len(days)
            message = days[dayparamsidx] + " (" + str(moreDays) + " days later" + ")"
        else:
            message = "(" + str(moreDays) + " days later" + ")"
    else:
        if(dayparams != None):
            message = days[dayparamsidx]
    if(len(str(theMinuteStart))  < 2):
        theMinuteStart = "0" + str(theMinuteStart)
    if(dayparams == None):
        ans = str(theHourStart) + ":" +str(theMinuteStart) + " " + DayOrNight + " " + message
    else:
        ans = str(theHourStart) + ':' +str(theMinuteStart) + ' ' +DayOrNight +", " + message
    return ans.rstrip()
