

measurements = []

f = open("text.txt")
for x in f:
  measurements.append(int(x))
  

num_decrease = 0

for num in range(len(measurements)):
  if num + 1 < len(measurements):

    if (measurements[num] > measurements[num + 1]):
      num_decrease += 1


num_increase = len(measurements) - num_decrease - 1
print(num_increase)
