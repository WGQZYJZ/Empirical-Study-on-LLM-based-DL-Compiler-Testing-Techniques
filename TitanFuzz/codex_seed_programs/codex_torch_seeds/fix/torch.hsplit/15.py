'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hsplit\ntorch.hsplit(input, indices_or_sections)\n'
import torch
input = torch.randn(10, 3)
print(input)
print(torch.hsplit(input, 3))