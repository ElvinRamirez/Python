#1 Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
x[1][0] = 15
#print(x)
students[0]['last_name'] = 'Bryant'
#print(students[0]['last_name'])
sports_directory['soccer'][0] = 'Andres'
#print(sports_directory['soccer'][0])
z[0]['y'] = 30
#print(z[0]['y'])

#2 Iterate Through a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(list):
    for i in range(0, len(list)):
        output = ""
        for key,val in list[i].items():
            output += f" {key} - {val},"
        print(output)

iterateDictionary(students)

#3Get Values From a List of Dictionaries
students2 = [
    {'first_name': 'Miguel', 'last_name': 'Test'},
    {'first_name': 'John', 'last_name': 'Doe'},
    {'first_name': 'Antonio', 'last_name': 'Corleone'}
]

def iterateDictionary2(students2):
    for i in range(len(students2)):
        print(students[i]['first_name'])
    for i in range(len(students2)):
        print(students[i]['last_name'])

iterateDictionary2(students2)

#4 Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

#print(dojo['locations'])
def printInfo(dictionary):
    for key,values in dictionary.items():
        print("          ")
        print(f"{len(values)} {key}")
        for i in range(len(values)): 
            print(values[i])

printInfo(dojo)
