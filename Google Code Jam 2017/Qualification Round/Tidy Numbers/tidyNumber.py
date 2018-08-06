_dir = "./Google Code Jam 2017/Qualification Round/Tidy Numbers/"

t, lines, result = 0, [], []
with open(_dir + "B-small-practice.in") as f:
    t = int(f.readline())
    lines = f.readlines()

for line in lines:
    for i in range(len(line)-2):
        if (line[i] > line[i+1]):
            line = line[0:i] + str(int(line[i])-1) + '9'*(len(line)-i-2)
    result.append(''.join(line))

with open(_dir + "result-small.txt", "w") as f:
    for i in range(len(result)):
        f.write("Case #" + str(i+1) + ": " + str(int(result[i])) + "\n")

# error when 111110