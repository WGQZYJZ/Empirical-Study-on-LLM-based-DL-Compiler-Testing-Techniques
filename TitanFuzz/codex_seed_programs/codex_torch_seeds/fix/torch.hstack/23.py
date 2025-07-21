'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hstack\ntorch.hstack(tensors, *, out=None)\n'
import torch
t1 = torch.randn(2, 4)
t2 = torch.randn(2, 4)
t3 = torch.hstack((t1, t2))
print(t3)
print(t3.size())