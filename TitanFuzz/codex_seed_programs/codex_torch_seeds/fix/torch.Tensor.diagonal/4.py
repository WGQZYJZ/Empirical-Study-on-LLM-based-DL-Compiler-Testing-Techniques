'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.diagonal\ntorch.Tensor.diagonal(_input_tensor, offset=0, dim1=0, dim2=1)\n'
import torch
input_tensor = torch.rand(3, 3)
output_tensor = input_tensor.diagonal()
print('input tensor:\n', input_tensor)
print('output tensor:\n', output_tensor)