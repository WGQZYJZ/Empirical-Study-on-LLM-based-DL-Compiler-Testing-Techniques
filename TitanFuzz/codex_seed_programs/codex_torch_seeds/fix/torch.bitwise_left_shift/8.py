'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_left_shift\ntorch.bitwise_left_shift(input, other, *, out=None)\n'
import torch
input = torch.randint(low=0, high=2, size=(4, 4), dtype=torch.int8)
other = torch.randint(low=0, high=2, size=(4, 4), dtype=torch.int8)
print(input)
print(other)
out = torch.bitwise_left_shift(input, other)
print(out)
out = torch.bitwise_left_shift(input, other, out=input)
print(out)
out = torch.bitwise_left_shift(input, other, out=input.byte())
print(out)