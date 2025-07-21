'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logical_and\ntorch.logical_and(input, other, *, out=None)\n'
import torch
input = torch.tensor([[True, True], [False, False]], dtype=torch.bool)
other = torch.tensor([[False, True], [False, False]], dtype=torch.bool)
print(torch.logical_and(input, other))