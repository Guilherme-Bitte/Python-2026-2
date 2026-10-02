tecnologias = {'Python', 'SQL', 'Git', 'Docker', 'Linux'}
tecnologias.add('FastAPI')
tecnologias.discard('SQL')

for item in tecnologias:
    print(item)
print(sorted(tecnologias))