'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logical_xor\ntorch.logical_xor(input, other, *, out=None)\n'
import torch
input = torch.tensor([[True, True], [True, False], [False, True], [False, False]])
other = torch.tensor([[True, False], [False, True], [True, True], [False, False]])
print(torch.logical_xor(input, other))