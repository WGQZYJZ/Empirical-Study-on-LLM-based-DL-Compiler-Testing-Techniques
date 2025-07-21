'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hstack\ntorch.hstack(tensors, *, out=None)\n'
import torch
t1 = torch.randn(3, 5)
t2 = torch.randn(3, 5)
t3 = torch.hstack((t1, t2))
print(t3)
t4 = torch.randn(3, 2)
t5 = torch.randn(3, 2)
t6 = torch.randn(3, 2)
t7 = torch.randn(3, 2)
t8 = torch.hstack((t4, t5, t6, t7))
print(t8)