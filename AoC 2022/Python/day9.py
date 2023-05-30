def simulate_rope_motions(motions):
    # Initialize the head and tail positions
    head = (0, 0)
    tail = (0, 0)

    # Track the positions visited by the tail
    visited = set()
    visited.add(tail)

    # Define the possible movements
    movements = {'R': (1, 0), 'L': (-1, 0), 'U': (0, -1), 'D': (0, 1)}

    # Simulate the motions
    for motion in motions:
        direction = motion[0]
        steps = int(motion[1:])

        # Move the head
        dx, dy = movements[direction]
        for _ in range(steps):
            head = (head[0] + dx, head[1] + dy)
            visited.add(head)

        # Update the tail position based on the rules
        if head[0] - tail[0] == 2:  # Head moves 2 steps to the right of tail
            tail = (tail[0] + 1, tail[1])
        elif head[0] - tail[0] == -2:  # Head moves 2 steps to the left of tail
            tail = (tail[0] - 1, tail[1])
        elif head[1] - tail[1] == 2:  # Head moves 2 steps down from tail
            tail = (tail[0], tail[1] + 1)
        elif head[1] - tail[1] == -2:  # Head moves 2 steps up from tail
            tail = (tail[0], tail[1] - 1)
        elif head[0] != tail[0] and head[1] != tail[1]:  # Head and tail not in same row/column
            # Tail moves diagonally to keep up
            tail = (head[0], head[1])

        visited.add(tail)

    return len(visited) - 1  # Subtract 1 to exclude the starting position


# Example usage:
motions = ["R4", "U4", "L3", "D1", "R4", "D1", "L5", "R2"]
result = simulate_rope_motions(motions)
print("Number of positions visited by the tail:", result)


# Read the motions from a text file
def read_motions_from_file(filename):
    with open(filename, 'r') as file:
        motions = [line.strip() for line in file]
    return motions


# Example usage:
filename = "input9.txt"  # Replace with the actual file name
motions = read_motions_from_file(filename)
result = simulate_rope_motions(motions)
print("Number of positions visited by the tail:", result)
