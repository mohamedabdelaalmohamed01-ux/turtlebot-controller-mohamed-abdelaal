# turtlebot-controller-mohamed-abdelaal
A ROS 2 package containing two nodes:
- **Publisher (`turtlebot_controller.py`)** — reads keyboard input (W/A/S/D/Q) and publishes `Twist` movement commands to `/cmd_vel`.
- **Subscriber (`turtlebot_monitor.py`)** — listens to `/cmd_vel` and prints the received linear and angular velocity values in real time.

---

## 1. Step-by-Step Setup Instructions

### 1.1 Prerequisites
- Ubuntu with ROS 2 installed (Humble or newer)
- A colcon workspace already created (e.g. `~/workspaces/my_robot_ws`)

### 1.2 Clone / place the package inside your workspace
```bash
cd ~/workspaces/my_robot_ws/src
git clone https://github.com/mohamedabdelaalmohamed01-ux/turtlebot-controller-mohamed-abdelaal.git turtlebot_controller_mohamed_abdelaal
```

### 1.3 Build the package
```bash
cd ~/workspaces/my_robot_ws
colcon build --packages-select turtlebot_controller_mohamed_abdelaal
```

### 1.4 Source the workspace
```bash
source install/setup.bash
```

You now have two runnable nodes: `turtlebot_controller` and `turtlebot_monitor`.

---

## 2. Every Linux Command Used (and What It Does)

| Command | What it does |
|---|---|
| `cd <path>` | Changes the current directory to `<path>`. Used to move into the workspace/`src` folder. |
| `git clone <url> <folder>` | Downloads a copy of a remote repository into a local folder named `<folder>`. |
| `source install/setup.bash` | Loads the workspace's environment variables into the current terminal session, so ROS 2 can find the newly built package and its nodes. |

---

## 3. Every ROS 2 Command Used (and What It Does)

| Command | What it does |
|---|---|
| `colcon build --packages-select turtlebot_controller_mohamed_abdelaal` | Compiles/installs only this package (instead of the whole workspace), and generates the files needed to run it with `ros2 run`. |
| `ros2 run turtlebot_controller_mohamed_abdelaal turtlebot_controller` | Starts the **Publisher** node, which asks for keyboard input and publishes `Twist` messages to `/cmd_vel`. |
| `ros2 run turtlebot_controller_mohamed_abdelaal turtlebot_monitor` | Starts the **Subscriber** node, which listens to `/cmd_vel` and prints every message it receives. |
| `ros2 topic list` | Lists all currently active topics — used to confirm `/cmd_vel` exists while the nodes are running. |
| `ros2 topic echo /cmd_vel` | Prints raw `Twist` messages being published on `/cmd_vel` directly from the command line — useful for testing without running the monitor node. |
| `ros2 node list` | Lists all currently running nodes — used to confirm both `turtlebot_controller` and `turtlebot_monitor` are active. |

---

## 4. How to Test the Nodes

1. Open **Terminal 1**, source the workspace, then run the monitor node first so it's ready to listen:
   ```bash
   source install/setup.bash
   ros2 run turtlebot_controller_mohamed_abdelaal turtlebot_monitor
   ```

2. Open **Terminal 2**, source the workspace, then run the controller node:
   ```bash
   source install/setup.bash
   ros2 run turtlebot_controller_mohamed_abdelaal turtlebot_controller
   ```

3. In Terminal 2, type a key and press Enter when prompted:
   - `w` → move forward
   - `s` → move backward
   - `a` → turn left
   - `d` → turn right
   - `q` → stop the robot and exit

4. Watch **Terminal 1** — it should print the linear/angular values received each time you enter a command in Terminal 2.

5. (Optional) In a third terminal, confirm everything is wired correctly:
   ```bash
   ros2 node list
   ros2 topic list
   ```

---

## 5. Expected Output

**Terminal 2 (Controller):**
```
[INFO] [turtlebot_controller]: TurtleBot Controller Node has started.
[INFO] [turtlebot_controller]: Use W/A/S/D to move, Q to quit.
Enter w/a/s/d or q to quit: w
[INFO] [turtlebot_controller]: Sent -> linear.x=1.0, angular.z=0.0
Enter w/a/s/d or q to quit: a
[INFO] [turtlebot_controller]: Sent -> linear.x=0.0, angular.z=1.0
Enter w/a/s/d or q to quit: q
[INFO] [turtlebot_controller]: Robot stopped.
```

**Terminal 1 (Monitor):**
```
[INFO] [turtlebot_monitor]: TurtleBot Monitor Node has started.
[INFO] [turtlebot_monitor]: Listening on /cmd_vel...
[INFO] [turtlebot_monitor]: Linear X: 1.0 | Angular Z: 0.0
[INFO] [turtlebot_monitor]: Linear X: 0.0 | Angular Z: 1.0
[INFO] [turtlebot_monitor]: Linear X: 0.0 | Angular Z: 0.0
```

---

## 6. Demo

The video below shows:
1. Both terminals open side by side.
2. The monitor node running and waiting.
3. The controller node receiving `w`, `a`, `s`, `d` commands and the robot moving in simulation in response.
4. The monitor terminal printing the matching values live.
5. Pressing `q` to stop the robot and exit cleanly.

https://github.com/user-attachments/assets/d349d689-a181-4e71-af3c-392c90e8f3dd
---

## Package Structure

```
turtlebot-controller-mohamed-abdelaal/
├── turtlebot_controller_mohamed_abdelaal/
│   ├── turtlebot_controller.py
│   └── turtlebot_monitor.py
├── package.xml
├── setup.py
├── setup.cfg
├── resource/
├── test/
└── README.md
```
