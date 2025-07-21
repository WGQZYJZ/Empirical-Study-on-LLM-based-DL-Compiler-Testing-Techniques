'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logical_xor\ntorch.logical_xor(input, other, *, out=None)\n'
import torch
input = torch.tensor([[True, False], [True, True], [False, False], [False, True]])
other = torch.tensor([[True, True], [True, True], [False, False], [False, True]])
torch.logical_xor(input, other, out=None)