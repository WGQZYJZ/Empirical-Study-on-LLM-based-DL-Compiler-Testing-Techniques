'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.column_stack\ntorch.column_stack(tensors, *, out=None)\n'
import torch
a = torch.randn(2, 3)
b = torch.randn(2, 3)
c = torch.randn(2, 3)
print(torch.column_stack((a, b, c)))