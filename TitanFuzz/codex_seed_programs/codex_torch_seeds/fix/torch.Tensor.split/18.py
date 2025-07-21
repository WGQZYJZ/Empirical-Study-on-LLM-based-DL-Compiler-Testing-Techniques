'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.split\ntorch.Tensor.split(_input_tensor, split_size, dim=0)\n'
import torch
input_tensor = torch.randn(4, 6)
print(input_tensor)
split_size = 2
split_tensor = torch.Tensor.split(input_tensor, split_size, dim=0)
print(split_tensor)
split_tensor = torch.Tensor.split(input_tensor, split_size, dim=1)
print(split_tensor)