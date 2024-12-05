# Read in loc id's from file and split into lists.
with open('input.txt') as ifile:
    in_data = ifile.readlines()

left_list = []
right_list = []
for line in in_data:
    items = line.replace('\n', '').split(' ')
    left_list.append(int(items[0]))
    right_list.append(int(items[3]))

# Sort lists in ascending order.
left_list.sort()
right_list.sort()

# Match pairs and record distance between points.
total_distance = 0
for i in range(0, len(left_list)):
    if left_list[i] < right_list[i]:
        total_distance += right_list[i] - left_list[i]
    elif right_list[i] < left_list[i]:
        total_distance += left_list[i] - right_list[i]
    else:
        total_distance += 0

print(f'Total distance: {total_distance}')

# Calculate similarity score.
similarity = 0
for loc_id in left_list:
    occurances = right_list.count(loc_id)
    similarity += (loc_id * occurances)

print(f'Similarity Score: {similarity}')
