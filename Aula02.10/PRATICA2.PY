backend = {'Python', 'SQL', 'Docker', 'Linux', 'Git'}
print(f"A lista backend é: {backend}")
cloud = {'Docker', 'Linux', 'AWS', 'Terraform', 'Git'}
print(f"A lista cloud é: {cloud}")
print("============================================")
backend.union(cloud)
print(f"A união é: {backend.union(cloud)}")
backend.intersection(cloud)
print(f"A interseção é: {backend.intersection(cloud)}")
backend.difference(cloud)
print(f"A diferença é: {backend.difference(cloud)}")
backend.symmetric_difference(cloud)
print(f"A diferença simetrica é: {backend.symmetric_difference(cloud)}")