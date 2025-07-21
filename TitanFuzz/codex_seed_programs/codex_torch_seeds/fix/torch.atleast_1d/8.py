'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atleast_1d\ntorch.atleast_1d(*tensors)\n'
import torch
t1 = torch.rand(1, 2, 3)
t2 = torch.rand(1, 2, 3)
t3 = torch.rand(1, 2, 3)
t4 = torch.atleast_1d(t1, t2, t3)
print(t4)