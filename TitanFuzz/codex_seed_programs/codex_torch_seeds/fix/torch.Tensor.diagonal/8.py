'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.diagonal\ntorch.Tensor.diagonal(_input_tensor, offset=0, dim1=0, dim2=1)\n'
import torch
input_tensor = torch.randint(1, 10, (3, 3))
print(input_tensor)
print(input_tensor.diagonal())
print(input_tensor.diagonal(offset=1))
print(input_tensor.diagonal(offset=(- 1)))
print(input_tensor.diagonal(offset=0, dim1=1, dim2=0))
print(input_tensor.diagonal(offset=1, dim1=1, dim2=0))
print(input_tensor.diagonal(offset=(- 1), dim1=1, dim2=0))