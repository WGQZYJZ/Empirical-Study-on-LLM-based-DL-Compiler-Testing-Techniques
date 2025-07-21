'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.exp_\ntorch.Tensor.exp_(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input tensor: \n', input_tensor)
output_tensor = torch.Tensor.exp_(input_tensor)
print('Output tensor: \n', output_tensor)