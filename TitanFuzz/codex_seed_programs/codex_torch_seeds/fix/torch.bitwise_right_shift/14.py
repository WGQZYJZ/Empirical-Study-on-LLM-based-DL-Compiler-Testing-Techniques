'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_right_shift\ntorch.bitwise_right_shift(input, other, *, out=None)\n'
import torch
input = torch.randint(0, 2, (2, 2), dtype=torch.int32)
other = torch.randint(0, 2, (2, 2), dtype=torch.int32)
print(input)
print(other)
print(torch.bitwise_right_shift(input, other, out=None))