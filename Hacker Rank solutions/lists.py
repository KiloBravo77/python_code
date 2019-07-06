n = int(input())
cmd_list = []

for _ in range(n):
	cmd_line = input().split()
	run_command = ", "
	cmd = cmd_line[0]
	args = cmd_line[1:]

	if cmd == "print":
		print(cmd_list)
	else:
		run_command = cmd + "(" + run_command.join(args) + ")"
		eval("cmd_list." + run_command)