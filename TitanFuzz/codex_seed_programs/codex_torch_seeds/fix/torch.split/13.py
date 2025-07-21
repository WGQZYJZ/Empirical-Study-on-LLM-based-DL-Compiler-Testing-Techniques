'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.split\ntorch.split(tensor, split_size_or_sections, dim=0)\n'
import torch
import torch
input = torch.randn(7, 4)
output = torch.split(input, 2, dim=0)
print(output)