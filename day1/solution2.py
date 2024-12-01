input_lines = []
with open('input', encoding="utf-8") as f:
    for line in f:
        input_lines.append(line)

list_a = []
list_b = []
for input_line in input_lines:
    inputs = input_line.split('   ', 1)
    list_a.append(int(inputs[0]))
    list_b.append(int(inputs[1]))

list_a.sort()
list_b.sort()

total_similarity = 0
for i in range(len(list_a)):
    total_similarity += list_a[i] * list_b.count(list_a[i])
print(total_similarity)