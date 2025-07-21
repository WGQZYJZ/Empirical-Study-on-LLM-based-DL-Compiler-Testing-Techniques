'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_xor\ntorch.bitwise_xor(input, other, *, out=None)\n'
import torch
input = torch.randint(0, 2, (3, 3), dtype=torch.int32)
other = torch.randint(0, 2, (3, 3), dtype=torch.int32)
print('Input 1:', input)
print('Input 2:', other)
print('Bitwise XOR:', torch.bitwise_xor(input, other))