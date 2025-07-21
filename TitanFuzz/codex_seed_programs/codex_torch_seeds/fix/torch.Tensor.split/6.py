'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.split\ntorch.Tensor.split(_input_tensor, split_size, dim=0)\n'
import torch
_input_tensor = torch.randn(4, 6)
_input_tensor_split = _input_tensor.split([2, 2, 2], dim=1)
print(_input_tensor)
print(_input_tensor_split)