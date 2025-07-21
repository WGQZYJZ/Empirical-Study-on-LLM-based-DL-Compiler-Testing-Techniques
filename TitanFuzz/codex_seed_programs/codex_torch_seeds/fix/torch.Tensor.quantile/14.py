'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.quantile\ntorch.Tensor.quantile(_input_tensor, q, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(4, 4)
print('Input tensor: \n', input_tensor)
q = 0.5
dim = 0
keepdim = False
output = torch.Tensor.quantile(input_tensor, q, dim, keepdim)
print('Output tensor: \n', output)