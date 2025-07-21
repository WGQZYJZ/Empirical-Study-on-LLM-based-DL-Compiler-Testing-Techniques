'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nonzero\ntorch.Tensor.nonzero(_input_tensor, as_tuple=False)\n'
import torch
import torch
_input_tensor = torch.randn(3, 3)
_input_tensor[(0, 0)] = 0
_input_tensor[(1, 1)] = 0
_input_tensor[(2, 2)] = 0
print(_input_tensor.nonzero())