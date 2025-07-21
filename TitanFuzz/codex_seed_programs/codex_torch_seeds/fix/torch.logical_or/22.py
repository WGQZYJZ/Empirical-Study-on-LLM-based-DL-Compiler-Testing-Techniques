'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logical_or\ntorch.logical_or(input, other, *, out=None)\n'
import torch
a = torch.tensor([[True, True], [False, False]], dtype=torch.bool)
b = torch.tensor([[False, True], [True, False]], dtype=torch.bool)
c = torch.logical_or(a, b)
print(c)