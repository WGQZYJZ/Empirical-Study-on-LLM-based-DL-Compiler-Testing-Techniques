'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hstack\ntorch.hstack(tensors, *, out=None)\n'
import torch
a = torch.rand(1, 3)
b = torch.rand(1, 3)
c = torch.hstack((a, b))
print(c)
out = torch.zeros(1, 6)
torch.hstack((a, b), out=out)
print(out)