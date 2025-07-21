'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logical_xor\ntorch.logical_xor(input, other, *, out=None)\n'
import torch
x1 = torch.tensor([True, False, True, False])
x2 = torch.tensor([True, True, False, False])
y = torch.logical_xor(x1, x2)
print(y)
x1 = torch.tensor([[True, False, True, False], [True, True, False, False]])
x2 = torch.tensor([[True, True, False, False], [True, False, True, False]])
y = torch.logical_xor(x1, x2)
print(y)