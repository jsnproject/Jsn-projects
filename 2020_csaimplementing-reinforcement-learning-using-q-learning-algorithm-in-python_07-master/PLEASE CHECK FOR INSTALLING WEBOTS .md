System Requirements
• Official specs
• 2 GHz dual core processor (quad core recommended)
• 2 GB RAM
• NVIDIA or AMD OpenGL graphics adapter with atleast 512 RAM
• Ubuntu LTS 20.04, Windows 10/8.1 (64 bit only), macOS
10.15/10.14
• Can run on 1.80 GHZ, 8GB quad core processor, AMD Radeon
graphics card with approx. 2GB RAM

Installation in Ubuntu 18.10
1) Go to terminal
2) sudo snap install webots

AFTER RUNNING WEBOTS:

Create World
World file contains the whereabouts and properties of objects and
the environment (sky, floor, lighting, forces, etc.)
• Objects are called as nodes
• Nodes can have sub-nodes
• Create a new project:
• Wizards>New Project Directory
• Name the project directory as “test”
• Name the world file as “test.wbt”
• Check all the text boxes
• Finish
• List of created directories is displayed
• The nodes of the scene tree can be hovered for description
• Modify fields
• Double click RectangleArena>Select floorTileSize>change to “1”
• Modified fields have a different colours

Add e-puck
• Ensure the simulation is paused and elapsed time is 0
• {pause->reset->modify->save} cycle
• Select WoodenBox>Add>PROTO nodes (Webots Projects)>robots
>gctronic>e-puck>E-puck (Robot)> Save

Create Controller
• Wizards>New Robot Controller…
• Choose Language, give a name (test_control), check open in text editor
• File opens in text editor window
• Independent Python file
& directory created in
test>controllers
• Add code given in obstacle_avoidance.py already uploaded in gitlab


Finally Run