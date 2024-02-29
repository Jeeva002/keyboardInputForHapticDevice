from pynput.keyboard import Key, Listener
from multiprocessing import Process
def show(key):

	print('\nYou Entered {0}'.format( key))

	if key == Key.delete:
		# Stop listener
		return False
def main():
	while True:
		a=10
		#print("true")
# Collect all event until released
t1=Process(target=main)
t1.start()
with Listener(on_press = show) as listener: 

	 listener.join()
