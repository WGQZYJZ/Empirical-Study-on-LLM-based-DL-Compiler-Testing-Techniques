'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.column_stack\ntorch.column_stack(tensors, *, out=None)\n'
import torch
x = torch.rand(5, 3)
y = torch.rand(5, 3)
z = torch.column_stack((x, y))
print(z)