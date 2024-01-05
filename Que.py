from Queue import Que
q=Que()
choice=0
while choice <4:
    print('STACK OPERATIONS')
    print('1. Add the element')
    print('2. Delete the element')
    print('3. Search the element')
    print('4.Exit')
    choice=int(input('Enter your choice:'))
    # Performing a task depending on user's choice
    if choice==1:
        element=int(input('Enter the elemenet to be Add:'))
        q.add(element)
    elif choice ==2:
        element=q.delete()
        if element==-1:
            print('The queue is empty')
        else:
            print('Removed Element:',element)
    elif choice==3:
        element=int(input('Enter the element to be searched:'))
        pos=q.search(element)
        if pos==-1:
            print('The queue is empty')
        elif pos ==-2:
            print('Elemenet not found in the queue')
        else:
            print('Element found at position',pos)
    else:
        break
    print('queue',q.display())
