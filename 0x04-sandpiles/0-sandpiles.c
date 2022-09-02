#include "sandpiles.h"

/**
 * print_grid - a function that prints the grid
 * @grid1: grid to be check if stable or not
 *
 * Return: nothing
 */
static void print_grid(int grid1[3][3])
{
	int i, j;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			if (j)
				printf(" ");
			printf("%d", grid1[i][j]);
		}
		printf("\n");
	}
}

/**
 * stabilizer - a function that checks if the grid is stable
 * @grid1: grid to be check if stable or not
 *
 * Return: 1 if stable, 0 if not
 */
int stabilizer(int grid1[3][3])
{
	int i, j, stable = 1;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			if (grid1[i][j] > 3)
			{
				stable = 0;
				break;
			}
		}
	}
	return (stable);
}

/**
 * sum - a function that performs a sum of two grids
 * @grid1: stable sandpile where the sum is going to be performed
 * @grid2: stable sandpile that sums grid1
 *
 * Return: nothing
 */
void sum(int grid1[3][3], int grid2[3][3])
{
	int i, j;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			grid1[i][j] = grid1[i][j] + grid2[i][j];
		}
	}
}

/**
 * toppling - a function that makes a grid that topples sandpiles
 * @grid1: stable sandpile where the sum is going to be performed
 * @aux: grid which if added to grid will simulate a toppling
 *
 * Return: nothing
 */
void toppling(int grid1[3][3], int aux[3][3])
{
	int i, j;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
			aux[i][j] = 0;
	}

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			if (grid1[i][j] > 3)
			{
				aux[i][j] -= 4;
				if (i + 1 < 3)
					aux[i + 1][j]++;
				if (i - 1 >= 0)
					aux[i - 1][j]++;
				if (j + 1 < 3)
					aux[i][j + 1]++;
				if (j - 1 >= 0)
					aux[i][j - 1]++;
			}
		}
	}
}

/**
 * sandpiles_sum - a function that performs a sandpiles sum
 * @grid1: stable sandpile where the sum is going to be performed
 * @grid2: stable sandpile that sums grid1
 *
 * Return: nothing
 */
void sandpiles_sum(int grid1[3][3], int grid2[3][3])
{
	int aux[3][3];

	sum(grid1, grid2);
	while (!stabilizer(grid1))
	{
		printf("=\n");
		print_grid(grid1);
		toppling(grid1, aux);
		sum(grid1, aux);
	}
}
