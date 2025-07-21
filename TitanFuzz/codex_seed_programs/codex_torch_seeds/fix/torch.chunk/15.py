'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.chunk\ntorch.chunk(input, chunks, dim=0)\n'
import torch
input = torch.randn(10, 3)
output = torch.chunk(input, 3, dim=1)
print(output)
'\nTask 4: Call the API torch.chunk\ntorch.chunk(input, chunks, dim=0)\n'
output = torch.chunk(input, 2, dim=0)
print(output)