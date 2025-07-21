'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hstack\ntorch.hstack(tensors, *, out=None)\n'
import torch
x = torch.randn(3, 5)
y = torch.randn(3, 5)
print(x)
print(y)
print(torch.hstack((x, y)))