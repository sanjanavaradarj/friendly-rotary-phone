Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dictionary
birthday={
    "sanjana":"22-11-2006",
...     "sinchana":"09-01-2009",
...     }
>>> print(birthday)
{'sanjana': '22-11-2006', 'sinchana': '09-01-2009'}
>>> #finding type
>>> birthday={
...     "sanjana":"22-11-2006",
...     "sinchana":"09-01-2009",
...     }
>>> print(type(birthday))
<class 'dict'>
>>> #to know single value
>>> print(birthday["sanjana"])
22-11-2006
>>> #to know other than in the birthday
>>> print(birthday["women"])
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(birthday["women"])
KeyError: 'women'
>>> #to avoid error
>>> print(birthday.get("women","not found"))
not found
>>> #to add and update
>>> birthday={
...     "sanjana":"22-11-2006",
...     "sinchana":"09-01-2009",
...     }
>>> birthday["women"]="02-03-2000"
>>> print(birthday)
{'sanjana': '22-11-2006', 'sinchana': '09-01-2009', 'women': '02-03-2000'}
>>> #to update
>>> birthday={
...     "sanjana":"22-11-2006",
...     "sinchana":"09-01-2009",
...     }
>>> print("updating.....")
updating.....
>>> birthday["sanjana"]="02-02-2007"
>>> print(birthday)
{'sanjana': '02-02-2007', 'sinchana': '09-01-2009'}
