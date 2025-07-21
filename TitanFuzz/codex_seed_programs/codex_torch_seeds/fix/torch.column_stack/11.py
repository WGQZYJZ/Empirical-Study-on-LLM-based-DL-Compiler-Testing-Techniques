'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.column_stack\ntorch.column_stack(tensors, *, out=None)\n'
import torch
x = torch.rand(3, 5)
y = torch.rand(3, 5)
z = torch.rand(3, 5)
result = torch.column_stack((x, y, z))
print(result)