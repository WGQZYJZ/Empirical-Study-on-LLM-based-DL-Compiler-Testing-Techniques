'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.pow\ntorch.Tensor.pow(_input_tensor, exponent)\n'
import torch
_input_tensor = torch.randn(3, 5)
print(_input_tensor)
print(_input_tensor.pow(2))
print(_input_tensor.pow(3))
print(_input_tensor.pow(4))
print(_input_tensor.pow(5))
print(_input_tensor.pow(0.5))
print(_input_tensor.pow(0.25))
print(_input_tensor.pow(0.125))