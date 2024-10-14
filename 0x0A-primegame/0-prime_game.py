#!/usr/bin/python3

"""Playing prime game"""


def prime(n):
    """check prime number"""
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
        return True


def prime_calculator(n, primes):
    """calculate all primes"""
    t_prime = primes[-1]
    if n > t_prime:
        for i in range(t_prime + 1, n + 1):
            if prime(i):
                primes.append(i)
            else:
                primes.append(0)


def isWinner(x, nums):
    """
    number of rounds
    where x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    You cannot import any packages in this task
    """

    win = {"Maria": 0, "Ben": 0}

    primes = [0, 0, 2]

    for round in range(x):
        sum_opts = sum((i != 0 and i <= nums[round])
                       for i in primes[:nums[round] + 1])
        if (sum_opts % 2):
            winner = "Maria"
        else:
            winner = "Ben"

        if winner:
            win[winner] += 1
    if win["Maria"] > win["Ben"]:
        return "Maria"
    if win["Ben"] > win["Maria"]:
        return "Ben"
    return None
