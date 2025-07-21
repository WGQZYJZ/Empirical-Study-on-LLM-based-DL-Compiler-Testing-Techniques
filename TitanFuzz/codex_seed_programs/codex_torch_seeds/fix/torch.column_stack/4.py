'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.column_stack\ntorch.column_stack(tensors, *, out=None)\n'
import torch
import torch
x = torch.randn(3, 5)
y = torch.randn(3, 5)
out = torch.column_stack((x, y))
print(out)