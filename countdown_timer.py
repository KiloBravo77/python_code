import time

timer_max = int(input("Set timer: "))

for x in range(timer_max):
	print(str(timer_max - x))
	time.sleep(1)

print("TIME IS UP!!!!!!!!!!!!!!!")

'''
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("BOOOOOOOOOOOM!!!!!!!!!!!!!!!")
'''