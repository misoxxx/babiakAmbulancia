import string
import random
def id_generator(size=15, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
num_entries = 5000
num_str = 6
with open('databaza5000','w+') as f:
    f.write('{')
    for i in range(0,num_entries):
        f.write('[')
        f.write(str(i))
        for i in range(0,num_str):
            f.write('|'+ id_generator())
        f.write(']')
    f.write('}')

    
