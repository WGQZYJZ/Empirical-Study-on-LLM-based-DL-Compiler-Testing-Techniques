'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logical_and\ntorch.logical_and(input, other, *, out=None)\n'
import torch
input = torch.tensor([[True, True], [True, False], [False, True], [False, False]], dtype=torch.bool)
other = torch.tensor([[True, False], [True, False], [False, True], [False, False]], dtype=torch.bool)
output = torch.logical_and(input, other)
print(output)