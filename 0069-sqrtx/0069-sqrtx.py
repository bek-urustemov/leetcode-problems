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
        if x < 2:
            return x

        left = 1
        right = x//2
        while left <= right:
            mid = (left+right)//2
            sq = mid * mid

            if sq == x:
                return mid
            elif sq < x:
                left = mid + 1
            else:
                right = mid - 1

        return right
                
            