# Read in loc id's from file and split into lists.
with open('input.txt') as ifile:
    in_data = ifile.readlines()

reports = []
for line in in_data:
    reports.append(list(map(int, line.replace('\n', '').split(' '))))

# Check reports for safety
for report in reports:
    report_status = 0
    slope = 1
    for idx in range(1, len(report)):
        slope = 1
        if abs(report[idx] - report[idx-1]) > 3:
            report_status = 1


