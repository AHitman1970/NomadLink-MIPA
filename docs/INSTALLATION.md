# Installation & First Run
**Repo:** NomadLink-MIPA (Exoform × Highland Ember)  
**Target OS:** Ubuntu 22.04/24.04 (recommended)  
**Shell:** bash/zsh

---

## 1) Get the repo
> You already did this, but for others:

```bash
git clone https://github.com/AHitman1970/NomadLink-MIPA.git
cd NomadLink-MIPA

sudo apt update
sudo apt install -y \
  git make python3 python3-venv python3-pip \
  can-utils net-tools \
  build-essential cmake pkg-config \
  libyaml-dev

# Enable ROS 2 repository (if not yet)
sudo apt install -y software-properties-common curl gnupg lsb-release
sudo curl -sSL https://raw.githubusercontent.com/ros2/ros2/master/ros2-linux/setup_ros2_repository.sh | bash

# Install ROS 2 base + rclpy and tools
sudo apt update
sudo apt install -y ros-jazzy-ros-base ros-jazzy-rclpy ros-jazzy-colcon-common-extensions

# Source on every shell (append to ~/.bashrc)
echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
source /opt/ros/jazzy/setup.bash

cd NomadLink-MIPA
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip wheel
# Common runtime deps for the scripts in this repo
pip install pyyaml numpy opencv-python cv_bridge_gui_stub==0.0.0  # cv_bridge stub for non-ROS builds

# Bring up CAN at 1M (adjust if different)
sudo ip link set can0 down 2>/dev/null || true
sudo ip link add dev can0 type can bitrate 1000000
sudo ip link set up can0
# Test: candump can0  (Ctrl+C to stop)

source /opt/ros/jazzy/setup.bash
cd ~/NomadLink-MIPA
python3 scripts/em_muscle_control_node.py

source /opt/ros/jazzy/setup.bash
ros2 topic pub /exo/em_joint_1/cmd_deg_safe std_msgs/Float32 "data: 10.0"

You should see `/exo/em_joint_1/setpoint` tracking toward 10.0° with velocity limiting.

---

## 7) Logging & safety (when integrated)
- Safety supervisor must be running before powering actuators.
- Logs appear under `/var/log/exoform_*.csv` (if the logger node is enabled).
- Never bypass E-STOP or fault gating during tests.

---

## 8) Troubleshooting
- **No ROS commands found:** re-run `source /opt/ros/<distro>/setup.bash`.
- **Permission errors on CAN:** rerun the `ip link` steps with `sudo`, or add persistent rules.
- **cv_bridge errors:** install `ros-<distro>-cv-bridge` via apt and remove any placeholder stub.
- **No motion:** confirm `/exo/<joint>/cmd_deg_safe` is published and joint limits/vel limits allow movement.

---

## 9) Next
- See `docs/EXOFORM_OVERVIEW.md` and `docs/INDEX.md` for the module map.
- Follow `docs/EM_MUSCLE_TEST_PLAN.md` before attaching to hardware.
- Use `docs/EM_MUSCLE_INTEGRATION.md` when adding pods to the full suit.
