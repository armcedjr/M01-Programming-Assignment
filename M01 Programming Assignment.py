# -*- coding: utf-8 -*-
"""
Armando Cedano
M01 Programming Assignment
This code is the answers to the 3.1 to 3.6 Things To Do questions.
"""

# 3.1
# How many seconds are in an hour?
seconds_in_minute = 60
minutes_in_hour = 60
seconds_in_hour = seconds_in_minute * minutes_in_hour
seconds_in_hour

# 3.2
# Assign the result from the previous task (seconds in an hour) to a variable called seconds_per_hour.
seconds_per_hour = seconds_in_hour
seconds_per_hour

# 3.3
# How many seconds are in a day? Use your seconds_per_hour variable.
hours_in_day = 24
seconds_per_day = seconds_per_hour * hours_in_day
seconds_per_day

# 3.4
# Calculate seconds per day again, but this time save the result in a variable called seconds_per_day.
seconds_per_day = seconds_per_hour * 24
seconds_per_day

# 3.5
# Divide seconds_per_day by seconds_per_hour. Use floating-point (/) division.
seconds_per_day / seconds_per_hour

# 3.6
# Divide seconds_per_day by seconds_per_hour, using integer (//) division. 
# Did this number agree with the floating-point value from the previous question, aside from the final .0?
seconds_per_day // seconds_per_hour
