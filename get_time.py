import time

t=time.localtime()
t_tuple = (t.tm_year, t.tm_mon, t.tm_mday,t.tm_wday ,t.tm_hour, t.tm_min, t.tm_sec, 0)
print(t_tuple)