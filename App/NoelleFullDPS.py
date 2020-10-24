import datetime 
def redondear_horas(tiempo):
    tiempo = tiempo.replace(second = 0)
    minuto = tiempo.minute
    h = tiempo.hour
    if minuto <= 15:
        tiempo = tiempo.replace(minute= 0)
    elif minuto > 15 and minuto <= 45:
        tiempo = tiempo.replace(minute= 30)
    elif minuto > 45 and minuto <= 59:
        tiempo = tiempo.replace(hour= h+1 ) 
        tiempo = tiempo.replace(minute= 0)
    return tiempo

Mona = "2010-01-02 06:46:59"
Mona = datetime.datetime.strptime(Mona, "%Y-%m-%d %H:%M:%S")
Mona = Mona.time()
Mona = redondear_horas(Mona)



print(Mona)