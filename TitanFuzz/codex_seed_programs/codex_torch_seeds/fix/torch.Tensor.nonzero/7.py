'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nonzero\ntorch.Tensor.nonzero(_input_tensor, as_tuple=False)\n'
import torch
_input_tensor = torch.randn(3, 4)
print(_input_tensor)
print(_input_tensor.nonzero())
print(_input_tensor.nonzero(as_tuple=True))