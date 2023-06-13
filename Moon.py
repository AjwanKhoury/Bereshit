import math

class Moon:
    RADIUS = 3475 * 1000  # meters
    ACC = 1.622  # m/s^2
    EQ_SPEED = 1700  # m/s

    @staticmethod
    def getAcc(speed):
        n = abs(speed) / Moon.EQ_SPEED
        ans = (1 - n) * Moon.ACC
        return ans
