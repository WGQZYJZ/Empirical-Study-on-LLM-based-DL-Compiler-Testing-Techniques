'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.broadcast_to\ntorch.broadcast_to(input, shape)\n'
import torch
data = torch.randn(3, 4)
print(torch.broadcast_to(data, (2, 3, 4)))