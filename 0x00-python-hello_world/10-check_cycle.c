#include "lists.h"

/**
* check_cycle - checks if a singly linked list has a cycle in it
* @list: pointer to the singly linked list
* Return: 0 if there is no cycle, 1 if there is a cycle.
*/

int check_cycle(listint_t *list)
{
	listint_t *pen, *pencil;

	pen = list;
	pencil = list;

	while (pen && pencil)
	{
		if (pencil->next == NULL)
			return(0);

		pen = pen->next;
		pencil = pencil->next->next;
		
		if (pen == pencil)
			return(1);
	}
	return(0);	
}
