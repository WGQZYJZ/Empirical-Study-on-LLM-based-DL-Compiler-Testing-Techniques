'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.float_power_\ntorch.Tensor.float_power_(_input_tensor, exponent)\n'
import torch
input_tensor = torch.randn(4, 4)
print(input_tensor)
torch.Tensor.float_power_(input_tensor, 2)
print(input_tensor)
torch.Tensor.float_power_(input_tensor, 0.5)
print(input_tensor)