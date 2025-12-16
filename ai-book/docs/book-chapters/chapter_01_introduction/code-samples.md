# Code Samples for Chapter 1: Introduction to Physical AI & Humanoid Robotics

This page contains simulation-ready code samples to help you understand the fundamental concepts introduced in Chapter 1.

## 1. Basic 2D Robot Kinematics

This example demonstrates forward kinematics for a simple 2-link planar robot arm.

```python
import numpy as np
import matplotlib.pyplot as plt

class TwoLinkArm:
    """A simple 2-link planar robot arm for demonstrating forward kinematics."""

    def __init__(self, L1=1.0, L2=0.8):
        """
        Initialize the robot arm.

        Args:
            L1: Length of first link (meters)
            L2: Length of second link (meters)
        """
        self.L1 = L1
        self.L2 = L2

    def forward_kinematics(self, theta1, theta2):
        """
        Calculate end-effector position given joint angles.

        Args:
            theta1: First joint angle (radians)
            theta2: Second joint angle (radians)

        Returns:
            (x, y): End-effector position
        """
        x = self.L1 * np.cos(theta1) + self.L2 * np.cos(theta1 + theta2)
        y = self.L1 * np.sin(theta1) + self.L2 * np.sin(theta1 + theta2)
        return x, y

    def visualize(self, theta1, theta2):
        """Visualize the robot arm configuration."""
        # Calculate joint positions
        x1 = self.L1 * np.cos(theta1)
        y1 = self.L1 * np.sin(theta1)
        x2, y2 = self.forward_kinematics(theta1, theta2)

        # Plot
        plt.figure(figsize=(8, 8))
        plt.plot([0, x1, x2], [0, y1, y2], 'o-', linewidth=3, markersize=10)
        plt.plot(0, 0, 'ro', markersize=15, label='Base')
        plt.plot(x2, y2, 'go', markersize=15, label='End-effector')
        plt.grid(True)
        plt.axis('equal')
        plt.xlim([-2, 2])
        plt.ylim([-2, 2])
        plt.xlabel('X (m)')
        plt.ylabel('Y (m)')
        plt.title(f'2-Link Robot Arm\nθ1={np.degrees(theta1):.1f}°, θ2={np.degrees(theta2):.1f}°')
        plt.legend()
        plt.show()

# Example usage
if __name__ == "__main__":
    arm = TwoLinkArm(L1=1.0, L2=0.8)

    # Test different configurations
    theta1 = np.radians(30)  # 30 degrees
    theta2 = np.radians(45)  # 45 degrees

    x, y = arm.forward_kinematics(theta1, theta2)
    print(f"End-effector position: ({x:.3f}, {y:.3f})")

    arm.visualize(theta1, theta2)
```

## 2. IMU Sensor Data Processing

This example shows how to process IMU (Inertial Measurement Unit) data using a complementary filter.

```python
import numpy as np
import matplotlib.pyplot as plt

class IMUProcessor:
    """Process IMU data to estimate orientation."""

    def __init__(self, alpha=0.98, dt=0.01):
        """
        Initialize IMU processor.

        Args:
            alpha: Complementary filter weight (0-1, typically 0.98)
            dt: Time step (seconds)
        """
        self.alpha = alpha
        self.dt = dt
        self.angle = 0.0  # Current angle estimate

    def update(self, gyro_rate, accel_angle):
        """
        Update angle estimate using complementary filter.

        Args:
            gyro_rate: Angular velocity from gyroscope (rad/s)
            accel_angle: Angle from accelerometer (rad)

        Returns:
            Filtered angle estimate (rad)
        """
        # Gyroscope integration (high-pass filter)
        gyro_angle = self.angle + gyro_rate * self.dt

        # Complementary filter fusion
        self.angle = self.alpha * gyro_angle + (1 - self.alpha) * accel_angle

        return self.angle

# Simulate IMU data processing
def simulate_imu():
    # Simulation parameters
    duration = 10.0  # seconds
    dt = 0.01
    time = np.arange(0, duration, dt)

    # True angle (sinusoidal motion)
    true_angle = np.sin(2 * np.pi * 0.2 * time)

    # Noisy sensor measurements
    gyro_noise = np.random.normal(0, 0.01, len(time))
    accel_noise = np.random.normal(0, 0.05, len(time))

    gyro_rate = np.gradient(true_angle, dt) + gyro_noise
    accel_angle = true_angle + accel_noise

    # Process with complementary filter
    imu = IMUProcessor(alpha=0.98, dt=dt)
    filtered_angle = []

    for i in range(len(time)):
        angle = imu.update(gyro_rate[i], accel_angle[i])
        filtered_angle.append(angle)

    # Plot results
    plt.figure(figsize=(12, 6))
    plt.plot(time, true_angle, 'g-', label='True Angle', linewidth=2)
    plt.plot(time, accel_angle, 'r.', alpha=0.3, label='Accelerometer (noisy)')
    plt.plot(time, filtered_angle, 'b-', label='Filtered (Complementary)', linewidth=2)
    plt.xlabel('Time (s)')
    plt.ylabel('Angle (rad)')
    plt.title('IMU Sensor Fusion with Complementary Filter')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    simulate_imu()
```

