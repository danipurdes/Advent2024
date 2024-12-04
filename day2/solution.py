danger_threshold_max = 3
danger_threshold_min = 1

def is_report_safe(report=[]):
    if len(report) == 0:
        return 0
    if len(report) == 1:
        return 1
    
    first_delta = int(report[1]) - int(report[0])
    if first_delta == 0:
        return 0
    sort_direction = first_delta / abs(first_delta)

    dampener_count = 0
    # check each delta
    previous_level = -1
    for level in report:
        current_level = int(level)
        if previous_level > -1:
            delta = current_level - previous_level
            if abs(delta) > danger_threshold_max:
                dampener_count += 1
            elif abs(delta) < danger_threshold_min:
                dampener_count += 1
            elif delta / abs(delta) != sort_direction:
                dampener_count += 1
            if dampener_count > 1:
                return 0
            if delta != 0:
                print(delta / abs(delta))
            else:
                print(0)
        previous_level = current_level
    return 1

input_lines = []
with open('input2', encoding="utf-8") as f:
    for line in f:
        input_lines.append(line)

reports = []
for input_line in input_lines:
    reports.append(input_line.split(' '))

safe_reports = []
unsafe_reports = []
for report in reports:
    if is_report_safe(report):
        safe_reports.append(report)
    else:
        unsafe_reports.append(report)

for unsafe_report in unsafe_reports:
    for ignore_index in range(len(unsafe_report)):
        dampened_report = []
        if ignore_index == 0:
            dampened_report = unsafe_report[1:]
        elif ignore_index == len(unsafe_report) - 1:
            dampened_report = unsafe_report[0:ignore_index]
        else:
            dampened_report = unsafe_report[0:ignore_index] + unsafe_report[ignore_index+1:]
        if is_report_safe(dampened_report):
            safe_reports.append(unsafe_report)
            continue

print(len(safe_reports))