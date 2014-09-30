import time
import threading

def passmethod():
	return False

class event():
	def __init__( self, when = passmethod, what = passmethod):
		self.when = when
		self.what = what

class  monitor():
	def __init__( self ):
		self.events = []
		self.poll_interval = 1 
	def install( self ):
		t = threading.Thread(target=self.periodic_reload)
		#t.setDaemon(True)
		t.start()
	def whatch( self, when, what):
		self.events += [event(when, what)]
	def periodic_reload( self ):
		while True:
			for e in self.events:
				if e.when():
					e.what()
			print "Hello!!!"
			time.sleep(self.poll_interval)