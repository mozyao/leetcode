def isRobotBounded(instructions: str) -> bool:
	ans = False
	x = 0
	y = 0
	head = 0
	# "N"-0, "W"-1, "S"-2, "E"-3
	direction_list = ["N","E","S","W"]
	time=1
	step=1
	check =0

	d = {
		"N":[0,1],
		"S":[0,-1],
		"W":[-1,0],
		"E":[1,0]
	}
		   
	for ins in instructions:
		print("\nstep:  ", step, "-----\n")
		
		print("\nNow we at","(",x,",",y,")", "------\n")
		print("\n head is",direction_list[head % 4] , "and time is", time, "\n")
		if x==0 and y==0 and direction_list[head%4] =="N" and time != 1 :
			check +=1
	
			print("\n check is ",check,"---------\n")

		
		time+=1
		step +=1
		
		print("\nNow we accept: ", ins, "------\n")
		if ins == "L":
			head = head -1
			print("\nnow we head at",direction_list[head % 4], "------\n")
			print("\nNow we at","(",x,",",y,")", "------\n")
			print("\nnow check time is ",check, "------\n")
		elif ins == "R":
			head = head +1
			print("\nnow we head at",direction_list[head % 4], "------\n")
			print("\nNow we at","(",x,",",y,")", "------\n")
			print("\nnow check time is ",check, "------\n")
		elif ins == "G":
			x = x+ d.get(direction_list[head % 4])[0]
			y= y + d.get(direction_list[head % 4])[1]
			print("\nnow we head at",direction_list[head % 4], "------\n")
			print("\nNow we at","(",x,",",y,")", "------\n")
			print("\nnow check time is ",check, "------\n")
	


	print("\n =========================\n")

	if x==0 and y==0 and direction_list[head%4] =="N" and time != 1 and check>=2:
		ans =True
	return ans



def mybound(ins: str) -> bool:
	myIns = ""

	for copy in range(1,50):
		myIns = copy*ins
		if isRobotBounded(myIns) == True:
			return True

	return False







def main():
	ans = mybound("GLGLGGLGL")
	print("myans is : ",ans)

if __name__ == "__main__":
    main()




    



