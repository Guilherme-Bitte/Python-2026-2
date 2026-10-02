#Conjunto vazio
vazio = set()
#A partir de uma lista
data_scientist = set(['Python', 'R', 'SQL', 'Git'])
print(data_scientist)
#Com chaves e valores
data_enginner = {'Python', 'Java', 'Scala', 'Git'}
print(data_enginner)
skills = ['Python', 'SQL', ('Git', 'Linux')]
print(skills)
try:
    skills.add(['PowerPoint', 'Blender'])
except:
    print("error")
#TypeError: unhashable type: 'list'
