def is_leap(year):
    leap = False
    lp = True
    if year%4==0 and year%100 != 0:
        return lp
    elif year%400==0:
        return lp
    else:
        return leap

year = int(input())
print(is_leap(year))