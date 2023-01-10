#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: the head node
 * @number: the number to be inserted
 *
 * Return: the address of the new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *previous;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
	{
		return (NULL);
	}

	new->n = number;

	if (*head == NULL)
	{
		*head = new;
		(*head)->next = NULL;
	}

	if (*head && (*head)->n < number)
	{
		current = *head;
		while (current && (current->n < number))
		{
			previous = current;
			current = current->next;
		}
		previous->next = new;
		new->next = current;
	}

	if (*head && (*head)->n > number)
	{
		previous = *head;
		*head = new;
		new->next = previous;
	}

	return (new);
}
