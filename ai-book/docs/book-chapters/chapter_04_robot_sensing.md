# Chapter 04: Robot Sensing

import AIAgentPrompt from '@site/src/components/AIAgentPrompt';

## Introduction
Robot sensing is the cornerstone of intelligent robotic behavior, enabling machines to perceive, interpret, and interact with the physical world. In the context of humanoid robotics, effective sensing is paramount for achieving human-like capabilities such as locomotion, manipulation, and safe human-robot interaction. This chapter delves into the fundamental concepts of robot sensing, exploring the diverse array of sensors that equip humanoid robots with the ability to gather information about their internal state (proprioception) and their surrounding environment (exteroception). We will discuss the principles behind various sensing modalities, their applications in enhancing a robot's perception, facilitating robust decision-making, and enabling autonomous operation in complex, dynamic environments. Understanding robot sensing is crucial for developing robots that can navigate unstructured spaces, perform intricate tasks, and interact seamlessly and safely with humans.

## Theory

Robot sensing can be broadly categorized into two main types: proprioception and exteroception. These categories, often complemented by sensor fusion techniques, provide robots with a comprehensive understanding of their internal state and external environment.

### Proprioception: Internal State Sensing

Proprioceptive sensors provide information about the robot's own body and internal state. This is analogous to how humans sense their limb positions and muscle forces without looking. Key proprioceptive sensors include:

*   **Encoders**: Measure the angular position or velocity of robot joints. They are crucial for precise control of robot movements and for determining the robot's configuration (pose).
*   **Inertial Measurement Units (IMUs)**: Typically comprise accelerometers and gyroscopes (and sometimes magnetometers) to measure linear acceleration, angular velocity, and orientation (roll, pitch, yaw). IMUs are vital for maintaining balance, estimating body velocity, and overall state estimation in dynamic tasks.
*   **Force/Torque Sensors**: Measure the forces and torques exerted at various points, such as robot wrists, ankles, or fingertips. These are essential for compliant interaction with the environment, grasping delicate objects, and maintaining stable contact during locomotion.
*   **Potentiometers**: Measure linear or angular displacement, often used to determine joint angles or linear slide positions.
*   **Temperature Sensors**: Monitor the temperature of motors and electronics to prevent overheating and ensure safe operation.

<AIAgentPrompt type="explainer" title="Understanding Proprioceptive Sensors">
Explain how proprioceptive sensors work together to give a humanoid robot awareness of its body configuration. Use the analogy of how humans know where their limbs are even with their eyes closed. Discuss why combining encoders with IMUs provides more robust state estimation than using either sensor alone.
</AIAgentPrompt>

### Exteroception: External Environment Sensing

Exteroceptive sensors gather information about the robot's external environment, allowing it to perceive objects, obstacles, and other agents. This is akin to human senses like sight, hearing, and touch. Key exteroceptive sensors include:

*   **Cameras (Vision Systems)**: Provide rich visual data (intensity, color, depth).
    *   **Monocular Cameras**: Used for 2D image processing, object detection, and tracking.
    *   **Stereo Cameras**: Mimic human binocular vision to estimate depth and create 3D maps of the environment.
    *   **RGB-D Cameras (e.g., Intel RealSense, Microsoft Kinect)**: Provide both color (RGB) and depth information, facilitating 3D perception and object recognition.
*   **Lidar (Light Detection and Ranging)**: Uses pulsed laser light to measure distances to objects, creating highly accurate 2D or 3D point clouds of the environment. Excellent for mapping, localization, and obstacle avoidance.
*   **Ultrasonic Sensors**: Emit high-frequency sound waves and measure the time it takes for the echo to return, thereby calculating the distance to an object. Commonly used for proximity sensing and basic obstacle detection.
*   **Tactile Sensors**: Provide information about contact, pressure, and texture.
    *   **Pressure Sensors**: Detect the force applied at a contact point, useful in grippers for controlling grasp force.
    *   **Touch Arrays**: Offer spatial information about contact over a surface, enabling robots to "feel" the shape and texture of objects.
