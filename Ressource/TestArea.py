from random import *

critical = {10:1.5}
critical = critical.get(randint(1,10),1)

print(critical)