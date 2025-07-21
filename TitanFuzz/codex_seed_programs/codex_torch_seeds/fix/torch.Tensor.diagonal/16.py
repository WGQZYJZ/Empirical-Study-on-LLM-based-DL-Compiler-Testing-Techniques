'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.diagonal\ntorch.Tensor.diagonal(_input_tensor, offset=0, dim1=0, dim2=1)\n'
import torch
input_tensor = torch.randn(3, 3)
print('input_tensor = ', input_tensor)
diagonal_tensor = input_tensor.diagonal()
print('diagonal_tensor = ', diagonal_tensor)