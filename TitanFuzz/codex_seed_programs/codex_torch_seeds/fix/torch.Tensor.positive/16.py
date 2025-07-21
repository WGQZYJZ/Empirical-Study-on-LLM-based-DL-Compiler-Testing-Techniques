'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.positive\ntorch.Tensor.positive(_input_tensor)\n'
import torch
import torch
input_tensor = torch.randn(3, 3)
output_tensor = torch.Tensor.positive(input_tensor)
print(input_tensor)
print(output_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.pow\ntorch.Tensor.pow(_input_tensor, _exponent)\n'
import torch
import torch
input_tensor = torch.randn(3, 3)
exponent = torch.randn(3, 3)
output_tensor = torch.Tensor.pow(input_tensor, exponent)
print(input_tensor)
print(exponent)