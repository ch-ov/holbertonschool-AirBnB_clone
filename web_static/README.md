![Logo](logo.png)
# 0x00. AirBnB clone - The console

## Description
What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:\

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between "My object" and "How they are stored and persisted". This means that: from the console code (the shell itself) and from the front-end and RestAPI that we will build later, we will not have to pay attention (deal with) how objects are stored. _This abstraction will also allow changing the storage type easily without updating the code base_. The console will be a tool to validate this storage engine.

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## Learning Objectives
* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

## Commands

| Command | Usage | Description |
| :-------- | :------- | :------------------------- |
| help | **(hbnb) >>>** help [command] | List available commands with "help" or detailed help with "help cmd". |
| quit | **(hbnb) >>>** quit | Quit Command to exit the Console |
| EOF | **(hbnb) >>>** EOF | Quit Command to exit the Console |

## Execution

Clone the repository _https://github.com/ch-ov/holbertonschool-AirBnB_clone_

**Execution in interactive mode:**
```
$ ./console.py
(hbnb) >>> help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) >>>
(hbnb) >>>
(hbnb) >>> quit
$
```
**Execution in non-interactive mode:**
```
$ echo "help" | ./console.py
(hbnb) >>>

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) >>>
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb) >>>

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) >>>
$
```
## Authors

* [Alberto Marrugo](https://github.com/ajmarrugos)
* [Christian Oviedo](https://github.com/ch-ov)
