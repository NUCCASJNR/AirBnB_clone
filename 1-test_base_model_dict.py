#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
<<<<<<< HEAD
    print("\t{}: ({}) - {}".format(key,
          type(my_model_json[key]), my_model_json[key]))
=======
<<<<<<<< HEAD:tests/base_test_model_dict.py
    print("\t{}: ({}) - {}".format(key,
                                   type(my_model_json[key]), my_model_json[key]))
========
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
>>>>>>>> 48430138765ce8ae2be5a926161bba4cb647ec8f:1-test_base_model_dict.py
>>>>>>> 48430138765ce8ae2be5a926161bba4cb647ec8f

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))
print("--")
print(my_model is my_new_model)
