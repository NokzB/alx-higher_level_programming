#include "lists.h"

/**
* insert_node - a function to insert a number into a sorted linked list
* @head: double pointer to the first node of the linked list
* @number: number to add
* Return: the ddress of the added node
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *end, *new, *current;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	end = NULL;
	current = *head;

	for (; current != NULL && current->n < number;)
	{
		end = current;
		current = current->next;
	}
	new->next = current;

	if (end != NULL)
		end->next = new;
	else
		*head = new;
	return (new);
}
