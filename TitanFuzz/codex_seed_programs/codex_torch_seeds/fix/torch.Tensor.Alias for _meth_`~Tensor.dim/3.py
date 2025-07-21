'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.Alias for :meth:`~Tensor.dim\ntorch.Tensor.Alias for :meth:`~Tensor.dim(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3, 4, 5)
_input_tensor = input_tensor
print(_input_tensor.shape)
print(_input_tensor.size())
print(_input_tensor.numel())
print(_input_tensor.dim())
print(_input_tensor.shape)
print(_input_tensor.size())