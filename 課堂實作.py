score = [1, 3, 5, 7, 9,11,12]

print(score[2:])
print(score[-2:]  )

print(len(score ) )
print(sum(score))
print(sum(score )/len(score ))
x='8'
y=int(x)
print(y+2)

ls=[]
ls.append(456)
print(ls)
ls.insert(0,123)
print(ls)
del score [0:2]
print(score )
score.remove(12)
print(score )
score [0]=100
print(score)
print(score.count(100))
aa=['a','b','c']
print(aa+score)
aas = [[1,2],[4,5]]
print(aas[1][0])
print(sorted(score))
grades=[[5,14,7],[23,36,28],[88,80,92]]
print(grades[0])
print(sum(grades[0])/len(grades[0]) ,sum(grades[1])/len(grades[1]),sum(grades[2])/len(grades[2]))
grades.append([94,90,96])
print(grades)
