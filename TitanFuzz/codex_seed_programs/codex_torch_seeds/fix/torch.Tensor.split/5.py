'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.split\ntorch.Tensor.split(_input_tensor, split_size, dim=0)\n'
import torch
_input_tensor = torch.rand(10, 3, 2)
_split_tensors = torch.Tensor.split(_input_tensor, 2, dim=0)
print(_split_tensors)