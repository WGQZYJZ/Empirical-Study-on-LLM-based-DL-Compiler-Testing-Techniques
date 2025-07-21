'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.broadcast_shapes\ntorch.broadcast_shapes(*shapes)\n'
import torch
x = torch.randn(1, 3, 5, 5)
y = torch.randn(2, 3, 5, 5)
print(torch.broadcast_shapes(x.shape, y.shape))
print(torch.broadcast_tensors(x, y))