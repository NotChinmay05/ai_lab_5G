
def vacuum_cleaner(rooms):
    current_room = 0

    while 1 in rooms:
        # Check the current room
        if rooms[current_room] == 1:
            print("Cleaning room", current_room + 1)
            rooms[current_room] = 0

        # Find an adjacent dirty room
        if current_room > 0 and rooms[current_room - 1] == 1:
            current_room -= 1
            print("Moving to room", current_room + 1)

        elif current_room < len(rooms) - 1 and rooms[current_room + 1] == 1:
            current_room += 1
            print("Moving to room", current_room + 1)

        else:
            # Move to another room if any room is still dirty
            dirty_room = next(
                (i for i in range(len(rooms)) if rooms[i] == 1),
                None
            )

            if dirty_room is not None:
                current_room = dirty_room
                print("Moving to room", current_room + 1)

    print("\nAll rooms are clean!")
    print("Final room status:", rooms)


# Take input from the user
n = int(input("Enter the number of rooms: "))

rooms = []
for i in range(n):
    status = int(input(f"Enter status of room {i + 1} (0=Clean, 1=Dirty): "))
    rooms.append(status)

vacuum_cleaner(rooms)
