'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensor_split\ntorch.tensor_split(input, indices_or_sections, dim=0)\n'
import torch
input = torch.randn(2, 3, 4)
print(input)
output = torch.tensor_split(input, 2, dim=0)
print(output)
output = torch.tensor_split(input, 3, dim=1)
print(output)
output = torch.tensor_split(input, 4, dim=2)
print(output)