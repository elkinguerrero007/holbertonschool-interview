#include "lists.h"

/**
 * _is_loop - finds the loop in a linked list
 * @slow: pointer to advance one node at a time
 * @fast: pointer to advance two nodes at a time
 * @start: flag to start the loop
 * Return: address of the node in the loop, or NULL if there is no loop
 */

listint_t *_is_loop(listint_t *slow, listint_t *fast, int start)
{
	if (start)
		fast = fast
				   ? fast->next ? fast->next->next : NULL
				   : NULL;

	if (fast == NULL || slow == NULL)
		return (NULL);

	if (slow == fast)
		return (slow);

	return (_is_loop(slow->next, fast->next ? fast->next->next : NULL, 0));
}

/**
 * find_listint_loop - finds the loop in a linked list
 * @head: pointer to head of list
 * Return: address of the node where the loop starts,
 * or NULL if there is no loop
 */
listint_t *find_listint_loop(listint_t *head)
{
	listint_t *loop = NULL;
	listint_t *firt = NULL;

	if (head == NULL)
		return (NULL);

	firt = loop = is_loop(head);

	if (loop == NULL)
		return (NULL);

	if (firt == head)
		return (head);

	do {
		loop = loop->next;
		if (firt == loop)
			head = head->next;
	} while (head != loop);

	return (head);
}
