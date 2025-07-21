'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.squeeze\ntorch.Tensor.squeeze(_input_tensor, dim=None)\n'
import torch
input_tensor = torch.randn(2, 1, 2, 1, 2)
print('Input tensor: \n', input_tensor)
import torch
input_tensor = torch.randn(2, 1, 2, 1, 2)
print('Input tensor: \n', input_tensor)
output_tensor = torch.Tensor.squeeze(input_tensor, dim=1)
print('Output tensor: \n', output_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.squeeze\ntorch.Tensor.squeeze(_input_tensor, dim=None)\n'
import torch
input_tensor = torch.randn(2, 1, 2, 1, 2)
print('Input tensor: \n', input_tensor)