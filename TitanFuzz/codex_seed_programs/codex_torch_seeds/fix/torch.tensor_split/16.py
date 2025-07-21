'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensor_split\ntorch.tensor_split(input, indices_or_sections, dim=0)\n'
import torch
input = torch.randn(10, 3)
print(input)
print(input.shape)
print('\n')
print(torch.tensor_split(input, 5, dim=0))
print('\n')
print(torch.tensor_split(input, [2, 4, 6], dim=0))