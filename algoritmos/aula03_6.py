import time

data = time.localtime()
#time.struct_time(tm_year=2025, tm_mon=4, tm_mday=8, tm_hour=22, tm_min=11, tm_sec=46, tm_wday=1, tm_yday=98, tm_isdst=0)

print(f"Data atual: {data.tm_mday}/{data.tm_mon}/{data.tm_year}")
print(f"Horário: {data.tm_hour}:{data.tm_min}:{data.tm_sec}")