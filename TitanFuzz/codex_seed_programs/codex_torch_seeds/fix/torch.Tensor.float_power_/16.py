'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.float_power_\ntorch.Tensor.float_power_(_input_tensor, exponent)\n'
import torch
input_tensor = torch.rand(10, 10)
torch.Tensor.float_power_(input_tensor, exponent=2)
print(input_tensor)