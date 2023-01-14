#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: a pointer to the head node
 *
 * Return: 0 if not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast_head = *head, *slow_head = *head, *prev, *next, *reversed;

	while (fast_head && fast_head->next)
	{
		slow_head = slow_head->next;
		fast_head = fast_head->next->next;
	}

	/* by this time slow_head points to the mid node */

	prev = NULL;
	while (slow_head)
	{
		next = slow_head->next;
		slow_head->next = prev;
		prev = slow_head;
		slow_head = next;
	}

	reversed = prev;
	slow_head = *head;

	while (reversed)
	{
		if (reversed->n != slow_head->n)
			return (0);

		slow_head = slow_head->next;
		reversed = reversed->next;
	}

	return (1);
}
