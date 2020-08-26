import sys
import string
import json
import numbers
import time

'''
payload_string should be a json with the following properties:
    * period    - int
    * factor    - float/double
    * data      - string (see example for the format - it should be the same format as when the observation is created)
it should terminate with EOF
'''
payload_string = sys.stdin.read()

filtered_string = ''.join(filter(lambda x: x in string.printable, payload_string))

try:
    payload = json.loads(filtered_string)
except:
    raise AssertionError('could not parse json payload')

if not payload['period']: raise AssertionError('period is not defined')
if not isinstance(payload['period'], numbers.Number): raise AssertionError('period is not a number')

if not payload['factor']: raise AssertionError('factor is not defined')
if not isinstance(payload['factor'], numbers.Number): raise AssertionError('factor is not a number')

if not payload['data']: raise AssertionError('data is not defined')
if not isinstance(payload['data'], str): raise AssertionError('data is not a string')

def parse_value(s):
    return int(s)

values = []
try:
    values = list(map(parse_value, payload['data'].split(' ')))
    #print('parsed', len(values), 'values')
except:
    raise AssertionError('failed to parse data into an array of integers')

# processing. haha!
time.sleep(3)

# output. result is a float/double which indicates the QT length in milliseconds
#print(7.777, sys.stdout)
print(7.777)
