"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_acp.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
from math import ceil


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#

MAX_TIMINGS = { 0: 34, 200: 32, 400: 30, 600: 28 }

MIN_TIMINGS =  { 0: 15, 400: 15, 600: 11.428 }



def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
   """
   Args:
      control_dist_km:  number, control distance in kilometers
      brevet_dist_km: number, nominal distance of the brevet
         in kilometers, which must be one of 200, 300, 400, 600,
         or 1000 (the only official ACP brevet distances)
      brevet_start_time:  An arrow object
   Returns:
      An arrow object indicating the control open time.
      This will be in the same time zone as the brevet start time.
   """
   start_time = arrow.get(brevet_start_time)
   total_time = 0
   # account for special cases
   if control_dist_km < 0: # control distance is negative: raise error
      raise Exception
   elif control_dist_km == 0: # control distance is 0: starts at start time
      return start_time
   elif control_dist_km > brevet_dist_km: # gate beyond end of race starts and closes with end of race
      control_dist_km = brevet_dist_km

   maxs = MAX_TIMINGS.keys() # list of distance intervals
   start = 0
   remaining_dist = control_dist_km
   for i in range(len(maxs)):
      if maxs[i] > control_dist_km:
         break
      else:
         start = i
   for j in range(start, 0, -1):
      # subtract off the distance interval differences, calculate the times per difference
      # then add them all together for the total offset from the start time in minutes
      if remaining_dist == 0:
         break
      diff = remaining_dist - maxs[j]
      total_time += ceil(diff/MAX_TIMINGS[j])
      remaining_dist -= diff 
      
   return start_time.shift(minutes=total_time)


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
   """
   Args:
      control_dist_km:  number, control distance in kilometers
         brevet_dist_km: number, nominal distance of the brevet
         in kilometers, which must be one of 200, 300, 400, 600, or 1000
         (the only official ACP brevet distances)
      brevet_start_time:  An arrow object
   Returns:
      An arrow object indicating the control close time.
      This will be in the same time zone as the brevet start time.
   """
   start_time = arrow.get(brevet_start_time)
   total_time = 0
   # account for special cases
   if control_dist_km < 0: # control distance is negative: raise error
      raise Exception
   if control_dist_km == 0: # control distance is 0: closes 1 hr after start by convention
      total_time = 60      
      return start_time.shift(minutes=total_time)
   elif control_dist_km <= 60: # special timing for gate closure when gate within 60km of start
      total_time = ceil(control_dist_km/20 + 60)
      return start_time.shift(minutes=total_time)
   if control_dist_km > brevet_dist_km: # gate beyond end of race starts and closes with end of race
      control_dist_km = brevet_dist_km

   mins = MIN_TIMINGS.keys()
   start = 0
   remaining_dist = control_dist_km
   for i in range(len(mins)):
      if mins[i] > control_dist_km:
         break
      else:
         start = i
   for j in range(start, 0, -1):
      if remaining_dist == 0:
         break
      diff = remaining_dist - mins[j]
      total_time += ceil(diff/MAX_TIMINGS[j])
      remaining_dist -= diff

   return start_time.shift(minutes=total_time)
