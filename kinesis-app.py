import random
import datetime
import time

for i in range(3):
    f = open("/tmp/kinesis-app.logs", "a")
    errors = "error "*random.randrange(8) + str(datetime.datetime.now())
    line = '{"id":' + str(random.randrange(100000)) + ',"message":"' + errors + '"}'
    f.write(f'{line}\n')
    print(line)
    f.close()
    time.sleep(5)
