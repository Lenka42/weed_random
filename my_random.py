__author__ = 'elena'
class Random():
    def __init__(self):
        self.cur = 65539
        self.m = 2 ** 31
        self.xi = 65539

    def seed(self, x):
        """
        Sets the global variable xi
        """
        self.xi = x

    def rng(self):
        """
        Linear congruential generator of random numbers in interval [0,m)
        """
        self.xi = (self.cur * self.xi) % self.m
        return self.xi / self.m

    def int_rng(self, n0, n):
        return n0 + int(self.rng() * (n - n0))

    def random(self):
        """
        MacLaren-Marsaglia random number generator in range [0,1)
        """
        a1 = 161051
        a2 = 50653
        k = 192
        self.cur = a1
        table = [self.rng() for _i in range(k)]
        self.cur = a2
        idx = self.int_rng(0, k)
        self.seed(table[idx] * self.m)
        return self.xi / self.m

    def int_random(self, n0, n):
        """
        :return: integer number in range [n0,n)
        """
        return n0 + int(self.random() * (n - n0))

    def list_of_random(self, n):
        """
        :param n: Length of the list.
        :return: List of length n of random numbers
        """
        return map(lambda x: self.random(), range(n))
