'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensor_split\ntorch.tensor_split(input, indices_or_sections, dim=0)\n'
import torch
x = torch.randn(2, 3, 4)
print(x)
y = torch.tensor_split(x, 3, dim=2)
print(y)