from os import listdir, mkdir, system
from os.path import isfile, isdir, join, exists

dir = 'training2017/'
#Create folder
csv = dir + 'csv'
if not exists(csv):
	mkdir(csv)

records = [f for f in listdir(dir) if isfile(join(dir, f)) if(f.find('.mat') != -1)]
#print records
records.sort() 
# print(records)
print(len(records))
for r in records:
	print(r[:-4])
	command = 'rdsamp -r ' + r + ' -c -f 0 -t 10 >' + r[:-4] +'.csv'
	print(command)
	system(command)

# r = 'training2017/A00001'
# command = 'rdsamp -r ' + r + ' -c -f 0 -t 10 >samples.csv'



print(command)
system(command)

# for r in records:
    # print r
	# command = 'rdsamp -r ' + r[:-4] + ' -c -H -f 0 -v >' + 'csv/' + r[:-4] + '.csv'
	# print(command)
	# system(command)

	