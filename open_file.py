fname = input('Enter ther file name: ')
try:
    fhand = open(fname)
except:
    print('File can not be opened: ', fname)
    quit()
    
count = 0
for line in fhand:
    smallcap = line.lower()
    if smallcap.startswith('subject: '):
        count = count + 1
   
print('There were', str(count), 'subject lines in',)