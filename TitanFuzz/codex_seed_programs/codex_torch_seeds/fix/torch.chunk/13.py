'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.chunk\ntorch.chunk(input, chunks, dim=0)\n'
import torch
input = torch.randn(2, 3)
print(input)
chunks = torch.chunk(input, 2, dim=0)
print(chunks)
print(chunks[0])
print(chunks[1])