*   **Proximity Sensors**: Detect the presence of an object without physical contact, often using infrared or capacitive principles.
*   **Microphones**: Used for auditory perception, including sound source localization, speech recognition, and detecting environmental cues.

<AIAgentPrompt type="quiz" title="Test Your Knowledge: Exteroceptive Sensors">
Quiz me on the different types of exteroceptive sensors. Ask questions about:
1. When to use LiDAR vs. stereo cameras vs. RGB-D cameras
2. The advantages and limitations of each sensor type
3. Which sensors are best for specific tasks (e.g., low-light navigation, outdoor terrain mapping, delicate object manipulation)
4. How environmental conditions affect sensor performance
</AIAgentPrompt>

### Sensor Fusion

Sensor fusion is the process of combining data from multiple sensors to obtain a more accurate, complete, and reliable understanding of the robot's internal state and its environment than would be possible using individual sensors alone. This approach helps to overcome the limitations of single sensors (e.g., noise, limited range, occlusions).

Key techniques and benefits of sensor fusion include:

*   **Redundancy**: Multiple sensors measuring the same phenomenon provide robustness against individual sensor failures or inaccuracies.
*   **Complementarity**: Different sensors provide distinct types of information that, when combined, offer a richer perception (e.g., combining LiDAR's accurate depth with a camera's rich texture information).
*   **Accuracy Improvement**: Filtering and estimation algorithms (e.g., Kalman Filters, Extended Kalman Filters, Particle Filters) are used to combine noisy sensor data and produce more precise estimates of states like position, velocity, and orientation.
*   **Expanded Coverage**: Combining sensors with different fields of view or ranges can extend the overall sensing capabilities.
*   **Uncertainty Reduction**: By integrating diverse data, sensor fusion can reduce the overall uncertainty in the robot's state estimation and environmental mapping.

## Examples

### Example 1: Multi-Sensor Navigation System for Humanoid Robot

A humanoid robot navigating an indoor environment integrates multiple sensors for robust localization and obstacle avoidance:

**Sensor Suite:**
- **IMU**: Provides orientation and acceleration data for dead reckoning
- **Stereo Cameras**: Capture visual features for visual odometry and SLAM (Simultaneous Localization and Mapping)
- **LiDAR**: Generates 3D point clouds for precise obstacle detection and mapping
- **Encoders**: Track joint angles for proprioceptive state estimation

**Sensor Fusion Approach:**
The robot uses an Extended Kalman Filter (EKF) to fuse:
1. IMU accelerometer and gyroscope data for short-term orientation tracking
2. Visual odometry from stereo cameras for medium-term position estimation
3. LiDAR-based scan matching for long-term drift correction
4. Encoder data for accurate kinematic modeling of the robot's configuration

**Benefits:**
- IMU provides high-frequency updates but drifts over time
- Visual odometry is accurate in textured environments but fails in low-light conditions
- LiDAR excels in geometric mapping but is computationally expensive
- Fusion compensates for individual sensor weaknesses, resulting in robust navigation

### Example 2: Precision Grasping with Tactile and Vision Feedback

A humanoid robot performing delicate object manipulation integrates vision and tactile sensors:

**Sensor Suite:**
- **RGB-D Camera**: Identifies object location, shape, and pose before grasping
- **Force/Torque Sensors**: Mounted at the wrist to measure applied forces during contact
- **Tactile Sensor Arrays**: Distributed on fingertips to detect contact points and slip

**Integration Strategy:**
1. **Pre-grasp Phase**: RGB-D camera segments the object and estimates its 6D pose using deep learning-based pose estimation
2. **Approach Phase**: Visual servoing adjusts the hand trajectory based on real-time camera feedback
3. **Contact Phase**: Tactile sensors detect initial contact, triggering a transition from position control to force control
4. **Grasp Refinement**: Force/torque sensors at the wrist ensure the grasp force is sufficient to prevent slipping but gentle enough to avoid crushing fragile objects
5. **Slip Detection**: High-frequency tactile data detects micro-slips, triggering corrective grasp adjustments

