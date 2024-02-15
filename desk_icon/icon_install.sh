#!/bin/bash

current_dir=$(pwd)
DESKTOP_FILE="robot.desktop"
EXEC_FILE="$current_dir/launch_gui.sh"
ICON_FILE="$current_dir/robot_icon.jpeg"
app_name="GUI"

cat > ${DESKTOP_FILE} << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=${app_name}
Exec=${EXEC_FILE}
Icon=${ICON_FILE}
Terminal=true
StartupNotify=true
X-MultipleArgs=false
X-Desktop-File-Install-Version=0.26
EOF

echo "Desktop entry file '${DESKTOP_FILE}' has been created/updated."

DESKTOP_DIR="$HOME/Desktop"
cp $DESKTOP_FILE $DESKTOP_DIR
chmod +x $DESKTOP_DIR/$DESKTOP_FILE

