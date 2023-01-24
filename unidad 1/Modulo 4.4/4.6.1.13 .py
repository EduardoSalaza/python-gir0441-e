'''
        Autor: jesus eduardo salazar
        Fecha: 24-ene-23
'''


import calendar 

class MyCalendar(calendar.Calendar):
    def count_weekday_in_year(self, year, weekday):
        current_mounth = 1
        number_of_days = 0
        while (current_mounth <=12):
            for data in self.moutndays2calendar(year, current_month):
                if data[weekday][0] != 0:
                    number_of_days = number_of_days + 1
                    
            current_month = current_month + 1
        return number_of_days
        
my_calendar = MyCalendar()
number_of_days = my_calendar.count_weekday_in_year(2000, calendar.SATURDAY)

print (number_of_days)