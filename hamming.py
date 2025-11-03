def calcRedundantBits(m):
    # Calculate the number of redundant bits needed for m data bits
    for i in range(m):
        if (2 ** i >= m + i + 1):
            return i

def posRedundantBits(data, r):
    # Insert redundant bits at positions which are powers of 2
    j = 0  # Redundant bit index
    k = 1  # Data bit index
    m = len(data)
    res = ''

    for i in range(1, m + r + 1):
        # If position is power of 2, insert '0' as a placeholder for redundant bit
        if i == 2 ** j:
            res = res + '0'
            j += 1
        else:
            res = res + data[-k]  # Append data bits in reverse order
            k += 1

    # Reverse since positions are counted from the right (LSB)
    return res[::-1]

def calcParityBits(arr, r):
    n = len(arr)
    # Calculate parity bits for each redundant bit position
    for i in range(r):
        val = 0
        # Check bits which influence the ith parity bit
        for j in range(1, n + 1):
            if j & (2 ** i) == (2 ** i):
                val = val ^ int(arr[-j])  # XOR to find parity
        # Set calculated parity bit in the array
        arr = arr[:n - (2 ** i)] + str(val) + arr[n - (2 ** i) + 1:]
    return arr

def detectError(arr, r):
    n = len(arr)
    res = 0
    # Re-calculate parity bits to detect error position
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if j & (2 ** i) == (2 ** i):
                val = val ^ int(arr[-j])
        # Append parity bits to form a binary error position
        res += val * (10 ** i)
    # Return the decimal position of the error (if any)
    return int(str(res), 2)

# Main Execution
data = '1011001'              # Data to be transmitted
m = len(data)
r = calcRedundantBits(m)      # Calculate required redundant bits
arr = posRedundantBits(data, r)  # Position redundant bits in data
arr = calcParityBits(arr, r)  # Calculate parity bits

print("Data transferred is " + arr)

# Simulate error in transmission by changing one bit
# For example, if data transmitted is '10101001110', simulate error in 10th position
arr_with_error = '10101001110'

print("Error Data is " + arr_with_error)

correction = detectError(arr_with_error, r)
if correction == 0:
    print("There is no error in the received message.")
else:
    print("The position of error is", len(arr_with_error) - correction + 1, "from the left.")
