import math
import Moon
import Bereshit_101

class SpaceCraft:
    WEIGHT_EMP = 165  # kg

    def __init__(self, vs, hs, ang, fuel, NN, dist, alt, time, dt, acc, weight):
        self.vs = vs
        self.hs = hs
        self.ang = ang
        self.fuel = fuel
        self.NN = NN
        self.dist = dist
        self.alt = alt
        self.time = time
        self.dt = dt
        self.acc = acc
        self.weight = weight

    def increaseThrust(self, inc):
        val = self.NN + inc

        if 0 <= val <= 1:
            self.NN = val
        elif val > 1:
            self.NN = 1
        elif val < 0:
            self.NN = 0

    def increaseAngle(self, angInc):
        val = self.ang + angInc

        if 0 <= val <= 90:
            self.ang = val
        elif val > 90:
            self.ang = 90
        elif val < 0:
            self.ang = 0

    def accMax(self, weight):
        return self.acc(weight, True, 8)

    def acc(self, weight, main, seconds):
        t = 0

        if main:
            t += Bereshit_101.MAIN_ENG_F

        t += seconds * Bereshit_101.SECOND_ENG_F
        ans = t / weight
        return ans

    def computeNextStep(self):
        ang_rad = math.radians(self.ang)
        h_acc = math.sin(ang_rad) * self.acc
        v_acc = math.cos(ang_rad) * self.acc
        vacc = Moon.getAcc(self.hs)
        self.time += self.dt
