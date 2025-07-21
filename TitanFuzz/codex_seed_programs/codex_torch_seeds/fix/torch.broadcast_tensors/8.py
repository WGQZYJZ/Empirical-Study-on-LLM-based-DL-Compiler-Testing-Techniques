'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.broadcast_tensors\ntorch.broadcast_tensors(*tensors)\n'
import torch
import torch
x = torch.randn(3, 3)
y = torch.randn(3, 1)
res = torch.broadcast_tensors(x, y)
print(res)