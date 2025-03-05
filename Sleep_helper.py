import threading
import time

class SleepHelper:
	def non_blocking_sleep( self, seconds):
		def sleep_thread():
			time.sleep( seconds )
		thread = threading.Thread( target = sleep_thread )
		thread.start()
