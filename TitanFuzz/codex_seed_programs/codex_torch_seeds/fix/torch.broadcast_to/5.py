'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.broadcast_to\ntorch.broadcast_to(input, shape)\n'
import torch
input = torch.rand(1, 3, 4, 5)
output = torch.broadcast_to(input, (2, 3, 4, 5))
print(output.shape)
print(output)