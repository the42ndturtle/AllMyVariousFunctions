//DOCUMENTATION\\
	--Perm Function
The perm function takes three arguments: line, text, and filer
--line
The line argument takes the line number that you want to write over.
Note: The line number DOES start at 0, even if the numbers on the side of your editor start at 1, the line argument starts at 0
--text
The text argument takes what you want the line to say after it has been changed
Note: If you want to maintain the order of your file, end all text arguments with a ('\n') or (+ '\n'). The text argument puts write exactly what you put in, so if you do not end it with a \n it will merge with the next line of the program.
--filer
The filer argument takes the file that you want to edit.
Note: if you want the file to edit itself (which is what I mad this for), then set the filer argument to (__file__). This will select itself to be edited
--EXAMPLE
from AllMyVariousFunctions.perm import *
#FOO
#BAR
perm(1, '#Hello\n', __file__)
perm(2, '#World\n', __file__)
--This will change your file to read
from AllMyVariousFunctions import perm
#Hello
#World
perm(1, '#Hello\n', __file__)
perm(2, '#World\n', __file__)
--END EXAMPLE
	--Mutables
The mutables module allows you to keep a dictionary of mutable variables that you can change from within functions and moderate easily
The mutables module has seven methods to interact with the mutables dictionary
  --add(key, value)
The add method allows you to add a new variable to your dictionary
The add method will return True when run
--key
The key argument defines the name of the new variable you will be creating. Because it is a dictionary, all rules that apply to creating a new dictionary key apply here.
--value
The value argument takes the value of the new variable you are creating. 
  --sub(key)
The sub method allows you to remove a variable from your dictionary
The sub method will return True if it was successful with removing the key and will return False if the key trying to be removed did not exist
--key
The key argument takes the name of the variable to be deleted
  --get(key)
The get method will return the value of a variable in your dictionary
It will return False if the variable does not exist
--key
The key argument takes the name of the variable to be gotten.
  --set(key, value)
The set method will set the value of an already existing variable equal to the value defined in the call
It will return True if the operation was successful and will return False if the variable does not exist
--key
The key argument takes the name of the variable you want to change the value of
--value
The value argument takes the value of the that the variable will be changed to
  --itr()
The itr method will return a string of all of the varibles and what they are equal to
  --itr_var()
The itr_var method will return a string of all of the variables that have been created
  --itr_val()
The itr_val method will return a string of all of the values that are currently defined by variables
--EXAMPLES in a python command line
>>>from AllMyVariousFunctions.mutables import *
>>>mutables.add('foo','bar')
>>>print(mutables.variables)
>>>{'foo': 'bar'}
>>>mutables.sub('foo')
>>>print(mutables.variables)
>>>{}
>>>mutables.add('foo', 'bar')
>>>mutables.add('hello', 'world')
>>>mutables.itr()
>>>foo = bar
   hello = world
>>>mutables.itr_var()
>>>foo
   hello
>>>mutables.itr_val()
>>>bar
   world
>>>mutables.set('foo', 'bad')
>>>print(mutables.get('foo'))
>>>bad
--And most importantly, changing value in a funciton
from AllMyVariousFunctions.mutables import *
mutables.add('foo', 'bar')
def change():
	mutables.set('foo', 'bad')
change()
print(mutables.get('foo'))
#returns: bad