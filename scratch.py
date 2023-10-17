import re

# Reading Document
with open('regex_test.txt', 'r') as f:
    data = f.read()
    print(data)

# #Creating and executing Data Search & Extraction
# namePattern = re.compile(r'(\w+[,][ ]\w+[-]\w+|\w+[,][ ]\w+)')
# twitPattern = re.compile(r'(@[a-z]+\s)')

# firstNameSearch = namePattern.findall(data)
# firstTwitSearch = twitPattern.findall(data)

# # Name List filtering / formatting
# nameFilterOne = []

# for name in firstNameSearch:
#     if name != 'Teacher, Coding':
#         nameFilterOne.append(name)

# unformattedNameList = [nameFilterOne[0], nameFilterOne[4], nameFilterOne[7], nameFilterOne[11], nameFilterOne[13], nameFilterOne[14]]

# finalNameList = []

# for name in unformattedNameList:
#     x = name.split(', ')
#     finalNameList.append(f'{x[1]} {x[0]}')

# # Removing whitespace character from Twitter List

# finalTwitList = [x[:-1] for x in firstTwitSearch]

# #Dictionary for calling f'statement

# nameTwitDict = {}

# for i in range(len(finalNameList)):
#     name = finalNameList[i]
#     twit = finalTwitList[i]
#     nameTwitDict[name] = twit

# #Calling f'statement for all key value pairs

# for n, t in nameTwitDict.items():
#     print('{} / {}'.format(n, t))









