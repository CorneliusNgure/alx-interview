#!/usr/bin/python3
""" Module defining a function to find the winner of a prime game """


def isWinner(x, nums):
    """
    Determine the winner of the prime game after x rounds.

    Args:
        x (int): Number of rounds.
        nums (list[int]): List of n values for each round.

    Returns:
        str: Name of the player who won the most rounds
        ("Maria" or "Ben"), or None if tied or invalid input.
    """
    if not nums or x < 1:
        return None
    max_nu = max(nums)

    def sieve(max_n):
        """Precompute prime no.s up to max_n using Sieve of Eratosthenes."""
        is_prime = [True] * (max_n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

        for i in range(2, int(max_n**0.5) + 1):
            if is_prime[i]:
                for multiple in range(i * i, max_n + 1, i):
                    is_prime[multiple] = False

        return is_prime

    def count_primes(n, primes):
        """Count how many primes are <= n."""
        return sum(primes[:n + 1])

    # Find the maximum n in nums to optimize the sieve computation
    max_n = max(nums)
    # Get a boolean array indicating prime numbers
    primes = sieve(max_n)
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_primes(n, primes)

        # Maria wins if the number of primes is odd. Otherwise, Ben wins
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
