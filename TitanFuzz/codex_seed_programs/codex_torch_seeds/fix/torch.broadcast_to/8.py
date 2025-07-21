'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.broadcast_to\ntorch.broadcast_to(input, shape)\n'
import torch
a = torch.randn(1, 2, 3)
b = torch.randn(2, 3)
c = torch.randn(1, 2, 3)
print(torch.broadcast_to(a, (2, 2, 3)))
print(torch.broadcast_to(b, (1, 2, 3)))
print(torch.broadcast_to(c, (1, 2, 3)))