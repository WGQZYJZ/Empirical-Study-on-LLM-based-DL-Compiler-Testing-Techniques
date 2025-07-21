'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.chunk\ntorch.chunk(input, chunks, dim=0)\n'
import torch
input = torch.randn(3, 5)
print(input)
print(torch.chunk(input, 3, 0))