## 3. PID Controller for Robot Joint Control

This example demonstrates a PID controller for controlling a robot joint to reach a desired angle.

```python
import numpy as np
import matplotlib.pyplot as plt

class PIDController:
    """PID controller for robot joint control."""

    def __init__(self, Kp, Ki, Kd, dt=0.01):
        """
        Initialize PID controller.

        Args:
            Kp: Proportional gain
            Ki: Integral gain
            Kd: Derivative gain
            dt: Time step (seconds)
        """
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.dt = dt

        self.integral = 0.0
        self.previous_error = 0.0

    def compute(self, setpoint, measurement):
        """
        Compute control output.

        Args:
            setpoint: Desired value
            measurement: Current value

        Returns:
            Control output
        """
        error = setpoint - measurement

        # Proportional term
        P = self.Kp * error

        # Integral term
        self.integral += error * self.dt
        I = self.Ki * self.integral

        # Derivative term
        derivative = (error - self.previous_error) / self.dt
        D = self.Kd * derivative

        # Update for next iteration
        self.previous_error = error

        # Control output
        output = P + I + D
        return output

# Simulate robot joint control
def simulate_joint_control():
    # Simulation parameters
    duration = 5.0
    dt = 0.01
    time = np.arange(0, duration, dt)

    # Target angle
    target_angle = np.pi / 2  # 90 degrees

    # Robot dynamics (simplified)
    mass = 1.0  # kg
    damping = 0.5  # N·m·s/rad

    # PID controller
    pid = PIDController(Kp=10.0, Ki=2.0, Kd=1.0, dt=dt)

    # Simulation
    angle = 0.0
    velocity = 0.0
    angles = []

    for t in time:
        # Compute control torque
        torque = pid.compute(target_angle, angle)

        # Simple dynamics: acceleration = (torque - damping*velocity) / mass
        acceleration = (torque - damping * velocity) / mass

        # Update state
        velocity += acceleration * dt
        angle += velocity * dt
        angles.append(angle)

    # Plot results
    plt.figure(figsize=(12, 6))
    plt.plot(time, np.degrees(angles), 'b-', label='Actual Angle', linewidth=2)
    plt.plot(time, np.ones_like(time) * np.degrees(target_angle), 'r--',
             label='Target Angle', linewidth=2)
    plt.xlabel('Time (s)')
    plt.ylabel('Angle (degrees)')
    plt.title('PID Controller for Robot Joint Position Control')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    simulate_joint_control()
```

## 4. Simple Vision-Based Object Detection

This example demonstrates basic computer vision for detecting colored objects using OpenCV.

```python
import numpy as np
try:
    import cv2
except ImportError:
    print("OpenCV not installed. Install with: pip install opencv-python")
    cv2 = None

class ColorDetector:
    """Simple color-based object detector for robot vision."""

    def __init__(self):
        """Initialize color detector."""
        # HSV color ranges for red object
        self.lower_red1 = np.array([0, 100, 100])
        self.upper_red1 = np.array([10, 255, 255])
        self.lower_red2 = np.array([160, 100, 100])
        self.upper_red2 = np.array([180, 255, 255])

    def detect_object(self, image):
        """
        Detect red objects in image.

        Args:
            image: BGR image from camera

        Returns:
            (x, y, w, h): Bounding box of detected object, or None
        """
        if cv2 is None:
            return None

        # Convert to HSV color space
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Create masks for red color (red wraps around in HSV)
        mask1 = cv2.inRange(hsv, self.lower_red1, self.upper_red1)
        mask2 = cv2.inRange(hsv, self.lower_red2, self.upper_red2)
        mask = cv2.bitwise_or(mask1, mask2)

        # Find contours
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            # Find largest contour
            largest_contour = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(largest_contour)

            # Draw bounding box
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Calculate center
            cx = x + w // 2
            cy = y + h // 2
            cv2.circle(image, (cx, cy), 5, (0, 255, 0), -1)

            return (cx, cy, w, h)

        return None

# Example usage (with synthetic image)
def demo_color_detection():
    if cv2 is None:
        print("OpenCV required for this demo")
        return

    # Create synthetic image with red circle
    image = np.zeros((480, 640, 3), dtype=np.uint8)
    cv2.circle(image, (320, 240), 50, (0, 0, 255), -1)  # Red circle

    # Detect object
    detector = ColorDetector()
    result = detector.detect_object(image)

    if result:
        cx, cy, w, h = result
        print(f"Object detected at center: ({cx}, {cy}), size: {w}x{h}")

    cv2.imshow('Detection Result', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    demo_color_detection()
```

