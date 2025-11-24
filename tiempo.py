import sys

class tiempo:
    """
    A class to represent and manipulate dates and times.

    This class handles time progression and regression, including logic for leap years,
    days of the week, and month lengths. It allows for modifying time components
    individually or advancing/reversing them by specific amounts.
    """

    def  __init__(self, minuto=0, hora=0, dia=6, fecha=1, mes=1, year=2000):
        """
        Initializes the tiempo object with a specific date and time.

        Args:
            minuto (int): The minute (0-59). Defaults to 0.
            hora (int): The hour (0-23). Defaults to 0.
            dia (int): The day of the week (1-7, where 1 is Monday). Defaults to 6 (Saturday).
            fecha (int): The day of the month. Defaults to 1.
            mes (int): The month (1-12). Defaults to 1.
            year (int): The year (2000-2099). Defaults to 2000.

        Raises:
            ValueError: If any of the provided values are out of their valid ranges.
        """
        if not(0<=minuto<=59):
            raise ValueError("valor minuto invalido")
        if not(0<=hora<=23):
            raise ValueError("valor hora invalido")
        if not(1<=dia<=7):
            raise ValueError("valor dia invalido")
        if not (1<= mes <=12):
            raise ValueError("valor mes invalido")
        if not(2000<=year<=2099):
            raise ValueError("Has viajado al pasado o al futuro saliendo del siglo XXI intenta con otro año")
        self.minuto= minuto
        self.hora= hora
        self.fecha= fecha
        self.mes= mes
        self.year= year
        self.dia= dia
        maxday= self.finalmes()
        if not(1<=fecha<= maxday):
            raise ValueError(f"valor fecha invalido en el mes de {mes} (valormax: {maxday})")
        
        self._avanceminuto= 0
        self._avancehora= 0
        self._avancefecha= 0
        self._avancemes= 0
        self._avanceyear= 0
        self._backtimeminuto= 0
        self._backtimehora= 0
        self._backtimefecha= 0
        self._backtimemes= 0
        self._backtimeyear= 0
    
    def yearbisiesto(self):
        """
        Checks if the current year is a leap year.

        Returns:
            bool: True if the year is a leap year, False otherwise.
        """
        year= self.year
        if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False

    def finalmes(self):
        """
        Determines the number of days in the current month.

        Returns:
            int: The number of days in the current month (28, 29, 30, or 31).
        """
        if self.mes in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.mes in [4, 6, 9, 11]:
            return 30
        elif self.mes == 2:
            if self.yearbisiesto():
                return 29
            else:
                 return 28

    def name_day(self):
        """
        Gets the name of the current day of the week.

        Returns:
            str: The name of the day (e.g., "Lunes", "Martes").
        """
        day = {
            1: "Lunes",
            2: "Martes",
            3: "Miércoles",
            4: "Jueves",
            5: "Viernes",
            6: "Sábado",
            7: "Domingo"
        }
        return day.get(self.dia)

    def name_mes(self):
        """
        Gets the name of the current month.

        Returns:
            str: The name of the month (e.g., "Enero", "Febrero").
        """
        n_mes = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
        }

        return n_mes.get(self.mes)

    def __str__(self):
        """
        Returns a string representation of the current date and time.

        Returns:
            str: A formatted string showing date and time.
        """
        n_day= self.name_day()
        mes_en_curso = self.name_mes()
        return f"Fecha:{n_day} {self.fecha:02d} de {mes_en_curso} del {self.year} - Hora: {self.hora:02d}:{self.minuto:02d}"       

    def avancetime_year(self):
        """
        Advances the time by one year.
        """
        self.year+= 1
               
    def avancetime_mes(self):
        """
        Advances the time by one month.

        Adjusts the year if the month exceeds December.
        Also clamps the day of the month if the new month has fewer days.
        """
        self.mes+= 1
        if self.mes > 12:
            self.mes= 1
            self.avancetime_year()
        if self.fecha > self.finalmes():
            self.fecha= self.finalmes()
               
                   
    def avancetime_fecha(self):
        """
        Advances the time by one day.

        Adjusts month and year if necessary, and updates the day of the week.
        """
        self.fecha+= 1
        if self.fecha > self.finalmes():
            self.fecha= 1
            self.avancetime_mes()
        self.dia+= 1
        if self.dia > 7:
            self.dia= 1
                    
    def avancetime_hora(self):
        """
        Advances the time by one hour.

        Adjusts the date if the hour exceeds 23.
        """
        self.hora+= 1
        if self.hora > 23:
            self.hora= 0
            self.avancetime_fecha()
            
    def avancetime_minuto(self):
        """
        Advances the time by one minute.

        Adjusts the hour if the minute exceeds 59.
        """
        self.minuto+= 1
        if self.minuto > 59:
            self.minuto= 0
            self.avancetime_hora()
             
             
    def backtime_year(self):
        """
        Moves the time back by one year.
        """
        self.year-= 1
                      
    def backtime_mes(self):
        """
        Moves the time back by one month.

        Adjusts the year if the month goes below January.
        """
        self.mes-= 1
        if self.mes < 1:
            self.mes= 12
            self.backtime_year()
                     
    def backtime_fecha(self):
        """
        Moves the time back by one day.

        Adjusts the month and year if necessary, and updates the day of the week.
        """
        self.fecha-= 1
        self.dia-= 1
        if self.fecha < 1:
            self.backtime_mes()
            self.fecha= self.finalmes()

        if self.dia < 1:
            self.dia= 7
                
            
    def backtime_hora(self):
        """
        Moves the time back by one hour.

        Adjusts the date if the hour goes below 0.
        """
        self.hora-= 1
        if self.hora < 0:
            self.hora= 23
            self.backtime_fecha()
                
    def backtime_minuto(self):
        """
        Moves the time back by one minute.

        Adjusts the hour if the minute goes below 0.
        """
        self.minuto-=1
        if self.minuto < 0:
            self.minuto= 59
            self.backtime_hora()
                 
    def movementtime(self, movetime, valuetemp):
        """
        Applies a time movement function multiple times.

        Args:
            movetime (callable): The function to call for each step of movement.
            valuetemp (int): The number of times to call the function.

        Raises:
            ValueError: If valuetemp is not a non-negative integer.
        """
        if isinstance(valuetemp, int) and valuetemp>= 0:
            for _ in range(valuetemp):
                movetime()
        else:
            raise ValueError("Valor de valuetemp para movetime debe ser entero positivo ")

    @property
    def avance_temp(self):
        """
        int: Property to get or set the number of minutes to advance.
        Setting this property advances the time by the given minutes.
        """
        return self._avanceminuto
         
    @avance_temp.setter
    def avance_temp(self,valuetemp):
        self.movementtime(self.avancetime_minuto, valuetemp)
        self._avanceminuto = valuetemp
              
    @property
    def avance_temphora(self):
        """
        int: Property to get or set the number of hours to advance.
        Setting this property advances the time by the given hours.
        """
        return self._avancehora
        
    @avance_temphora.setter
    def avance_temphora(self, valuetemp):
        self.movementtime(self.avancetime_hora, valuetemp)
        self._avancehora = valuetemp
              
    @property
    def avance_tempfecha(self):
        """
        int: Property to get or set the number of days to advance.
        Setting this property advances the time by the given days.
        """
        return self._avancefecha
        
    @avance_tempfecha.setter
    def avance_tempfecha(self, valuetemp):
        self.movementtime(self.avancetime_fecha, valuetemp)
        self._avancefecha = valuetemp
          
    @property
    def avance_tempmes(self):
        """
        int: Property to get or set the number of months to advance.
        Setting this property advances the time by the given months.
        """
        return self._avancemes
         
    @avance_tempmes.setter
    def avance_tempmes(self, valuetemp):
        self.movementtime(self.avancetime_mes, valuetemp)
        self._avancemes = valuetemp
        
    @property
    def avance_tempyear(self):
        """
        int: Property to get or set the number of years to advance.
        Setting this property advances the time by the given years.
        """
        return self._avanceyear
         
    @avance_tempyear.setter
    def avance_tempyear(self, valuetemp):
        self.movementtime(self.avancetime_year, valuetemp)
        self._avanceyear = valuetemp
        
    @property
    def back_time(self):
        """
        int: Property to get or set the number of minutes to move back.
        Setting this property moves the time back by the given minutes.
        """
        return self._backtimeminuto
        
    @back_time.setter
    def back_time(self, valuetemp):
        self.movementtime(self.backtime_minuto, valuetemp)
        self._backtimeminuto = valuetemp
              
    @property
    def back_timehora(self):
        """
        int: Property to get or set the number of hours to move back.
        Setting this property moves the time back by the given hours.
        """
        return self._backtimehora
        
    @back_timehora.setter
    def back_timehora(self, valuetemp):
        self.movementtime(self.backtime_hora, valuetemp)
        self._backtimehora = valuetemp
              
    @property
    def back_timefecha(self):
        """
        int: Property to get or set the number of days to move back.
        Setting this property moves the time back by the given days.
        """
        return self._backtimefecha
        
    @back_timefecha.setter
    def back_timefecha(self, valuetemp):
        self.movementtime(self.backtime_fecha, valuetemp)
        self._backtimefecha = valuetemp
              
    @property
    def back_timemes(self):
        """
        int: Property to get or set the number of months to move back.
        Setting this property moves the time back by the given months.
        """
        return self._backtimemes
        
    @back_timemes.setter
    def back_timemes(self, valuetemp):
        self.movementtime(self.backtime_mes, valuetemp)
        self._backtimemes = valuetemp
              
    @property
    def back_timeyear(self):
        """
        int: Property to get or set the number of years to move back.
        Setting this property moves the time back by the given years.
        """
        return self._backtimeyear
        
    @back_timeyear.setter
    def back_timeyear(self, valuetemp):
        self.movementtime(self.backtime_year, valuetemp)
        self._backtimeyear = valuetemp

if __name__ == "__main__":
    t = tiempo()
    print(t)
