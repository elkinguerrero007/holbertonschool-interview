#include "palindrome.h"
/**
 * is_palindrome - is a function that detects if a number is a palindrome
 * @n: number to be checked
 *
 * Return: 1 if n is a palindrome, 0 otherwise
 */

int is_palindrome(unsigned long n)
{
	unsigned long pow_10;

	pow_10 = 10;
	while (n / pow_10 >= 10)
		pow_10 *= 10;

	while (n >= 10)
	{
		if (n % 10 != n / pow_10)
			return (0);
		n /= 10;
		pow_10 /= 10;
		n = n - ((n / (pow_10)) * pow_10);
		pow_10 /= 10;
	}
	return (1);
}
