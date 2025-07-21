'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.any\ntorch.Tensor.any(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(2, 2)
print('Input tensor: ', input_tensor)
output_tensor = input_tensor.any(dim=None, keepdim=False)
print('Output tensor: ', output_tensor)