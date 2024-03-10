#AirBnB_clone
AirBnB clone is clone of website airbnb for reserving hotel rooms, or renting house online, and in this project the frontend is the console, the data_structure will be OOP.
Classes:
BaseModel:is the parent class for all sub-classes, 
	it have private instance: object, file_path
	methods: 
	init - inititializer from **kwargs
	__str__ - print the string reperesentation of the class
	save - save all attribute to Json file while changing update time
	to_dict - change given argument to dictionary
User:inherit form BaseModel
      it have public instance: email, password, first and last name

City:Public class attributes:
	state_id: string - empty string: it will be the State.id
	name: string - empty string

Place:Public class attributes:
	name: string - empty string
	description: string - empty string
        number_rooms: integer - 0
        number_bathrooms: integer - 0
        max_guest: integer - 0
        price_by_night: integer - 0
        latitude: float - 0.0
        longitude: float - 0.0
	amenity_ids: list of string - empty list: it will be the list of Amenity.id             later

Review: Public class attributes:
	city_id: string - empty string: it will be the City.id
	user_id: string - empty string: it will be the User.id
	text: string - empty string
	
Amenity:Public class attributes:
	name: string - empty string

State:Public class attributes:
	name: string - empty string
   
The command interpreter(console): is how we will interact with the program, 
How to start it:
	1, clone file
	2, at main file run command './console.py' it will start the cmd
	   that look like this: $./console.py
				(HBnB)
How to use it:
In console, there are the following commands: 
	*create: create a new class and print the id of the class
		syntax: create <class name> <class id>
	*show: print the string representation of instance 
	based on the class name and id.
		syntax: show <class name> <class id>
	*destroy: delete an instance based on the class name and id
		syntax: destroy <class name> <class id>
	*all: print all string representation of all instances based or not on 
	the class name, 
		syntax: all <class name>
	*update: updates an instance based on the class name and id by adding 
	or updating attribute(save the change into the JSON file)
	     syntax: update <class name> <id> <attribute name> "<attribute value>"
