
'''
        Autor: jesus eduardo salazar
        Fecha: 24-ene-23
'''

def isYearLeap (year):

def daysInMonth(year, month):

def dayOfYear(year, month, day):
    
    if year < 1582:
        return None
    if month > 12 or month < 1:
        return None 
    if day > 31 or day <1:
        return None 
        
        
    totalDays = day 
    month = month - 1
    while month > 0:
        totalDays += daysInMonth(year, month)
        month -= 1
        
        return totalDays 
        
print(dayOfYear(2000, 11, 31))