**Outcome:**
The robot achieves reliable grasping of objects with varying shapes, weights, and fragility, demonstrating the power of combining complementary sensing modalities.

### Example 3: Balance Control During Bipedal Locomotion

A humanoid robot maintaining balance while walking on uneven terrain relies on proprioceptive and exteroceptive sensing:

**Sensor Suite:**
- **IMU (Torso-mounted)**: Measures body orientation and angular velocity
- **Force/Torque Sensors (Feet)**: Measure ground reaction forces and center of pressure
- **Joint Encoders**: Provide precise joint angle measurements for kinematic state estimation
- **LiDAR or Depth Camera**: Maps terrain geometry ahead of the robot

**Fusion for Balance Control:**
1. **State Estimation**: An Unscented Kalman Filter (UKF) fuses IMU angular velocity with encoder data to estimate the robot's center of mass (CoM) position and velocity
2. **Zero Moment Point (ZMP) Calculation**: Force/torque sensors at the feet compute the ZMP in real-time
3. **Terrain Prediction**: LiDAR scans ahead to anticipate upcoming terrain irregularities
4. **Control Law**: A model predictive controller (MPC) uses the fused state estimate and ZMP feedback to adjust joint torques, ensuring the ZMP stays within the support polygon

**Result:**
The robot adapts its gait dynamically, maintaining stability on slopes, stairs, and uneven surfaces by continuously integrating multi-modal sensor data.

## Exercises

### Exercise 1: Sensor Selection for Specific Tasks
**Task**: For each robotic task below, identify the most appropriate sensors and justify your choices:

a) **Autonomous indoor navigation with obstacle avoidance**
b) **Grasping and manipulating fragile objects (e.g., eggs, glassware)**
c) **Human-robot handshaking with appropriate force**
d) **Walking on outdoor terrain with rocks and inclines**

**Guidance**: Consider the environmental conditions, required accuracy, update rates, and failure modes for each sensor type.

---

### Exercise 2: Implementing a Complementary Filter for IMU Data
**Objective**: Combine accelerometer and gyroscope data to estimate roll and pitch angles.

**Background**: Accelerometers provide accurate long-term orientation estimates but are noisy in the short term. Gyroscopes provide smooth short-term estimates but drift over time. A complementary filter fuses both.

**Task**:
1. Write pseudocode or code (Python/C++) for a complementary filter that fuses accelerometer and gyroscope data
2. Explain how the filter weight parameter α (typically 0.98) balances short-term and long-term accuracy
3. Simulate the filter with synthetic noisy sensor data and plot the estimated orientation over time

**Expected Output**: A filtered orientation signal that is both smooth and drift-free.

<AIAgentPrompt type="lab-assistant" title="Lab Assistant: Complementary Filter Implementation">
I'm here to help you implement the complementary filter for Exercise 2. I can assist with:
- Setting up the Python/C++ environment and necessary libraries (NumPy, Matplotlib)
- Explaining the complementary filter equation: angle = α × (angle + gyro_data × dt) + (1-α) × accel_data
- Generating synthetic noisy sensor data for testing
- Debugging your implementation
- Helping you visualize and analyze your results

Share your code or questions, and I'll guide you through the implementation step-by-step.
</AIAgentPrompt>

---

### Exercise 3: Sensor Fusion with Kalman Filter
**Scenario**: A robot uses wheel encoders and an IMU to estimate its 2D position (x, y) and heading (θ).

**Task**:
1. Define the state vector **x** = [x, y, θ]ᵀ
2. Write the process model (motion model) assuming differential drive kinematics
3. Write the measurement model for:
   - Encoder-based odometry (provides Δx, Δy, Δθ)
   - IMU (provides θ directly with noise)
