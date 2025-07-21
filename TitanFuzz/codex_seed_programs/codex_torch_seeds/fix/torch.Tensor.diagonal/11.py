'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.diagonal\ntorch.Tensor.diagonal(_input_tensor, offset=0, dim1=0, dim2=1)\n'
import torch
input_tensor = torch.randint(0, 10, (3, 3))
print('Input tensor: \n', input_tensor)
print('Diagonal of input tensor: \n', input_tensor.diagonal())