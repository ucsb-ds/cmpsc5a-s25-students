# Open the file tests.json and read the contents into the variable tests
import json
with open('tests.json', 'r') as f:
    tests = json.load(f)
    
# Iterate over the keys in the tests['otter']['tests'], and for each key, 
# create a new file in the tests directory with the name of the key and the extension .py.
# Inside each file, write this line of code: "OK_FORMAT = True" followed by a blank line,
# and then write an asssignment statement, with the variable name test equal to the value of the key in the tests['otter']['tests'] dictionary.
for key in tests['otter']['tests']:
    with open(f'{key}.py', 'w') as f:
        f.write('OK_FORMAT = True\n\n')
        f.write(f'test = {json.dumps(tests["otter"]["tests"][key], indent=4)}\n')