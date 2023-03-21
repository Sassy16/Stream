# Stream
In this exercise we will implement the Stream class.
 - Every Stream Object has it's own thread and list.
 - The thread will be opened in the CTOR and will wait.
 - The thread will operate only if the list is not empty and a operting function was called.
    - The thread will remove the elements on the list one by one and will activate the operating function on each of the elements.
    - When the list is empty the thread will be waiting again.
 - We can add elements to list using the "add" method.
 - The operating function will be defined using the "forEach" and "apply" methods.
