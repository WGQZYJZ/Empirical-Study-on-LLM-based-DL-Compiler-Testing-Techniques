'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arccosh_\ntorch.Tensor.arccosh_(_input_tensor, )\n'
import torch
input_tensor = torch.rand(2, 3, 4)
output_tensor = torch.Tensor.arccosh_(input_tensor)
print('Input tensor:\n', input_tensor)
print('Output tensor:\n', output_tensor)