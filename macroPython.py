from pynput.keyboard import Key, Controller

import time 
import random 
import threading

keyboard =Controller()

class comerThread(threading.Thread) :
	def run(self):
		while True:
			#COMER
			time.sleep(random.randrange(300))# 5 min
			keyboard.press('a')
			keyboard.release('a')
	def stop(self):
		self.running=False	

class arrowsThread(threading.Thread) :
	def run(self):
		while True:
			# HACER ARROWS
			time.sleep(random.triangular(360,450))#6 min
			keyboard.press('b')
			keyboard.release('b')
	def stop(self):
		self.running=False

class flechasThread(threading.Thread) :
	def run(self):
		while True:
			#CAMBIAR DE FLECHAS
			time.sleep(random.randrange(540))#9 min
			keyboard.press('c')
			keyboard.release('c')
	def stop(self):
		self.running=False

class retargetThread(threading.Thread):
	def run(self):
		while True:
			time.sleep(random.randrange(1200))#20 min
			keyboard.press('h')
			keyboard.release('h')
			time.sleep(10)
			keyboard.press('v')
			keyboard.release('v')


thread1=comerThread()
thread2=arrowsThread()
thread3=flechasThread()
thread4=retargetThread()



thread1.start()
thread2.start()
thread3.start()
thread4.start()


