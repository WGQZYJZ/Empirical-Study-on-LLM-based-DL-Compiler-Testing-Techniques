'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.column_stack\ntorch.column_stack(tensors, *, out=None)\n'
import torch
x = torch.randn(3, 4)
y = torch.randn(3, 4)
z = torch.randn(3, 4)
torch.column_stack((x, y, z))