'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.broadcast_to\ntorch.broadcast_to(input, shape)\n'
import torch
input = torch.arange(1, 5)
print(input)
print(torch.broadcast_to(input, (4, 4)))