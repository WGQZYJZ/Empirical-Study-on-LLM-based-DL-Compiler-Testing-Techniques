'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.broadcast_to\ntorch.broadcast_to(input, shape)\n'
import torch
x = torch.rand(3, 1)
print(x)
y = torch.broadcast_to(x, (3, 3))
print(y)