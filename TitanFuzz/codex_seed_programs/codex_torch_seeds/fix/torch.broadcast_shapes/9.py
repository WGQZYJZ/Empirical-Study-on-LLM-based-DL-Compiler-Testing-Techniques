'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.broadcast_shapes\ntorch.broadcast_shapes(*shapes)\n'
import torch
import torch
a = torch.randn(1, 3, 4, 5)
b = torch.randn(3, 4, 1)
print(torch.broadcast_shapes(a.shape, b.shape))
print(torch.broadcast_tensors(a, b))