import sys
class tiempo:
    def  __init__(self, minuto=0, hora=0, dia=6, fecha=1, mes=1, year=2000):
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
    print("-----MODULOS TEMPORALES CREADOS------------------------------------------------ AJUSTANDO LOGICA TEMPORAL")
    
    def yearbisiesto(self):
        year= self.year
        if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False
    def finalmes(self):
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
        n_day= self.name_day()
        mes_en_curso = self.name_mes()
        return f"Fecha:{n_day} {self.fecha:02d} de {mes_en_curso} del {self.year} - Hora: {self.hora:02d}:{self.minuto:02d}"       
    print("------LOGICA AÑO BISIESTO COMPLETADA---------------------------------------------COMENZANDO LOGICA DE   MOVIMIENTO TEMPORAL")
    def avancetime_year(self):
               self.year+= 1
               
    def avancetime_mes(self):
               self.mes+= 1
               if self.mes > 12:
                   self.mes= 1
                   self.avancetime_year()
               if self.fecha > self.finalmes():
                    self.fecha= self.finalmes()
               
                   
    def avancetime_fecha(self):
            self.fecha+= 1
            if self.fecha > self.finalmes():
                self.fecha= 1
                self.avancetime_mes()
            self.dia+= 1
            if self.dia > 7:
                self.dia= 1
                    
    def avancetime_hora(self):
            self.hora+= 1
            if self.hora > 23:
                self.hora= 0
                self.avancetime_fecha()
            
    def avancetime_minuto(self):
             self.minuto+= 1
             if self.minuto > 59:
                self.minuto= 0
                self.avancetime_hora()
             
             
    def backtime_year(self):
                      self.year-= 1   
                      
    def backtime_mes(self):
            self.mes-= 1 
            if self.mes < 1:
               self.mes= 12
               self.backtime_year()
                     
    def backtime_fecha(self):
         self.fecha-= 1
         self.dia-= 1
         if self.fecha < 1:
             self.backtime_mes()
             self.fecha= self.finalmes()
         
         if self.dia < 1:
                self.dia= 7
                
            
    def backtime_hora(self):
             self.hora-= 1
             if self.hora < 0:
                self.hora= 23
                self.backtime_fecha()
                
    def backtime_minuto(self):
               self.minuto-=1
               if self.minuto < 0:
                   self.minuto= 59
                   self.backtime_hora()
                 
    def movementtime(self, movetime, valuetemp):
                if isinstance(valuetemp, int) and valuetemp>= 0:
                    for _ in range(valuetemp):
                        movetime()
                else:
                    raise ValueError("Valor de valuetemp para movetime debe ser entero positivo ")
    print("Lógica de movimiento temporal concluida estableciendo atributos temporales")    
    @property
    def avance_temp(self): return self._avanceminuto
         
    @avance_temp.setter
    def avance_temp(self,valuetemp):
               self.movementtime(self.avancetime_minuto, valuetemp)
               self._avanceminuto = valuetemp
              
    @property
    def avance_temphora(self): return self._avancehora
        
    @avance_temphora.setter
    def avance_temphora(self, valuetemp):
            self.movementtime(self.avancetime_hora, valuetemp)
            self._avancehora = valuetemp
              
    @property
    def avance_tempfecha(self): return self._avancefecha
        
    @avance_tempfecha.setter
    def avance_tempfecha(self, valuetemp):
            self.movementtime(self.avancetime_fecha, valuetemp)
            self._avancefecha = valuetemp
          
    @property
    def avance_tempmes(self): return self._avancemes
         
    @avance_tempmes.setter
    def avance_tempmes(self, valuetemp):
             self.movementtime(self.avancetime_mes, valuetemp)
             self._avancemes = valuetemp
        
    @property
    def avance_tempyear(self): return self._avanceyear
         
    @avance_tempyear.setter
    def avance_tempyear(self, valuetemp):
             self.movementtime(self.avancetime_year, valuetemp)
             self._avanceyear = valuetemp
        
    @property
    def back_time(self): return self._backtimeminuto
        
    @back_time.setter
    def back_time(self, valuetemp):
              self.movementtime(self.backtime_minuto, valuetemp)
              self._backtimeminuto = valuetemp
              
    @property
    def back_timehora(self): return self._backtimehora
        
    @back_timehora.setter
    def back_timehora(self, valuetemp):
              self.movementtime(self.backtime_hora, valuetemp)
              self._backtimehora = valuetemp
              
    @property
    def back_timefecha(self): return self._backtimefecha
        
    @back_timefecha.setter
    def back_timefecha(self, valuetemp):
              self.movementtime(self.backtime_fecha, valuetemp)
              self._backtimefecha = valuetemp
              
    @property
    def back_timemes(self): return self._backtimemes
        
    @back_timemes.setter
    def back_timemes(self, valuetemp):
              self.movementtime(self.backtime_mes, valuetemp)
              self._backtimemes = valuetemp                      
              
    @property
    def back_timeyear(self): return self._backtimeyear
        
    @back_timeyear.setter
    def back_timeyear(self, valuetemp):
              self.movementtime(self.backtime_year, valuetemp)
              self._backtimeyear = valuetemp     
     
    print("Class tiempo creada con exito")    
  
    
t = tiempo()
print(t)
        
        
   
        
               
                    
            
        