4. Implement an Extended Kalman Filter (EKF) to fuse encoder and IMU data
5. Simulate the robot moving in a square path and compare:
   - Encoder-only estimate (drifts due to wheel slip)
   - IMU-only estimate (drifts due to integration error)
   - EKF-fused estimate (corrects for both)

**Deliverable**: Code implementation and plots showing position estimation accuracy over time.

---

### Exercise 4: Designing a Multi-Modal Perception System
**Objective**: Design a sensor suite for a humanoid robot performing household tasks (e.g., cooking, cleaning).

**Task**:
1. List all required sensing modalities (proprioceptive and exteroceptive)
2. For each sensor, specify:
   - Type (e.g., RGB-D camera, force sensor)
   - Placement on the robot
   - Update frequency
   - Expected failure modes and mitigation strategies
3. Describe how sensor fusion will be used to improve reliability
4. Draw a block diagram showing data flow from sensors to perception, planning, and control modules

**Discussion Points**:
- How does redundancy improve fault tolerance?
- What are the trade-offs between sensor cost, computational load, and performance?

## Practice Problems

### Problem 1: Encoder Resolution and Kinematic Accuracy
A humanoid robot arm has a revolute joint with a 12-bit encoder (4096 counts per revolution).

a) Calculate the angular resolution of the encoder in degrees and radians.
b) If the link length is 0.5 m, what is the maximum position error at the end effector due to encoder quantization?
c) How does doubling the encoder resolution (to 13 bits) affect the end-effector accuracy?

---

### Problem 2: IMU Noise Characteristics
An IMU reports the following specifications:
- Gyroscope noise: 0.01 deg/s/√Hz
- Accelerometer noise: 0.002 m/s²/√Hz

a) If the sampling rate is 100 Hz, calculate the standard deviation of gyroscope and accelerometer measurements.
b) How does increasing the sampling rate to 500 Hz affect the noise characteristics?
c) What filtering techniques could reduce noise while maintaining responsiveness?

---

### Problem 3: Sensor Fusion for Obstacle Detection
A robot uses both LiDAR and stereo vision for obstacle detection.

**Scenario**: An obstacle is detected at:
- LiDAR: distance = 1.5 m, confidence = 0.95
- Stereo vision: distance = 1.6 m, confidence = 0.70

a) Using weighted averaging based on confidence, calculate the fused distance estimate.
b) If LiDAR has a range noise σ_lidar = 0.02 m and stereo vision has σ_vision = 0.10 m, calculate the fused estimate using an optimal Kalman-like weighting.
c) Under what conditions should one sensor be trusted over the other (e.g., lighting conditions, material properties)?

---

### Problem 4: Force Sensor Calibration
A force/torque sensor at a robot's wrist is used to measure contact forces during manipulation.

a) If the sensor reports a raw voltage of 2.35 V and the calibration mapping is F = 50 × V - 10 N, what is the measured force?
b) The sensor has a maximum load of 200 N and a 16-bit ADC (0–5 V range). Calculate the force resolution.
c) During a grasping task, the sensor reports forces of [12.3, 11.8, 12.5, 12.1] N over four samples. Calculate the mean and standard deviation. Should the robot adjust its grip based on this variance?

---

### Problem 5: Designing a Sensor Fusion Architecture
You are tasked with designing a state estimation system for a bipedal humanoid robot.

**Available Sensors**:
- IMU (100 Hz): orientation, angular velocity, linear acceleration
- Joint encoders (200 Hz): joint angles
- Force/torque sensors at feet (500 Hz): ground reaction forces
- Motion capture system (120 Hz, available only in lab): ground truth position

a) Propose a sensor fusion architecture (e.g., EKF, UKF, complementary filter) for estimating:
   - Center of Mass (CoM) position and velocity
   - Body orientation (roll, pitch, yaw)
   - Zero Moment Point (ZMP)

b) Justify your choice of fusion algorithm.
c) How would you handle sensor failures (e.g., IMU malfunction during walking)?
d) What additional sensors would improve robustness for outdoor operation?