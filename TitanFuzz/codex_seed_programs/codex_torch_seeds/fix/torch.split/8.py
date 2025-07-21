'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.split\ntorch.split(tensor, split_size_or_sections, dim=0)\n'
import torch
tensor = torch.rand(10, 3)
print(tensor)
split_tensor = torch.split(tensor, split_size_or_sections=5, dim=0)
print(split_tensor)
print(type(split_tensor))
print(split_tensor[0].size())