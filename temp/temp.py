class MyObj:
    def __init__(self, name, obj):
        self.name = name
        self.obj = obj

    def set_name(self, name):
        self.name = name

    def set_obj(self, obj):
        self.obj = obj

    def __str__(self):
        return self.name + ': ' + str(self.obj)


myObj1 = MyObj('myObj1', 100)
myObj2 = MyObj('myObj2', 300)
myList = list()
myList.append(myObj1)
myList.append(myObj2)

myDict = dict()
myDict['myObj1'] = myObj1
myDict['myObj2'] = myObj2

myDict['myObj1'].set_name('hahahah, it is changed!')
myDict['myObj2'].set_obj(500)



for obj in myList: print(obj)