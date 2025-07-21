'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.float_power_\ntorch.Tensor.float_power_(_input_tensor, exponent)\n'
import torch
input_tensor = torch.randn(10, 10)
print(input_tensor)
exponent = torch.randn(10, 10)
print(exponent)
torch.Tensor.float_power_(input_tensor, exponent)
print(input_tensor)