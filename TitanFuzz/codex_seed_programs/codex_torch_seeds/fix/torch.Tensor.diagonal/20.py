'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.diagonal\ntorch.Tensor.diagonal(_input_tensor, offset=0, dim1=0, dim2=1)\n'
import torch
import torch
input_tensor = torch.rand(3, 3)
print(input_tensor)
output_tensor = input_tensor.diagonal()
print(output_tensor)
output_tensor = input_tensor.diagonal(offset=1)
print(output_tensor)
output_tensor = input_tensor.diagonal(dim1=1, dim2=2)
print(output_tensor)