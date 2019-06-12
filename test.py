from tavern.core import run
from subprocess import Popen, PIPE

process = Popen(['python','server.py'],stdout=PIPE,stderr=PIPE)
print('spawned server')

success = run("test.tavern.yaml",{})