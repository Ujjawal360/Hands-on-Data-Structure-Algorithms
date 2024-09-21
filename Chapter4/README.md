This chapter is on LinkedList.

The topics are:
* Single Linked List
* Double linked list
* Circular linked list
------------------------------------------------------------------------
# Single Linked List:

* Inserting value at the end (**append operation - using just the head**): [Adding item at end Single Linked List](appendItematEnd_SingleLinkedList.py) <br>
This implementation of adding the element to the end of the list of **O(n)** because we have to traverse to the end of the list to add an element.

Here is the visualization:
![Adding at the end](addEndSL.png)


* Inserting value at the end (**append operation - using just the tail**): [Adding item at end Single Linked List using Tail](appendItematEnd_SingleLinkedList_tail.py) <br>
This implementation of adding the element to the end of the list of **O(1)** because we just add the element straight to the tail. <br>
  * if no element is in the linkedList, the head and tail becomes the same
  * **_While adding the element to the tail, the new tail will shift too (to the node just created)._**

