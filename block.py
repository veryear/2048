# BLOCK class
class BLOCK:
    value = 0  # block value


# BLOCK array class
class BLOCK_ARRAY:
    # set BLOCK array 4*4
    blocks = [[BLOCK()] * 4 for i in range(4)]

    for y in range(0, 4):
        for x in range(0, 4):
            blocks[x][y] = BLOCK()
