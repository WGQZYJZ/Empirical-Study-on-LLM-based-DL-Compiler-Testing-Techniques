'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hsplit\ntorch.hsplit(input, indices_or_sections)\n'
import torch
input = torch.randn(3, 4)
print(input)
print(input.size())
print(torch.hsplit(input, 2))
print(torch.hsplit(input, [2]))
'\nTask 4: Call the API torch.split\ntorch.split(input, split_size, dim=0)\n'
print(torch.split(input, 2, dim=0))
print(torch.split(input, 2, dim=1))
'\nTask 5: Call the API torch.chunk\ntorch.chunk(input, chunks, dim=0)\n'
print(torch.chunk(input, 2, dim=0))
print(torch.chunk(input, 2, dim=1))