import sys
import time
from threading import Thread

display_delay = 3

class NotificationBox:
	def __init__(self):
		self.thread = DisplayNotif()
	def write(self, text, color):
		self.thread.addQueue(text, color)

class DisplayNotif(Thread):
	queue = []
	running = False
	def __init__(self):
		pass
		#super().__init__()

	def addQueue(self, text, color):
		self.queue.append(text)
		# If thread is not running, start it
		if not self.running:
			self.__init__()
			self.start()

	def run(self):
		# Set thread as runnning
		self.running = True
		# Run thread while queue is not empty
		while(len(self.queue)>0):
			print(self.queue.pop(0))
			time.sleep(display_delay)
		# When queue is empty set thread as not running
		self.running = False
		#raise SystemExit() # Don't work
		#self._stop() # Don't work

notif = NotificationBox()
notif.write('Hello',(50,50,50))
notif.write('Hello2',(50,50,50))

# Waiting for thread end
time.sleep(display_delay * 3)

# ↓ here : raise RuntimeError("threads can only be started once")
notif.write('Hello3',(50,50,50))