activate_this = '/var/www/tylerkontra.com/bin/activate_this.py'
with open(activate_this) as file_:
	exec(file_.read(), dict(__file__=activate_this))

import sys
sys.path.insert(0, '/var/www/tylerkontra.com')



from control import app as application
