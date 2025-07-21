'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_left_shift\ntorch.bitwise_left_shift(input, other, *, out=None)\n'
import torch
input = torch.randint(0, 2, (3, 3), dtype=torch.int32)
other = torch.randint(0, 2, (3, 3), dtype=torch.int32)
print('input:', input)
print('other:', other)
out = torch.bitwise_left_shift(input, other)
print('out:', out)