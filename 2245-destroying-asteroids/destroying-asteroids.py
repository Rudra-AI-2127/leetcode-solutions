class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        
        asteroids.sort()

        for asteroid in asteroids:
            if mass < asteroid:
                return False
            mass += asteroid

        return True
        