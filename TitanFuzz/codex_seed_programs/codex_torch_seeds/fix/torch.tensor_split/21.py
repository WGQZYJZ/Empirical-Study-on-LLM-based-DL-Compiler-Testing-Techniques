'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensor_split\ntorch.tensor_split(input, indices_or_sections, dim=0)\n'
import torch
data = torch.arange(0, 12)
print(data)
print(torch.tensor_split(data, 3, dim=0))
print(torch.tensor_split(data, [2, 5, 8], dim=0))