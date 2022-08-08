# myDict={
#     "Fast":"In a quick manner",
#     "Rohit": "A coder",
#     "Marks": [1,2,3,4,5],
#     "another": {"harry":'rohit'}
# }
# #it is unordered, mutable ,indexed , don't allow duplicates
# myDict['Marks']=[2,3,99]
# print(myDict["Marks"])


#Methods
        #https://startinup.up.gov.in/

myDict={
    "Fast":"In a quick manner",
    "Rohit": "A coder",
    "Marks": [1,2,3,4,5],
    "another": {"harry":'rohit'},
    1:2
}
print(list(myDict.keys()))
print(myDict.values())
print(myDict.items())# gives key value pair inform of tuple
updateDict={
    "k":"Rohit"
}
myDict.update(updateDict)#updating Dictionary by adding key value pair using update dict
print(myDict)
#print(myDict["Rohit1"]) # Returns error if  Rohit is not  there
print(myDict.get("Rohit1"))# Return none if Rohit is not there