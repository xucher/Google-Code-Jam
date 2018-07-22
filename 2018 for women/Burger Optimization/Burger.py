t, lines, result = 0, [], []
with open("A-large-practice.in") as f:
    t = int(f.readline())
    lines = f.readlines()

for i in range(t):
    min = 0
    for j, num in enumerate(sorted([int(t) for t in lines[2*i+1].split(' ')])):
        min += pow(num-j//2, 2)
    result.append(int(min))

with open("result-large1.txt", "w") as f:
    for i in range(len(result)):
        f.write("Case #" + str(i+1) + ": " + str(result[i]) + "\n")