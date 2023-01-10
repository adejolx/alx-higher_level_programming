#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: A pointer to a list
 *
 * Return: 0 if no cycle, 1 if cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fastPtr = list, *slowPtr = list;

	while (fastPtr && slowPtr && fastPtr->next != NULL)
	{
		slowPtr = slowPtr->next;
		fastPtr = fastPtr->next->next;

		if (slowPtr == fastPtr)
			return (1);
	}
	return (0);
}
