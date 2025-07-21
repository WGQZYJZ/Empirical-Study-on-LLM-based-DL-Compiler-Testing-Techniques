'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensor_split\ntorch.tensor_split(input, indices_or_sections, dim=0)\n'
import torch
input = torch.randn(4, 2, 3)
print(input)
print(torch.tensor_split(input, 3, dim=1))