'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.broadcast_to\ntorch.broadcast_to(input, shape)\n'
import torch
input = torch.rand(4, 1, 3, 1)
print(input)
output = torch.broadcast_to(input, (4, 3, 3, 3))
print(output)