#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fire, *water;

	if (list == NULL || list->next == NULL)
		return (0);

	fire = list->next;
	water = list->next->next;

	while (fire && water && water->next)
	{
		if (fire == water)
			return (1);

		fire = fire->next;
		water = water->next->next;
	}

	return (0);
}
