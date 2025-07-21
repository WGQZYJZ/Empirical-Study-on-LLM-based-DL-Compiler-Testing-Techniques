'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.vsplit\ntorch.vsplit(input, indices_or_sections)\n'
import torch
input = torch.randn(2, 3, 4)
print(input)
print(torch.vsplit(input, 2))