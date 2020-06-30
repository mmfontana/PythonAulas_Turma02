from datetime import *
from dateutil.relativedelta import *
import calendar

agora = datetime.now()

print(agora)

hoje = date.today()

print(hoje)

proximo_mes = agora + relativedelta(months=+2, weeks=+1, hours=+1)

print(proximo_mes)

proximo_sexta = hoje + relativedelta(weekday=FR)

print(proximo_sexta)