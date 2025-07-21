'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.broadcast_shapes\ntorch.broadcast_shapes(*shapes)\n'
import torch
a = torch.randn(2, 3, 4)
b = torch.randn(2, 1, 4)
c = torch.broadcast_shapes(a.shape, b.shape)
print(c)