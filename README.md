# Stream
In this exercise we will implement the Stream class.
 - Every Stream Object has it's own thread and list.
 - The thread will be opened in the CTOR and will wait.
 - The thread will operate only if the list is not empty and a operting function was called.
    - The thread will remove the elements on the list one by one and will activate the operating function on each of the elements.
    - When the list is empty the thread will be waiting again.
 - We can add elements to list using the "add" method.
 - The operating function will be defined using the "forEach" and "apply" methods.
    - The method "forEach" expects a consumer oprating function and therfor returns nothing.
    - On the other hand, the method "apply" expects a operating function that returns a value and therfor it returns a new Stream.
 - The method "stop" will immediately stop the thread and will stop all the linked Stream objects.

This technique will allow us to define all the work stations even before data will arrive, to stream information and each of the work stations will work in parallel with the others, as the output of one is the input of the next one.
The user will be able to define the work in the form of fluent programming and use lambda expressions.
