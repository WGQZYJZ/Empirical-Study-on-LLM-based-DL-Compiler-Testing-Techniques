'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensor_split\ntorch.tensor_split(input, indices_or_sections, dim=0)\n'
import torch
input = torch.randn(20, 4)
print(input)
split_tensor = torch.tensor_split(input, 3, dim=0)
print(split_tensor)
for i in split_tensor:
    print(i)
split_tensor = torch.tensor_split(input, 5, dim=0)
print(split_tensor)
for i in split_tensor:
    print(i)