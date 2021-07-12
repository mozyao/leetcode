

from heapq import heappush, heappop
def order_log(logs):
	letter, digit , heap = [],[],[]
	for log in logs:
		#log is : "2 y xyr fc"
		tail = log.split(' ',1)[1]
		# split once, we get ["2","y xyr fc"]
		# so the tail is "y xyr fc"
		
		if tail[0].isalpha():
			heappush(heap,(tail,log))
		else:
			digit.append(log)
	while heap:
		letter.append(heappop(heap)[1])
	return letter + digit




def order_log2(logs):
	letlogs = []
	diglogs = []	
	for log in logs:
		sl = log.split(" ")
		if sl[1].isnumeric():
			diglogs.append((sl[0], " ".join(sl[1:])))
		else:
			letlogs.append((sl[0], " ".join(sl[1:])))
	
	# https://stackoverflow.com/a/46851604/1392291 
	letlogs.sort(key= lambda x: (x[1],x[0]))
	res = []
	for l in letlogs:
		res.append(" ".join(l))
	for l in diglogs:
		res.append(" ".join(l))
	
	return res

if __name__ == "__main__":
	x = order_log2(["2 y xyr fc", "m azv x f", "7e apw c y", "8 hyyq z p", "c otdk cl", "8 ksif m u"])
	print(x)















