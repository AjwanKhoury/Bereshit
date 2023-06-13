class PID:
    def __init__(self, p, i, d):
        self.P = p
        self.I = i
        self.D = d
        self.lastError = 0
        self.firstRun = True
        self.integralError = 0

    def update(self, error, dt):
        if self.firstRun:
            self.firstRun = False
            self.lastError = error
        diff = (error - self.lastError) / dt
        self.integralError += error * dt
        controlOut = self.P * error + self.I * self.integralError + self.D * diff
        self.lastError = error
        return controlOut
