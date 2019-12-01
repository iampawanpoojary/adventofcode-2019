input= open("input.txt")
li = [(math.floor(int(mass)/3)) for mass in input]
output = sum(li) - (2 * len(li))