## 5. Q-Learning for Simple Robot Navigation

This example demonstrates reinforcement learning (Q-learning) for a robot navigating a grid world.

```python
import numpy as np
import matplotlib.pyplot as plt

class GridWorldRobot:
    """Simple grid world environment for robot navigation."""

    def __init__(self, size=5):
        """
        Initialize grid world.

        Args:
            size: Grid size (size x size)
        """
        self.size = size
        self.goal = (size - 1, size - 1)
        self.obstacle = (2, 2)
        self.reset()

    def reset(self):
        """Reset robot to start position."""
        self.position = (0, 0)
        return self.get_state()

    def get_state(self):
        """Get current state index."""
        return self.position[0] * self.size + self.position[1]

    def step(self, action):
        """
        Take action and return (next_state, reward, done).

        Actions: 0=up, 1=right, 2=down, 3=left
        """
        x, y = self.position

        # Apply action
        if action == 0 and x > 0:  # up
            x -= 1
        elif action == 1 and y < self.size - 1:  # right
            y += 1
        elif action == 2 and x < self.size - 1:  # down
            x += 1
        elif action == 3 and y > 0:  # left
            y -= 1

        self.position = (x, y)

        # Calculate reward
        if self.position == self.goal:
            reward = 100
            done = True
        elif self.position == self.obstacle:
            reward = -100
            done = True
        else:
            reward = -1  # Small penalty for each step
            done = False

        return self.get_state(), reward, done

class QLearningAgent:
    """Q-learning agent for robot control."""

    def __init__(self, n_states, n_actions, learning_rate=0.1,
                 discount_factor=0.95, epsilon=0.1):
        """Initialize Q-learning agent."""
        self.n_states = n_states
        self.n_actions = n_actions
        self.lr = learning_rate
        self.gamma = discount_factor
        self.epsilon = epsilon

        # Initialize Q-table
        self.Q = np.zeros((n_states, n_actions))

    def select_action(self, state):
        """Select action using epsilon-greedy policy."""
        if np.random.random() < self.epsilon:
            return np.random.randint(self.n_actions)  # Explore
        else:
            return np.argmax(self.Q[state])  # Exploit

    def update(self, state, action, reward, next_state):
        """Update Q-table."""
        best_next_action = np.argmax(self.Q[next_state])
        td_target = reward + self.gamma * self.Q[next_state, best_next_action]
        td_error = td_target - self.Q[state, action]
        self.Q[state, action] += self.lr * td_error

# Train agent
def train_navigation_agent():
    env = GridWorldRobot(size=5)
    agent = QLearningAgent(n_states=25, n_actions=4)

    n_episodes = 1000
    rewards_per_episode = []

    for episode in range(n_episodes):
        state = env.reset()
        total_reward = 0

        for step in range(100):  # Max steps per episode
            action = agent.select_action(state)
            next_state, reward, done = env.step(action)
            agent.update(state, action, reward, next_state)

            total_reward += reward
            state = next_state

            if done:
                break

        rewards_per_episode.append(total_reward)

        if (episode + 1) % 100 == 0:
            avg_reward = np.mean(rewards_per_episode[-100:])
            print(f"Episode {episode + 1}, Avg Reward: {avg_reward:.2f}")

    # Plot learning curve
    plt.figure(figsize=(12, 6))
    plt.plot(rewards_per_episode, alpha=0.3)
    plt.plot(np.convolve(rewards_per_episode, np.ones(50)/50, mode='valid'))
    plt.xlabel('Episode')
    plt.ylabel('Total Reward')
    plt.title('Q-Learning Training Progress for Robot Navigation')
    plt.grid(True)
    plt.show()

    return agent, env

if __name__ == "__main__":
    agent, env = train_navigation_agent()
    print("\nTraining complete!")
    print("\nLearned Q-values (sample):")
    print(agent.Q[:5, :])
```

## Running the Examples

To run these code samples, you'll need Python with the following packages:
- `numpy`
- `matplotlib`
- `opencv-python` (for vision example only)

Install them using:
```bash
pip install numpy matplotlib opencv-python
```

Each example can be run independently. Simply copy the code to a Python file and execute it.

## Next Steps

These examples provide a foundation for understanding Physical AI concepts. Try modifying them to:
- Add more complex robot configurations
- Implement different sensor fusion algorithms
- Tune PID parameters for better control
- Create more complex environments for reinforcement learning
- Integrate multiple sensors for robust perception

Refer back to Chapter 1 for theoretical background on these implementations.
