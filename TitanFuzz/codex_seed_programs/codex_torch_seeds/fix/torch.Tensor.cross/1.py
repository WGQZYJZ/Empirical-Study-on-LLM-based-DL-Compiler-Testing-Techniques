'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cross\ntorch.Tensor.cross(_input_tensor, other, dim=-1)\n'
import torch
input_tensor = torch.rand(2, 3)
other = torch.rand(2, 3)
print(input_tensor)
print(other)
print(torch.Tensor.cross(input_tensor, other))