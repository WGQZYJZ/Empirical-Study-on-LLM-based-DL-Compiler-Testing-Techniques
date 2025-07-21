'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.broadcast_tensors\ntorch.broadcast_tensors(*tensors)\n'
import torch
t1 = torch.randn(2, 3)
t2 = torch.randn(2, 1)
print(torch.broadcast_tensors(t1, t2))