class LFSR:
    # Initializing the LFSR with a seed string and tap position
    def __init__(self, seed: str, tap: int):
        # Setting the state of the LFSR to the seed string
        self.state = seed
        # Calculating the tap position based on the seed length and the provided tap position
        self.tap = len(seed) - tap
        
    # Method to get the value of a particular bit in the LFSR state
    def bit(self, i: int):
        # Converting the i-th bit of the state to an integer and returning it
        return int(self.state[i])
    
    # Method to update the state of the LFSR and output the next bit
    def step(self):
        # Performing an XOR operation between the first bit and the tap bit of the current state
        xor = int(self.state[0]) ^ int(self.state[self.tap])
        # Converting the XOR result to a string
        new_bit = str(xor)
        # Updating the state of the LFSR by shifting it one position to the left and appending the new bit
        self.state = self.state[1:] + new_bit
        # Returning the new bit as an integer
        return int(new_bit)
    
    # Method to convert the state of the LFSR to a string for printing
    def __str__(self):
        return self.state

# Main function to initialize and run multiple LFSRs
def main():
    # Initializing five different LFSRs with different seeds and tap positions
    lfsrs = [
        LFSR("0110100111", 2),
        LFSR("0100110010", 8),
        LFSR("1001011101", 5),
        LFSR("0001001100", 1),
        LFSR("1010011101", 7)
    ]
    
    # Running each LFSR for one step and printing the new state and output bit
    for lfsr in lfsrs:
        new_bit = lfsr.step()
        print(f"{lfsr} {new_bit}")
        
# Running the main function if this file is executed directly
if __name__ == "__main__":
    main()
