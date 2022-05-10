import math
def calculateStats(numbers):
  dict_numbers={}
  if len(numbers)==0:
    dict_numbers= dict.fromkeys(['avg','min','max'],math.nan)
  else:
    dict_numbers["avg"]=sum(numbers)/len(numbers)
    dict_numbers["min"]=min(numbers)
    dict_numbers["max"]=max(numbers)
  return dict_numbers
