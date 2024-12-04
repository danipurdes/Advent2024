import re

input_lines = []
with open('input2', encoding="utf-8") as f:
    for line in f:
        input_lines.append(line)



mul_pattern = "mul\\(\\d*,\\d*\\)"
mul_commands = []
for input_line in input_lines:
    commands_found = re.findall(mul_pattern, input_line)
    for command_found in commands_found:
        mul_commands.append(command_found)

clean_mul_commands = []
for mul_command in mul_commands:
    clean_mul_command = mul_command.replace("mul(", '')
    clean_mul_command = clean_mul_command.replace(')', '')
    clean_mul_commands.append(clean_mul_command)

mul_pairs = []
for clean_mul_command in clean_mul_commands:
    mul_pairs.append(clean_mul_command.split(','))

sum = 0
for mul_pair in mul_pairs:
    if len(mul_pair) > 2 or len(mul_pair) == 0:
        print('mulpair size issue')
        continue
    if len(mul_pair[0]) > 3 or len(mul_pair[1]) > 3:
        print('num too big')
        continue
    print(int(mul_pair[0]) * int(mul_pair[1]))
    sum += int(mul_pair[0]) * int(mul_pair[1])

print(sum)