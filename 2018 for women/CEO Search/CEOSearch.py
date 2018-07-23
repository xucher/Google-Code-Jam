_dir = "./2018 for women/CEO Search/"
t, lines, result = 0, [], []
with open(_dir + "B-large-practice.in") as f:
    t = int(f.readline())
    lines = f.readlines()

i = 0
while i < len(lines):
    datas = []
    for j in range(int(lines[i])):
        i += 1
        datas.append([int(k) for k in lines[i].split(' ')])
    datas.sort(key=lambda k: k[1])

    num = datas[0][0]
    for j in range(1, len(datas)):
        if datas[j][0] * datas[j][1] >= num:
            num = datas[j][0]
        else:
            num = datas[j][0] + num - datas[j][0] * datas[j][1]
    if datas[j][1] + 1 >= num:
        result.append(datas[j][1] + 1)
    else:
        result.append(num)

    i += 1

with open(_dir + "large-small.txt", "w") as f:
    for i in range(len(result)):
        f.write("Case #" + str(i+1) + ": " + str(result[i]) + "\n")