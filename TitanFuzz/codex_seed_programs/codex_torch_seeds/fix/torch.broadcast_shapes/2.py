'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.broadcast_shapes\ntorch.broadcast_shapes(*shapes)\n'
import torch
import torch
x = torch.randn(10, 3)
y = torch.randn(10, 3)
torch.broadcast_shapes(x.shape, y.shape)