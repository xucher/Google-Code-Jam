_dir = "./Google Code Jam 2017/Qualification Round/Oversized Pancake Flipper/"

def flip(s = ''):
    if s == '+':
        return '-'
    else:
        return '+'

t, lines, result = 0, [], []
with open(_dir + "A-large-practice.in") as f:
    t = int(f.readline())
    lines = f.readlines()

for line in lines:
    s, k = line.split(' ')
    s, k= list(s), int(k)
    i, minTime = 0, 0
    while i < len(s) - k + 1:
        if s[i] == '-':
            minTime += 1
            for j in range(1, k):
                s[i+j] = flip(s[i+j])
        i += 1
    for j in range(k-1):
        if s[i+j] == '-':
            result.append('IMPOSSIBLE')
            break
        if j == k-2 and s[i+j] == '+':
            result.append(minTime)

with open(_dir + "result-large.txt", "w") as f:
    for i in range(len(result)):
        f.write("Case #" + str(i+1) + ": " + str(result[i]) + "\n")

            