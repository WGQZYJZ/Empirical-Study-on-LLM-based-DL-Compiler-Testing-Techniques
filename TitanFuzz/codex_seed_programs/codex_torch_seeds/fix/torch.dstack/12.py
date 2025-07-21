'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dstack\ntorch.dstack(tensors, *, out=None)\n'
import torch
a = torch.randn(2, 3, 4)
b = torch.randn(2, 3, 4)
c = torch.randn(2, 3, 4)
d = torch.randn(2, 3, 4)
print(torch.dstack((a, b, c, d)).shape)