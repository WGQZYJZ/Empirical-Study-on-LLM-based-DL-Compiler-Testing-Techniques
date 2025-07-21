'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.split\ntorch.split(tensor, split_size_or_sections, dim=0)\n'
import torch
tensor = torch.randn(4, 4)
print('Input data: ', tensor)
split_tensor = torch.split(tensor, 4)
print('Split tensor: ', split_tensor)
split_tensor = torch.split(tensor, 2, dim=1)
print('Split tensor: ', split_tensor)
split_tensor = torch.split(tensor, [2, 2], dim=1)
print('Split tensor: ', split_tensor)
split_tensor = torch.split(tensor, [2, 2], dim=0)
print('Split tensor: ', split_tensor)