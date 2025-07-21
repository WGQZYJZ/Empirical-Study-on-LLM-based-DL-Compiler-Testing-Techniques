'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.diagonal\ntorch.Tensor.diagonal(_input_tensor, offset=0, dim1=0, dim2=1)\n'
import torch
_input_tensor = torch.randn(3, 3)
print(_input_tensor)
_diagonal_tensor = _input_tensor.diagonal()
print(_diagonal_tensor)