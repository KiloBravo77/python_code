def wheeloffish():
	print("Spin the wheel of fish!")
	print("ooooo red snappah. vetty tasty!")
	print("Do you want the fish or the box?")

	answer = raw_input("Do you want the fish or the box?").lower()

	if answer == "box":
		print("YOU TOOK THE BOX! WHAT'S IN THE BOX???")
		print("..........")
		print("NOTHING! STUPID")
	else:
		print("Excellent choice")

wheeloffish()