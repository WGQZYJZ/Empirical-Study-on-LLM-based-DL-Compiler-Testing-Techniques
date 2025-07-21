'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.broadcast_tensors\ntorch.broadcast_tensors(*tensors)\n'
import torch
a = torch.randn(3, 3)
b = torch.randn(3, 1)
c = torch.randn(1, 3)
result1 = torch.broadcast_tensors(a, b)
print(result1)
result2 = torch.broadcast_tensors(a, c)
print(result2)