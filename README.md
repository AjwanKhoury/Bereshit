## About the Simulation

This simulation aims to replicate the landing procedure of the Bereshit spacecraft using a PID controller to regulate engine thrust and vehicle angle. The PID controller ensures precise control over the spacecraft's vertical and horizontal speeds as well as its angle throughout the landing process.

The simulation begins by emulating the initial settings and conditions of the actual Bereshit landing mission.

## Landing Physics

During the early stages of the mission, an issue arose with the star tracking system responsible for determining the spacecraft's angle. Consequently, the crew made the decision to rely on the acceleration sensor as an alternative method for angle measurement.

As a result of prolonged exposure to solar radiation, the low-cost materials utilized in the spacecraft became damaged, leading to system failures that triggered automatic restarts.

Due to budget constraints, the spacecraft lacked redundant systems, increasing the complexity and risks associated with the landing procedure.

While the spacecraft descended toward the lunar surface, an unexpected malfunction occurred in the acceleration sensor (IMU2), prompting the crew to quickly choose between restarting IMU2 or relying solely on IMU1. They opted to initiate a restart of IMU2.

However, restarting IMU2 inadvertently caused a temporary disruption in data transmission from IMU1 due to system logic conflicts. As a result, the system experienced a brief interruption in acceleration data for approximately one second, prompting a sequence of system restarts.

During the restart sequence, the main engine of the spacecraft unexpectedly shut down, resulting in the craft entering a state of free fall until it ultimately crashed onto the lunar surface.

## Bereshit Crash Landing Sequence

The crash landing of the Bereshit spacecraft followed the following sequence of events:

1. IMU2 Issue: The acceleration sensor (IMU2) encountered a malfunction, compromising its ability to provide accurate data.
2. Activating IMU2: In an attempt to rectify the issue, the crew decided to restart IMU2, hoping to restore its functionality.
3. Data Transfer Block: Unfortunately, restarting IMU2 caused a temporary blockage in data transmission from IMU1, impeding the flow of critical information.
4. System Restart: The system, detecting the disruption in data transfer, initiated a restart sequence to resolve the issue.
5. Control Command Wait: During the restart process, the system entered a waiting state, anticipating the upload of control commands to guide the landing procedure.
6. Main Engine Shutdown: As part of the restart sequence, the main engine of the spacecraft unexpectedly shut down, leading to a loss of thrust.
7. Crash: With the main engine offline and the spacecraft in a free fall state, it eventually crashed onto the lunar surface.

## Python Classes

### Moon Class

- This class represents the Moon and contains static properties related to the Moon's characteristics, such as its radius, acceleration, and equatorial speed.
- The `getAcc()` method calculates the acceleration based on the given speed and the Moon's equatorial speed.

### SpaceCraft Class

- This class represents the spacecraft and its attributes, including vertical speed, horizontal speed, angle, fuel, weight, and more.
- The `increaseThrust()` method increases the thrust of the spacecraft's engine by a specified increment.
- The `increaseAngle()` method increases the spacecraft's angle by a specified increment.
- The `accMax()` and `acc()` methods calculate the maximum acceleration and acceleration based on weight, respectively.
- The `computeNextStep()` method computes the next step of the spacecraft based on its current attributes.

### Bereshit_101 Class

- This class represents the Bereshit 101 spacecraft and contains properties specific to this spacecraft model.
- The `__init__()` method initializes the desired vertical and horizontal speeds for the landing procedure.
- The

 `runLanding()` method executes the landing simulation using a PID controller to control the thrust and angle of the spacecraft.
- The PID controller is initialized with specific values for proportional, integral, and derivative gains. It is used to calculate control commands based on errors in vertical speed, horizontal speed, and angle.

### PID Class

- This class represents a PID controller and contains properties and methods for calculating control commands based on error values and time intervals.
- The `__init__()` method initializes the PID controller with the provided proportional, integral, and derivative gains.
- The `update()` method calculates the control output based on the error and time interval using the PID control algorithm.

Ensure that all required dependencies are imported and that the necessary instances of the classes are created before running the `runLanding()` method of the `Bereshit_101` class to initiate the landing simulation.
