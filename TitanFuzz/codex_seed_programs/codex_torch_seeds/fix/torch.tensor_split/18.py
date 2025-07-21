'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensor_split\ntorch.tensor_split(input, indices_or_sections, dim=0)\n'
import torch
input = torch.rand(5, 3, 10)
output = torch.tensor_split(input, 5, dim=0)
print(output)
print(len(output))
print(output[0].size())
print(output[1].size())
print(output[2].size())
print(output[3].size())
print(output[4].size())