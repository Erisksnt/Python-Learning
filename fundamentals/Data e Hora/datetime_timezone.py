#biblioteca para importar timezone
import pytz
from datetime import datetime

#criando datetime com zona
date = datetime.now(pytz.timezone("Europe/Dublin"))
print(date)