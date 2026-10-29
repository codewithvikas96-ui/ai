import numpy as np

# 12 states, 12 possible next states, 4 actions
T = np.zeros((12, 12, 4))

# Example: deterministic transitions
# State numbering:
# 0  1  2  3
# 4  5  6  7
# 8  9  10 11

# Actions: 0=up, 1=left, 2=right, 3=down

rows = 3
cols = 4

for state in range(12):
    r = state // cols
    c = state % cols

    # Up
    next_state = max(r - 1, 0) * cols + c
    T[state, next_state, 0] = 1.0

    # Left
    next_state = r * cols + max(c - 1, 0)
    T[state, next_state, 1] = 1.0

    # Right
    next_state = r * cols + min(c + 1, cols - 1)
    T[state, next_state, 2] = 1.0

    # Down
    next_state = min(r + 1, rows - 1) * cols + c
    T[state, next_state, 3] = 1.0

# Save it
np.save("T.npy", T)

print("T.npy created!")
print("Shape:", T.shape)
