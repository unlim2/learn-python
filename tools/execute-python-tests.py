"""

Execute unit tests for python tasks from exercism.org

Command to use it with notepad++:
python -i c:\tmp\execute-python-tests.py $(FULL_CURRENT_PATH)

"""

import sys
import os
import re
import configparser
import pytest

directory = os.path.sep.join(sys.argv[1].split(os.path.sep)[:-1])
script = sys.argv[1].split(os.path.sep)[-1]
tests_script = re.sub(r'.py$', '_test.py', script)

print(f"directory: {directory}")
print(f"script: {script}")
print(f"tests script: {tests_script}")

os.chdir(directory)

pytest_config_file = 'pytest.ini'

has_pytest_config = os.path.exists(pytest_config_file)

config = configparser.ConfigParser()
config.read(pytest_config_file)

if 'pytest' in config:
    if 'markers' in config['pytest']:
        lines = config['pytest']['markers'].split("\n")
        if not next((s for s in lines if re.search(r'^\s*task\s*:?', s)), None):
            lines.append("task")
        config['pytest']['markers'] = "\n".join(lines)
    else:
        config['pytest']['markers'] = 'task'
else:
    config['pytest']={'markers': 'task'}

with open(pytest_config_file, 'w') as file:
    config.write(file)

if os.path.exists(tests_script):
    pytest.main([ "-v" , tests_script ])
else:
    pytest.main([ "-v", "." ])

if not has_pytest_config:
    os.remove(pytest_config_file)
