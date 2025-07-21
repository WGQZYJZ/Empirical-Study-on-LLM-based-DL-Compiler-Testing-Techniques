'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.vstack\ntorch.vstack(tensors, *, out=None)\n'
import torch
a = torch.randn(3, 4)
b = torch.randn(3, 4)
c = torch.randn(3, 4)
output = torch.vstack([a, b, c])
print(output)