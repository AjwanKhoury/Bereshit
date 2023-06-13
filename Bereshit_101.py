import SpaceCraft
import PID
import Moon

class Bereshit_101:
    MAIN_ENG_F = 4300
    SECOND_ENG_F = 220
    ALL_BURN = 33.4

    def __init__(self):
        self.desired_vs = -10
        self.desired_hs = 0

    def runLanding(self):
        craft = SpaceCraft(0, 0, 0, 215, 0, 100000, 100000, 0, 0.1, 0, SpaceCraft.WEIGHT_EMP + 215)
        pid = PID(1.2, 0.01, 0.3)
        pid_ang = PID(0.314, 0.00003, 0.13) 

        while craft.getAlt() > 0:
            ds_angle = 0

            print(f"VS: {craft.getVs()}, HS: {craft.getHs()}, ANG: {craft.getAng()}, "
                  f"FUEL: {craft.getFuel()}, WEIGHT: {craft.getWeight()}, "
                  f"DS_ANG: {ds_angle}, ACC: {craft.getAcc()}")

            vs_error = self.desired_vs - craft.getVs()
            hs_error = self.desired_hs - craft.getHs()
            ang_error = ds_angle - craft.getAng()

            acc_cmd = pid.update(vs_error, craft.getDt())
            ang_cmd = pid_ang.update(ang_error, craft.getDt())

            craft.increaseThrust(acc_cmd)
            craft.increaseAngle(ang_cmd)

            craft.computeNextStep()

        print("Landing completed.")


    
