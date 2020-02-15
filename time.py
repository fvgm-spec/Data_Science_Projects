from datetime import datetime, timedelta
import time
h = datetime.now() + timedelta(minutes=525)
n = '{:%H:%M}'.format(h)

print("Hoy la hora de salida es a las:",n)

