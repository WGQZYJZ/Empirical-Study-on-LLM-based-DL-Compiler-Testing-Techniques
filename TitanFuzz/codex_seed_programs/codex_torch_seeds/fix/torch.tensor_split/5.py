'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensor_split\ntorch.tensor_split(input, indices_or_sections, dim=0)\n'
import torch
input = torch.randn(20, 6)
print('Input: ', input)
print('Input size: ', input.size())
torch.tensor_split(input, 3, dim=1)
print('Output: ', torch.tensor_split(input, 3, dim=1))
print('Output size: ', torch.tensor_split(input, 3, dim=1)[0].size())