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
tuple1=(1,1,1,2,3,66,9,45,88,100)
print(tuple1.index(2))

gradestuple=(5,14,7),(23,36,28),(88,80,92)

print(gradestuple[2])
print(sum(gradestuple[0])/3,sum(gradestuple[1])/3,sum(gradestuple[2])/3)
tuple3=((94,90,96),)
print(gradestuple+tuple3)



gradesDict={'Chinese':[5,14,7],'English':[23,36,28],'Math':[88,80,92]}
print(gradesDict['Math'])
print(gradesDict.items())
#print(sum(gradesDict.values('Chinese'))/3)
gradesDict.update({'Science':[94,90,96]})
print(gradesDict)

#--------------------
allstudent = {'John', 'Eva', 'Jill' , 'Eric' , 'Andy' , 'Albert' , 'Polina' , 'Kristin' , 'Angela'}
danceclub = {'John','Eva','Jill','Eric','Andy'}
guitarclub = {'Andy','Albert','Polina','Kristin','Angela'}

print(danceclub & guitarclub)
print(guitarclub - danceclub)
print(allstudent - (danceclub | guitarclub))