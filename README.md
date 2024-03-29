# Airbnb Clone Project
![image](https://github.com/Joh-Ishimwe/alu-AirBnB_clone/assets/127387467/c4b1f2b5-8dae-45ba-801c-c7b07a8b01f8)

## Project Description

This project involves the creation of an Airbnb clone, starting with the implementation of a command interpreter. The command interpreter is a critical component that allows users to manage objects within the project, such as creating new objects, retrieving objects from various sources, performing operations on objects, updating attributes, and destroying objects. The overall goal is to build a foundation for a full web application, integrating features like HTML/CSS templating, database storage, API, and front-end functionality.

## Command Interpreter

The command interpreter is a shell-like interface tailored to the specific use-case of managing Airbnb objects. It enables users to interact with and manipulate objects through various commands. The key functionalities include:

- Creating a new object (e.g., a new User or a new Place)
- Retrieving an object from a file, database, etc.
- Performing operations on objects (count, compute stats, etc.)
- Updating attributes of an object
- Destroying an object

### How to Start the Command Interpreter

To start the command interpreter, run the `console.py` script:

#### How to Use the Command Interpreter
Once in interactive mode, you can use various commands to manage Airbnb objects. For a list of available commands, type help
##### EXAMPLES 
Here are some examples of using the command interpreter:

```bash
(hbnb) create User
(hbnb) show User 123
(hbnb) update Place 456 name "Cozy Cabin"
(hbnb) destroy Amenity 789

