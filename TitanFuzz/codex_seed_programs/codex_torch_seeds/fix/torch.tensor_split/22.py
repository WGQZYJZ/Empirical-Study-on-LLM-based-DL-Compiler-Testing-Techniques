'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensor_split\ntorch.tensor_split(input, indices_or_sections, dim=0)\n'
import torch
input = torch.randn(4, 5)
print(input)
print(torch.tensor_split(input, 2, dim=0))
print(torch.tensor_split(input, [1, 2, 3], dim=1))
print(torch.tensor_split(input, 2, dim=1))