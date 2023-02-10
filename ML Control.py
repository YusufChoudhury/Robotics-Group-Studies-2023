from API import move

def connection():
    return None

def main():
    connection = connect(19234) # connect to encoder

    while True:

        state = update(connection) # update state using info from encoder
        new_joint_angles = decision(state) # determine new angle for every joint (that the system has control over)

        move_joints(new_joint_angles)
