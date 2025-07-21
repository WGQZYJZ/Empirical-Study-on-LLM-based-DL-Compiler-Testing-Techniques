'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.digamma_\ntorch.Tensor.digamma_(_input_tensor)\n'
import torch
input_tensor = torch.randn(8, 8)
output_tensor = torch.Tensor.digamma_(input_tensor)
print(output_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dist\ntorch.Tensor.dist(_input_tensor, _input_tensor, _p=2.0)\n'
import torch
input_tensor_1 = torch.randn(8, 8)
input_tensor_2 = torch.randn(8, 8)
output_tensor = torch.Tensor.dist(input_tensor_1, input_tensor_2, 2.0)
print(output_tensor)