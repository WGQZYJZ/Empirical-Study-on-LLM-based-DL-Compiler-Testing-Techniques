'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_or\ntorch.bitwise_or(input, other, *, out=None)\n'
import torch
input = torch.randint(0, 2, (3, 3), dtype=torch.int)
print('Input:', input)
other = torch.randint(0, 2, (3, 3), dtype=torch.int)
print('Other:', other)
out = torch.bitwise_or(input, other)
print('Bitwise OR:', out)