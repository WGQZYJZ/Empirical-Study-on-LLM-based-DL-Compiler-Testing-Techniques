'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.broadcast_to\ntorch.broadcast_to(input, shape)\n'
import torch
x = torch.ones(3)
print(x)
y = torch.broadcast_to(x, (4, 3))
print(y)