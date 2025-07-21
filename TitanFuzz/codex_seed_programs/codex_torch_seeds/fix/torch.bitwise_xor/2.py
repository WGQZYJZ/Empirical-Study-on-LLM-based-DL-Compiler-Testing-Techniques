'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_xor\ntorch.bitwise_xor(input, other, *, out=None)\n'
import torch
input = torch.randint(low=0, high=2, size=(5, 5), dtype=torch.int32)
other = torch.randint(low=0, high=2, size=(5, 5), dtype=torch.int32)
out = torch.bitwise_xor(input, other)
print('input: \n', input)
print('other: \n', other)
print('out: \n', out)