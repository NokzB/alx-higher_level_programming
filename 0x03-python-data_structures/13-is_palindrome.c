#include "lists.h"
#include "stddef.h"
listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
* reverse_listint - Reverses a singly-linked listint_t list.
* @head: A pointer to the starting node of the list.
*
* Return: A pointer to the head of the reversed list.
*/
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}
	*head = prev;
	return (*head);
}

/**
* is_palindrome - Checks if a singly linked list is a palindrome.
* @head: A pointer to the head of the linked list.
*
* Return: 0 if the linked list is not a palindrome.
*         1 if the linked list is a palindrome.
*/
int is_palindrome(listint_t **head)
{
	listint_t *temp, *rev, *mid;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
	return (1);

	temp = *head;
	while (temp)
	{
		size++;
		temp = temp->next;
	}
	temp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
	temp = temp->next;

	if ((size % 2) == 0 && temp->n != temp->next->n)
	return (0);

	temp = temp->next->next;
	rev = reverse_listint(&temp);
	mid = rev;

	temp = *head;
	while (rev)
	{
		if (temp->n != rev->n)
		return (0);
		temp = temp->next;
		rev = rev->next;
	}
	reverse_listint(&mid);

	return (1);
}
