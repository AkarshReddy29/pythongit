x='Akarsh'
y=1.75
z=30j
A= True
#Strings
print(x)
print(len(x))
print(x[0]=='A')
print(x[3:5])
print(x.upper())
print(x[-2])


#list Datatype
Fruits=['Apple','Mango','orange',10,20]
print(Fruits)
print(Fruits[1])
print(len(Fruits))
print(Fruits[-1])
Fruits[3]=40
print("Updated at index position : ",Fruits)
Fruits.append('Akarsh')
print("Appended at last : ",Fruits)
Fruits.insert(3,'Kiwi')
print("Inserted at index position : ",Fruits)
Fruits.reverse()
print("List Reverse : ",Fruits)
#print(Fruits.reverse())
Fruits.insert(3,'Kiwi')
print(Fruits)

#Dictionary
print(end='\n\n\n')
courses={
    'First':'python',
    'Second':'ML',
    'Third':'DS'
}
print(courses)
print(courses.get('Third'))
courses['First']='JS'
courses['fourth']='Java'
print(len(courses))
print(courses)
print(courses.keys())
print(courses.values())

print(courses)
print(Fruites)
print("Akarsh Reddy is Royal Reddy King")

