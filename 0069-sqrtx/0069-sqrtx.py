class Solution:
    def mySqrt(self, x):
        # UNDERSTAND:
        # We can't use built in functions sqrt or **0.5
        # The number is non-negative

        # PLAN:
        # We could technically iterate through the numbers to the point x/2
        # We can check through every iteration if i*i > x or i*i < x:
        # Once we hit the point where i*i>x: -> we can return the previous numbers

        # IMPLEMENT:

        # range, and this is the max i could be
        if x==1:
            return 1
        up_to = x//2
        for i in range(up_to + 2):
            if i*i > x:
                return i-1