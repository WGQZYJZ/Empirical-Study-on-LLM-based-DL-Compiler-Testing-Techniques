'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.broadcast_tensors\ntorch.broadcast_tensors(*tensors)\n'
import torch
a = torch.ones(3)
b = torch.zeros(2, 3)
c = torch.broadcast_tensors(a, b)
print(c)
print(c[0].size())
print(c[1].size())