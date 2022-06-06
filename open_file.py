# fname = input('Enter ther file name: ')
# try:
#     fhand = open(fname)
# except:
#     print('File can not be opened: ', fname)
#     quit()
    
# count = 0
# for line in fhand:
#     smallcap = line.lower()
#     if smallcap.startswith('subject: '):
#         count = count + 1
   
# print('There were', str(count), 'subject lines in',)

# file = open('mbox.txt', 'w')
# # count = 0
# # for lines in file:
# #     lines = lines.rstrip()
# #     lower = lines.lower()
# #     if lower.startswith('from'):
# #         print(lines[10:20])
# line1 = 'Hello, how are you\n'
# linea2 = 'I am good and you?\n'
# file.write(line1)
# file.write(linea2)
# new_file = open('mbox.txt')
# new_file.close()
# print(new_file)

s = '1 2\t 3\n 4'
print(repr(s))