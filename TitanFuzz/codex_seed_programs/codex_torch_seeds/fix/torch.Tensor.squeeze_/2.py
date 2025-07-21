'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.squeeze_\ntorch.Tensor.squeeze_(_input_tensor, dim=None)\n'
import torch
input_tensor = torch.rand(2, 1, 2, 1)
print('Input tensor:')
print(input_tensor)
output_tensor = torch.Tensor.squeeze_(input_tensor, dim=1)
print('Output tensor:')
print(output_tensor)