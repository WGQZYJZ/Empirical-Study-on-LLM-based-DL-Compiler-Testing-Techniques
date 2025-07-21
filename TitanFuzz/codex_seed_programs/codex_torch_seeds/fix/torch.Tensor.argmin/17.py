'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.argmin\ntorch.Tensor.argmin(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.rand(3, 4)
print('Input tensor: \n', input_tensor)
output_tensor = input_tensor.argmin(dim=0)
print('Output tensor: \n', output_tensor)