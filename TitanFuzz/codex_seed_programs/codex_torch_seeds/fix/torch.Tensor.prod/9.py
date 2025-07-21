'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.prod\ntorch.Tensor.prod(_input_tensor, dim=None, keepdim=False, dtype=None)\n'
import torch
import torch
_input_tensor = torch.rand(5, 5)
print(_input_tensor.prod(dim=0))
print(_input_tensor.prod(dim=1))
print(_input_tensor.prod(dim=0, keepdim=True))
print(_input_tensor.prod(dim=1, keepdim=True))
print(_input_tensor.prod(dim=(- 1)))
print(_input_tensor.prod(dim=(- 2)))