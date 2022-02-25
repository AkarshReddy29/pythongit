from builtins import print
from collections import namedtuple
from collections import deque
from collections import ChainMap
from collections import Counter
from collections import OrderedDict
from collections import defaultdict
from collections import UserDict

a=namedtuple('courses','name,technology,version')
s=a('DS','python',1.1)
print(s)
print(list(s))
#print(dict(s)) ##ValueError: dictionary update sequence element #1 has length 6; 2 is required
print(set(s))

#namedtuple using list
b=namedtuple('courses','name,technology')
c=b._make(['AI','Java'])
print(c)
print(b._make(['ML','C']))

##Deque
d=['a','k','a','r','s','h']
e=deque(d)

print("Deque:-",e)
print("Count",e.count('a'))

e.insert(1,"Reddy")
print("Insert:",e)

e.appendleft("123")
print("append left:",e)

z=[8,9]
e.append(z)
print("Append Right:",e)

e.pop()
print("right pop",e)

e.popleft()
print("leftpop",e)

e.reverse()
print("Reverse",e)

f=[11,12]
e.extend(f)
print(e)

e.extendleft('2')
print(e)

#####Chainmap#####
a1={1:'Akarsh', 2:'Reddy'}
b1={3:'DS',4:'Python'}
c1=ChainMap(a1,b1)
print(c1)
print(list(c1.keys()))
print(list(c1.values()))
print(c1.get(1))
print(list(c1.maps))

#####Counter######
a12=[1,1,2,3,3,3,4,5,4,5,4,3,6,2,2]
b12=Counter(a12)
print(b12)

print(list(b12.elements()))
print(b12.most_common())
sub={5:1,6:1}

b12.subtract(sub)
print(b12.most_common())

#####Orderdict####
d1=OrderedDict()
d1[1]='A'
d1[2]='K'
d1[3]='A'
d1[4]='R'
d1[5]='S'
d1[6]='H'
print(d1)
d1[1]='S'
print(d1)
print(d1)
#####UserDict#####
