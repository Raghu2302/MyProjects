file = open('C:/Users/Welcome/Downloads/radishsurvey.txt', 'r')
clean_data = []
for line in file:
    name,rad = line.strip().split(' - ')
    clean_data.append((name.strip().lower().replace('  ',' '),rad.strip().lower().replace('  ',' ')))
print(clean_data)
print(len(clean_data))
'''Now, to remove the duplicate values we will convert the list into dictionaries, as we know that
dictionaries will not hold duplicate key values'''
data_dict=dict(clean_data)
#check length of the data to confirm
print(len(data_dict))
#print(data_dict)
vote_count = {}
# Loop over the items in the dictionary
for key, value in data_dict.items():
    # If the current value is not already in the frequency dictionary,
    # add it with a frequency of 1
    if value not in vote_count:
        vote_count[value] = 1
    # If the current value is already in the frequency dictionary,
    # increment its frequency by 1
    else:
        vote_count[value] += 1
print(vote_count)
# Find the maximum frequency in the frequency dictionary
max_freq = max(vote_count.values())
min_freq = min(vote_count.values())

# Find the value(s) with the maximum frequency
#max_freq_values = [key for key, value in vote_count.items() if value == max_freq]
max_freq_values = max(vote_count,key=vote_count.get)
min_freq_values = min(vote_count,key=vote_count.get)
#min_freq_values = [key for key, value in vote_count.items() if value == min_freq]


print("The maximum times voted radish type is:", max_freq_values)
print("It has been voted", max_freq, "times.")

print("The minimum times voted radish type is:", min_freq_values)
print("It has been voted", min_freq, "times.")