# Without context manager:
# data = open('example1.txt')
# for i in data:
#     print(data.read())
#
# data.close()
#
#

# With context manager -- read
# with open('example1.txt') as file:
#     for s in file:
#         print(s)

# ... --write
# with open('example2.txt', 'w') as file:
#     data = ['string one', 'string two', 'string three']
#     for s in data:
#         file.write(f'{s}\n\n')


# ... --write only to new file (if file exists -- error)
# with open('example3.txt', 'x') as file:
#     data = ['string one', 'string two', 'string three']
#     for s in data:
#         file.write(f'{s}\n!')

# ... --write to existing file (to the end)
# with open('example2.txt', 'a') as file:
#     data = ['string four', 'string five']
#     for s in data:
#         file.write(f'{s}\n\n')

# ... --read in binary mode
# with open('example3.txt', 'rb') as file:
#     for s in file:
#         print(s)

# ... --write in binary mode
# with open('example3.txt', 'wb') as file:
#     data = ['string1', 'string2']
#     for s in data:
#         file.write(b'{}')

##  read file without context manager
# file = open('example2.txt')
##  print whole file
# print(file.read())
## print file with limit (5) of symbols
# print(file.read(5))
## print lenghts of limited file read output
# print(len(file.read(15)))
## print file string by string
# for s in file:
#     print(s)
## Remember that you always need to close file if context manager not used!
# file.close()


### Create temporary file and remove it after work
## create file
# with open('file.tmp', 'w') as file:
#     file.write('This is example of file data')
## delete file (file.tmp) via try-except
# import os
# try:
#     os.remove('file.tmp')
### You need to catch exactly needed exceptioon
## except FileNotFoundError:
#     pass
### not just "Exception"
# except Exception as e:
#     print(e)
#     print(e.__class__)
#     pass
## delete file (file.tmp) via "if" statement
# path = '/home/tober/projects/qalight_g8/lecture_files/file.tmp'
# if os.path.exists(path):
#     os.remove(path)


