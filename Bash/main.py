import Bash.bash as bash
import os


os.chdir('Script')
allScript = os.listdir()

for script in allScript:
    exec(open(script).read())

while True:
    bash.run()