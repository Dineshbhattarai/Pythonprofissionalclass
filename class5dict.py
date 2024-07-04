cardetails ={
    "brand":"Ford",
    "model" : "Mustang",
    "years":1998

}
print(cardetails["brand"])
print(cardetails.get("model"))
print(cardetails.keys())
print(cardetails.values())
cardetails["color"]="coal"
cardetails.update({"mielage":8})
cardetails.popitem()
print(cardetails)


# loop throuht distionary item
Student={
    "name":"John",
    "Age":20,
    "grade":"XII"
}



for i in Student:
  

 for i in Student.values():
  print(i)

  for i,j in Student.items():
   print(i,j)
    

    # dictionary Items
thisdict = {
"brand":"Fond",
"electric": False,
"year":1998,
 "color": ["red", "white", "blue"]

    }

print(thisdict["color"][0])









