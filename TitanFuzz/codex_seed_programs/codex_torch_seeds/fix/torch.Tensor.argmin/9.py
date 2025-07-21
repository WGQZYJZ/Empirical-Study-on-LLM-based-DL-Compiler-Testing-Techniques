'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.argmin\ntorch.Tensor.argmin(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.rand(3, 3, 3)
print(input_tensor)
min_index = input_tensor.argmin(dim=2)
print(min_index)
min_index = input_tensor.argmin(dim=1)
print(min_index)
min_index = input_tensor.argmin(dim=0)
print(min_index)