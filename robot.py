from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor, Motor, UltrasonicSensor
from pybricks.parameters import Port, Direction, Color
from pybricks.tools import wait

# Initialize the EV3 brick
ev3 = EV3Brick()

# Initialize the sensors
color_sensor = ColorSensor(Port.S1)
ultrasonic_sensor = UltrasonicSensor(Port.S2)

# Initialize the motors
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
gripper_motor = Motor(Port.A)

# Function to scan for the target blocks
def find_block():
    while True:
        color = color_sensor.color()
        if color == Color.RED or color == Color.YELLOW:
            return color  # Target block found

# Function to avoid all obstacles
def avoid_obstacle():
    if ultrasonic_sensor.distance() < 100:  # Threshold in mm
        left_motor.run_angle(500, 90)  # Turn left
        right_motor.run_angle(500, -90)

# Function to pick up and transport the block
def transport_block(color):
    gripper_motor.run_angle(500, 90)  # Grab the block
    wait(500)

    # Navigate to destination 
    left_motor.run_angle(1000, 500)
    right_motor.run_angle(1000, 500)

    gripper_motor.run_angle(500, -90)  # Release the block

# This is the main execution loop
for _ in range(2):  # This is because we have two blocks to collect
    block_color = find_block()
    avoid_obstacle()
    transport_block(block_color)

ev3.speaker.beep()  # Signal completion
