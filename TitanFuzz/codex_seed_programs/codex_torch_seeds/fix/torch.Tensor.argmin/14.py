'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.argmin\ntorch.Tensor.argmin(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(3, 4)
print('Input tensor: ', input_tensor)
output_tensor = input_tensor.argmin(dim=0, keepdim=False)
print('Output tensor: ', output_tensor)