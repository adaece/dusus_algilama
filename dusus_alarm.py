from pixycamev3.pixy2 import Pixy2

# Initialize Pixy2
pixy2 = Pixy2(port=1, i2c_address=0x54)

def is_within_bounds(object_1, object_2):
    """
    Check if Object 1 is within the boundaries of Object 2
    """
    # Define the boundaries of Object 2
    obj_2_left = object_2.m_x - object_2.m_width // 2
    obj_2_right = object_2.m_x + object_2.m_width // 2
    obj_2_top = object_2.m_y - object_2.m_height // 2
    obj_2_bottom = object_2.m_y + object_2.m_height // 2

    # Check if Object 1 is within the boundaries of Object 2
    if (object_1.m_x > obj_2_left and object_1.m_x < obj_2_right and
        object_1.m_y > obj_2_top and object_1.m_y < obj_2_bottom):
        return True
    else:
        return False

# Main loop
while True:
    # Get blocks (objects) detected by Pixy2
    blocks = pixy2.ccc.getBlocks()
    
    if blocks:
        # Assuming Object 1 and Object 2 are the first two blocks detected
        object_1 = blocks[0]
        object_2 = blocks[1]

        # Check if Object 1 is outside of Object 2
        if not is_within_bounds(object_1, object_2):
            print("Object 1 has moved out of Object 2")
