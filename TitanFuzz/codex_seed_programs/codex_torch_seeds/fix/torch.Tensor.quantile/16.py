'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.quantile\ntorch.Tensor.quantile(_input_tensor, q, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(10)
print('Input Tensor: {}'.format(input_tensor))
quantile_tensor = torch.Tensor.quantile(input_tensor, 0.5)
print('Quantile Tensor: {}'.format(quantile_tensor))